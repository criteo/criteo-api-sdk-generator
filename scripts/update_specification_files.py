"Automate downloading all versions' OAS specifications, saving them with the correct naming and removing the obsolete ones."

# Implementation notes:
#
# - The handling of existing files (esp. deletion) is done in an "optimistic way"
# based on the assumption that they are all already under version control
# (which is indeed the typical case today).
#
# - Similary the "HTTP get" is also done in an optmistic way based on the assumption
# that the script is run manually in a fairly simple setup but to avoid any install (beyond python).

import sys, getopt
from pathlib import Path
import logging

import urllib.request
import urllib.parse

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOGGER = logging.getLogger(__name__)
ALL_API_SERVICES = ["marketingSolutions", "retailMedia"]
NUM_YEARS_TO_KEEP = 1
EVERGREEN_VERSIONS = {"preview",}
SPECIFICATION_EXTENSION = ".json"


def _get_year_month_from_version_name(version_name):
  parts = version_name.split("-")
  if len(parts) != 2 or len(parts[0]) != 4 or len(parts[1]) != 2:
    raise NotImplementedError(f"Unsupported version name: {version_name}.")
  else:
    return map(int, parts)


def _is_more_recent_than_reference_version_minus(candidate_version, reference_version, num_years_before):
  year, month = _get_year_month_from_version_name(reference_version)
  threshold_year = year - num_years_before
  threshold_month = month
  candidate_year, candidate_month = _get_year_month_from_version_name(candidate_version)
  return (candidate_year, candidate_month) >= (threshold_year, threshold_month)


def _get_service_version_from_specification_filepath(filepath):
   return Path(filepath).stem.split("_")


def remove_out_of_support_specifications(specification_folder, reference_version, num_years_to_keep):
  folder_path = Path(specification_folder)
  for specification_path in folder_path.glob(f"*{SPECIFICATION_EXTENSION}"):
    _, version = _get_service_version_from_specification_filepath(specification_path)
    if version.lower() in EVERGREEN_VERSIONS:
        continue
    if _is_more_recent_than_reference_version_minus(version, reference_version, num_years_to_keep):
        continue
    specification_path.unlink()


def download_specification(version, api_service, specification_folder, gateway_service):
    folder_path = Path(specification_folder)
    target_file = folder_path / f"{api_service.lower()}_{version}{SPECIFICATION_EXTENSION}"
    specification_url = f"{gateway_service}/{version.lower()}/{api_service.lower()}/open-api-specifications.json"
    try:
        f = urllib.request.urlopen(specification_url)
        if target_file.exists():
            LOGGER.debug(f"Removing existing file {target_file} as it is about to be replaced")
        with target_file.open("wb") as specification:
            specification.write(f.read())
    except urllib.error.HTTPError as e:
        LOGGER.error(f"Failed to get specification for {version}, {api_service} from {specification_url}")
        raise e


def update_previous_specifications(specification_folder, gateway_service):
  folder_path = Path(specification_folder)
  for specification_path in folder_path.glob(f"*{SPECIFICATION_EXTENSION}"):
    api_service_lower, version = _get_service_version_from_specification_filepath(specification_path)
    api_service_candidates = [
      candidate_service
      for candidate_service in ALL_API_SERVICES
      if candidate_service.lower() == api_service_lower]
    if not api_service_candidates:
      raise RuntimeError(f"Cannot recognize the API service associated to {specification_path} ({api_service_lower} is unknown)")
    api_service = api_service_candidates[0]
    download_specification(version, api_service, specification_folder, gateway_service)


def main():
    help_msg = f'{__doc__}\n{__file__} -r <version to release> -s <path to specification folder> -c <URL to the configuration service>'
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hvr:s:g:", ["help", "verbose", "release=", "specification_folder=", "gateway_service="])
    except getopt.GetoptError:
        LOGGER.error(f'Invalid call: [help] {help_msg}')
        sys.exit(2)

    for option, value in opts:
        if option in ('-h', '--help'):
            LOGGER.info(help_msg)
            sys.exit()
        elif option in ('-v', ):
           LOGGER.setLevel(logging.DEBUG)
        elif option in ('-r', '--release'):
            release = value
        elif option in ('-s', '--specification_folder'):
            specification_folder = value
        elif option in ('-g', '--gateway_service'):
            gateway_service = value
        else:
            raise Exception(f'Unsupported command line option ({option}={value}).')

    LOGGER.info("Removing obsolete versions")
    remove_out_of_support_specifications(specification_folder, release, NUM_YEARS_TO_KEEP)
    LOGGER.info("Updating previous relevant versions")
    update_previous_specifications(specification_folder, gateway_service)
    LOGGER.info("Downloading the newest specifications")
    for api_service in ALL_API_SERVICES:
        LOGGER.info(f"Getting new specifications for {api_service}/{release}")
        download_specification(release, api_service, specification_folder, gateway_service)


if __name__ == '__main__':
  main()
