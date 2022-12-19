from shared.utils import run_command, CommandException
import os

class OpenApiToPostman():
    """
    The most important thing to know here are the two parameters: 
    _requestParametersResolution: Select whether to generate the 
    request parameters based on the schema or the example in the schema.

    _responseParametersResolution: Select whether to generate the 
    response parameters based on the schema or the example in the schema.

    Once there is a unified documentation format we can switch
    the defaults to be 'Example'.

    P.S the difference exampleParametersResolution vs _responseParametersResolution 
    is intentional; it's a typo in Postman product.
    """
    def __init__(self, _folderStrategy='Tags', _requestParametersResolution='Schema', _responseParametersResolution='Example', _filelist='',_root_postman_specs_dir='./postman-specifications'):
        self.folderStrategy = _folderStrategy
        self.requestParametersResolution = _requestParametersResolution
        self.responseParametersResolution = _responseParametersResolution
        self.filelist = _filelist
        self.root_postman_specs_dir = _root_postman_specs_dir

    def clean_convert_to_collection(self):
        run_command("rm -rf {0} && mkdir {0}".format(self.root_postman_specs_dir))
        postman_specification_files = []
        for file in self.filelist:
            outputfilename = os.getcwd()+'/'+self.root_postman_specs_dir +'/'+file.split('/')[-1]
            run_command("openapi2postmanv2 -s \"{0}\" -o \"{1}\" -p -O folderStrategy={2},requestParametersResolution={3},exampleParametersResolution={4},optimizeConversion=false,schemaFaker=false,stackLimit=50".format(file, outputfilename, self.folderStrategy, self.requestParametersResolution, self.responseParametersResolution))
            if os.path.isfile(outputfilename) and outputfilename.endswith('json'):
                postman_specification_files.append(outputfilename)
        return postman_specification_files