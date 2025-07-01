"""POC / Preprocess OAS files for changelog comparison: check files are valid OAS, remove version prefix in path,
and dereferences schemas (a.k.a. inlining or antialiasing)"""
import subprocess
import sys, getopt
from pathlib import Path
import logging
from prance import ResolvingParser, ValidationError
import json
from os import path
import re
from itertools import groupby
from operator import itemgetter

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def set_endpoint(change):
    pattern = r"\/([a-zA-Z0-9~\{\}-]+)"
    change['endpoint'] = '?'
    if change['NewJsonRef'] and change['OldJsonRef'] or change['NewJsonRef'] is None or change['OldJsonRef'] is None:
        match_parts = re.findall(pattern, change['OldJsonRef'] or change['NewJsonRef'])
        if match_parts is not []:
            endpoint_path = match_parts[1].replace('~1', '/')
            if len(match_parts) > 2:
                change['endpoint'] = match_parts[2].upper() + ' ' + endpoint_path
            else:
                change['endpoint'] = endpoint_path
    return change

def format_changelog(grouped_changes):
    print(grouped_changes)
    for endpoint, changes in grouped_changes.items():
        print(endpoint)
        for change in changes:
            print(f"\t{change['Code']}: {change['Message']} [at {change['NewJsonRef'] or change['OldJsonRef']}]")


def compute_changelog(from_output_file,  to_output_file):
    ignored = [10021]
    # TODO: we should also ignore schema changes for non-successful reponses
    command = f"openapi-compare -o {from_output_file} -n {to_output_file} -f Json"
    output = subprocess.check_output(command, shell=True)
    changes = json.loads(output)
    changes = [set_endpoint(change) for change in changes if change['Id'] not in ignored]
    changes.sort(key=itemgetter("endpoint"))
    grouped_changes = {k: list(v) for k, v in groupby(changes, key=itemgetter("endpoint"))}
    print(format_changelog(grouped_changes))

def recursion_limit_handler(recursion_limit, parsed_reference_url, references):
    print(f"Reached recursion limit {recursion_limit}, at {parsed_reference_url}")
    # Replace circular references with unspecific object
    return { "type": "object" }

def prepare_input_file(input_file, output_file):
    try:
        parser = ResolvingParser(url=input_file, encoding='utf-8', recursion_limit_handler=recursion_limit_handler, backend='openapi-spec-validator', strict=False)
        flattened_spec = parser.specification

        version = input_file.split('.')[-2].split('_')[-1]
        url = flattened_spec['servers'][0]['url'] + '/' + version
        flattened_spec['servers'][0]['url'] = url

        for prefixed_path in list( flattened_spec['paths'].keys()):
            no_prefix_path = prefixed_path.replace(f"/{version}/", '/')
            flattened_spec['paths'][no_prefix_path] = flattened_spec['paths'].pop(prefixed_path)

        flattened_spec['components'] = {}
        with open(output_file, "w") as f:
            json.dump(flattened_spec, f, indent=2)
    except ValidationError as e:
        print(e)
    

def main():
    help_msg = f'{__doc__}\n{__file__} -f <OAS from> -t <OAS to>'
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "h:f:t:", ["help", "from=", "to="])
    except getopt.GetoptError:
        LOGGER.error(f'Invalid call: [help] {help_msg}')
        sys.exit(2)

    for option, value in opts:
        if option in ('-h', '--help'):
            LOGGER.info(help_msg)
            sys.exit()
        elif option in ('-f', '--from'):
            from_oas_filepath = value
        elif option in ('-t', '--to'):
            to_oas_filepath = value
        else:
            raise Exception(f'Unsupported command line option ({option}={value}).')

    if from_oas_filepath is None or to_oas_filepath is None:
        LOGGER.error("Missing one of the input file paths")
        exit()
    from_output_file = Path(f"changelog/{path.basename(from_oas_filepath)}.processed")
    to_output_file = Path(f"changelog/{path.basename(to_oas_filepath)}.processed")
    if not path.exists(from_output_file) or not path.exists(to_output_file):
        LOGGER.info(f"Processing from OAS file: {from_oas_filepath}")
        prepare_input_file(from_oas_filepath, from_output_file)
        LOGGER.info(f"Processing to OAS file: {to_oas_filepath}")
        prepare_input_file(to_oas_filepath, to_output_file)

    compute_changelog(from_output_file, to_output_file)

if __name__ == '__main__':
  main()