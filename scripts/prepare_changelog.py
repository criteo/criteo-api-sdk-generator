"""POC / Preprocess OAS files for changelog comparison: check files are valid OAS, remove version prefix in path,
and dereferences schemas (a.k.a. inlining or antialiasing)"""

import subprocess
import sys, getopt
from pathlib import Path
from prance import ResolvingParser, ValidationError
import json
from os import path
import re
from itertools import groupby
from operator import itemgetter
import logging

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def set_endpoint(change: dict) -> dict:
    pattern = r"\/([a-zA-Z0-9~\{\}-]+)"
    change["endpoint"] = "?"
    if (
        change["NewJsonRef"]
        and change["OldJsonRef"]
        or change["NewJsonRef"] is None
        or change["OldJsonRef"] is None
    ):
        match_parts = re.findall(pattern, change["OldJsonRef"] or change["NewJsonRef"])
        if match_parts is not []:
            endpoint_path = match_parts[1].replace("~1", "/")
            if len(match_parts) > 2:
                change["endpoint"] = match_parts[2].upper() + " " + endpoint_path
            else:
                # TODO: Get method from path when ADDED PATH OR REMOVE PATH (possibly, change openapicomparator)
                change["endpoint"] = endpoint_path
    return change


def format_changelog(grouped_changes: dict):
    output = []
    for endpoint, changes in grouped_changes.items():
        output.append(f"{endpoint}")
        for change in changes:
            change_in_request = (
                change["NewJsonRef"] is not None
                and (
                    "/requestBody/" in change["NewJsonRef"]
                    or "/parameters/" in change["NewJsonRef"]
                )
                or change["OldJsonRef"] is not None
                and (
                    "/requestBody/" in change["OldJsonRef"]
                    or "/parameters/" in change["OldJsonRef"]
                )
            )
            change_in_response = (
                change["NewJsonRef"] is not None
                and "/responses/" in change["NewJsonRef"]
                or change["OldJsonRef"] is not None
                and "/responses/" in change["OldJsonRef"]
            )
            if change_in_request or change_in_response:
                output.append(
                    f"\t{change['Code']} "
                    f"[in {'request' if change_in_request else ''}"
                    f"{' and ' if change_in_request and change_in_response else ''}"
                    f"{'response' if change_in_response else ''}]: "
                    f"{change['Message']}"
                )
            else:
                output.append(f"\t{change['Code']}: {change['Message']}")
    return "\n".join(output)


def compute_changelog(
    from_output_file: Path, to_output_file: Path, ignored_codes=[10021, 1001, 1037]
):
    # Improvements:
    # - filter out changes to non-successful reponses
    # - add info about what is added or removed (e.g., in enum)
    # - index by endpoint, not path anytime possible
    command = f"openapi-compare -o {from_output_file} -n {to_output_file} -f Json"
    output = subprocess.check_output(command, shell=True)
    changes = json.loads(output)
    changes = [
        set_endpoint(change) for change in changes if change["Id"] not in ignored_codes
    ]
    changes.sort(key=itemgetter("endpoint"))
    grouped_changes = {
        k: list(v) for k, v in groupby(changes, key=itemgetter("endpoint"))
    }
    print(format_changelog(grouped_changes))


def recursion_limit_handler(recursion_limit, parsed_reference_url, references):
    LOGGER.warning(
        f"Reached recursion limit {recursion_limit}, at {parsed_reference_url}, reference are replaced with unspecific object schema"
    )
    return {"type": "object"}


def simplify_content_types(content_object: dict):
    content_types = list(content_object.keys())
    if len(content_types) > 1:
        if "application/json" in content_types:
            extra_content_types = [
                content_type
                for content_type in content_types
                if content_type != "application/json"
            ]
        else:
            extra_content_types = content_types[1:]
        for content_type_to_remove in extra_content_types:
            content_object.pop(content_type_to_remove)


def prepare_input_file(input_file: str, output_file: Path):
    try:
        # Unalising
        parser = ResolvingParser(
            url=input_file,
            encoding="utf-8",
            recursion_limit_handler=recursion_limit_handler,
            backend="openapi-spec-validator",
            strict=False,
        )
        flattened_spec = parser.specification
        if flattened_spec is None:
            raise ValidationError()
        flattened_spec["components"] = {}

        # Unprefixing
        version = input_file.split(".")[-2].split("_")[-1]
        url = flattened_spec["servers"][0]["url"] + "/" + version
        flattened_spec["servers"][0]["url"] = url

        for prefixed_path in list(flattened_spec["paths"].keys()):
            no_prefix_path = prefixed_path.replace(f"/{version}/", "/")
            flattened_spec["paths"][no_prefix_path] = flattened_spec["paths"].pop(
                prefixed_path
            )

        # Simplify response status codes (remove non-successful) and content types (keep one)
        for path, path_obj in flattened_spec["paths"].items():
            for op, op_obj in path_obj.items():
                if "requestBody" in op_obj and len(op_obj["requestBody"].values()) > 0:
                    simplify_content_types(op_obj["requestBody"]["content"])
                if "responses" in op_obj:
                    non_succesful_responses = [
                        status_code
                        for status_code in op_obj["responses"].keys()
                        if str(status_code)[0] != '2'
                    ]
                    for status_code in non_succesful_responses:
                        op_obj["responses"].pop(status_code)
                    if len(op_obj["responses"].values()) > 0:
                        successful_response = next(iter(op_obj["responses"].values()))
                        if 'content' in successful_response:
                            simplify_content_types(successful_response["content"])
                        else:
                            LOGGER.info(f"No content for {op} {path} status code = {op_obj['responses'].keys()}")

        with open(output_file, "w") as f:
            json.dump(flattened_spec, f, indent=2)
    except ValidationError as e:
        LOGGER.error(e)


def main():
    help_msg = f"{__doc__}\n{__file__} -f <OAS from> -t <OAS to>"
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "h:f:t:", ["help", "from=", "to="])
    except getopt.GetoptError:
        LOGGER.error(f"Invalid call: [help] {help_msg}")
        sys.exit(2)

    from_oas_filepath, to_oas_filepath = None, None
    for option, value in opts:
        if option in ("-h", "--help"):
            LOGGER.info(help_msg)
            sys.exit()
        elif option in ("-f", "--from"):
            from_oas_filepath = value
        elif option in ("-t", "--to"):
            to_oas_filepath = value
        else:
            raise Exception(f"Unsupported command line option ({option}={value}).")

    if from_oas_filepath is None or to_oas_filepath is None:
        LOGGER.error("Missing one of the input file paths")
        exit()
    from_output_file = Path(f"{path.dirname(to_oas_filepath)}/{path.basename(from_oas_filepath)}.processed")
    to_output_file = Path(f"{path.dirname(to_oas_filepath)}/{path.basename(to_oas_filepath)}.processed")
    if not path.exists(from_output_file) or not path.exists(to_output_file):
        LOGGER.info(f"Processing from OAS file: {from_oas_filepath}")
        prepare_input_file(from_oas_filepath, from_output_file)
        LOGGER.info(f"Processing to OAS file: {to_oas_filepath}")
        prepare_input_file(to_oas_filepath, to_output_file)

    compute_changelog(from_output_file, to_output_file)


if __name__ == "__main__":
    main()
