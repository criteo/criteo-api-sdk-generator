import requests
import logging
import json
import pdb 
from requests.auth import HTTPBasicAuth
import os
from os import path
import sys
from shared.documentation.postman_client import OpenApiToPostman
from shared.models.criteo_service import CriteoService

DEBUG = 1
IS_PROD = int(os.getenv('IS_PROD'))

#constants

API_KEY = os.getenv('POSTMAN_MANAGEMENT')

if (IS_PROD):
	workspaceId = os.getenv('POSTMAN_WORKSPACE_ID')
else:
	workspaceId = os.getenv('POSTMAN_PREPROD_WORKSPACE_ID')

if workspaceId is None:
	raise ValueError("No active workspace is defined")

#ROOT_POSTMAN_SPECS_DIR is an output folder

ROOT_POSTMAN_SPECS_DIR = 'postman-specifications'
ROOT_SOURCE_SPECS_DIR =  'api-specifications'

GET_ALL_WORKSPACE_URL = f'https://api.getpostman.com/collections?workspace={workspaceId}'
COLLECTIONS_UPDATE_URL = 'https://api.getpostman.com/collections/%s'
COLLECTIONS_CREATE_URL = f'https://api.getpostman.com/collections?workspace={workspaceId}'
HEADER = {
	'Content-Type': 'application/json',
	'X-API-Key': API_KEY
}
 

if DEBUG:
	logging.basicConfig()
	logging.getLogger().setLevel(logging.DEBUG)
	requests_log = logging.getLogger("requests.packages.urllib3")
	requests_log.setLevel(logging.DEBUG)
	requests_log.propagate = True


def get_workspace_data():
	workspace_response = requests.get(GET_ALL_WORKSPACE_URL, headers=HEADER)
	if workspace_response.status_code != 200:
		raise requests.exceptions.HTTPError("Could not fetch Postman collections")
	workspace_response_json = workspace_response.json()
	return workspace_response_json

def prepare_collection_data(read_collection_data, name):
	collection_wrapper = {}
	read_collection_data_json = json.loads(read_collection_data)
	read_collection_data_json['info']['name'] = name
	collection_wrapper['collection'] = read_collection_data_json
	JSON_collection_wrapper = json.dumps(collection_wrapper)
	return JSON_collection_wrapper

def update_collection(uid_to_update, collection_name_to_update, file):
		with open(file, encoding="utf-8") as f:
			read_collection_data = f.read()
			COLLECTIONS_UPDATE_URL_CURR = COLLECTIONS_UPDATE_URL%uid_to_update
			JSON_collection_wrapper = prepare_collection_data(read_collection_data, collection_name_to_update)
			collections_response = requests.put(COLLECTIONS_UPDATE_URL_CURR, headers=HEADER, data=JSON_collection_wrapper)
			if collections_response.status_code != 200:
				raise ValueError("Could not update Postman collections: " + collections_response.status_code)
			f.close()

def create_collection(collection_name_to_update, file):
		with open(file, encoding="utf-8") as f:
			read_collection_data = f.read()
			COLLECTIONS_UPDATE_URL_CURR = COLLECTIONS_CREATE_URL
			JSON_collection_wrapper = prepare_collection_data(read_collection_data, collection_name_to_update)
			print(COLLECTIONS_UPDATE_URL_CURR)
			collections_response = requests.post(COLLECTIONS_UPDATE_URL_CURR, headers=HEADER, data=JSON_collection_wrapper)
			if collections_response.status_code != 200:
				collections_response.json()
				raise ValueError("Could not create Postman collections: "+str(collections_response.status_code))
			f.close()

def prepare_postman_specs_data():
	
	source_files = [f'{ROOT_SOURCE_SPECS_DIR}/{f}' for f in os.listdir(ROOT_SOURCE_SPECS_DIR) if os.path.isfile(f'{ROOT_SOURCE_SPECS_DIR}/{f}') and f'{ROOT_SOURCE_SPECS_DIR}/{f}'.endswith('json')]
	postman_converter_instance = OpenApiToPostman(_filelist=source_files,_root_postman_specs_dir=ROOT_POSTMAN_SPECS_DIR)
	postman_specification_files = postman_converter_instance.clean_convert_to_collection()
	if len(postman_specification_files) == 0:
		raise ValueError("Could not update Postman collections")
	return postman_specification_files


def main():
	try:
		# get all collections from the workspace

		postman_specification_files = prepare_postman_specs_data()

		solutions_naming_map = dict({CriteoService.marketingsolutions:"MS API", CriteoService.retailmedia:"RM API"})
		
		workspace_response_json = get_workspace_data()

		for file in postman_specification_files:
			create_flag = False
			print('Updating/Creating collection: '+file)
			solution, version = os.path.basename(file).split('.')[0].split('_')
			collection_name_to_update = f'{solutions_naming_map[solution]} {version}'
			print(collection_name_to_update)
			collection_id_to_update_list = [collection['uid'] for collection in workspace_response_json['collections'] if collection['name'].upper() == collection_name_to_update.upper()]
			if len(collection_id_to_update_list) > 1:
				raise ValueError("More than 1 collection with the identical name. Please make sure collection names are unique")
			elif len(collection_id_to_update_list) == 0:
				create_flag = True
			else:
				uid_to_update = collection_id_to_update_list[0]
			if create_flag == False:
				update_collection(uid_to_update,collection_name_to_update,file)
			else:
				create_collection(collection_name_to_update,file)

	except OSError as err:
	    print("File manipulation error:", err)
	    sys.exit(0)
	except requests.exceptions.ConnectionError as err:
		print("Requests failure: e.g. DNS failure, refused connection", err)
		sys.exit(0)
	except requests.exceptions.HTTPError as err:
		print("Invalid HTTP response", err)
		sys.exit(0)
	except Exception as e:
	    print("Generic error or a network error:", err)
	    sys.exit(0)



if __name__ == '__main__':
	main()




