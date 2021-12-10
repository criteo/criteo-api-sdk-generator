import os
from os import path
import shutil

class IFsClient:
    def change_dir(self, path):
        """Change current directory to given path"""
        pass

    def remove(self, path):
        """Remove directory (recursively) or file"""
        pass

    def copy(self, source, destination):
        """Copy directory (recursively) or folder"""
        pass


class FsClient(IFsClient):
    def change_dir(self, path):
        os.chdir(path)

    def remove(self, file_path):
        if path.isfile(file_path):
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)       

    def copy(self, source, destination):
        if path.isfile(source):
            shutil.copy(source, destination)
        else:
            shutil.copytree(source, destination)
