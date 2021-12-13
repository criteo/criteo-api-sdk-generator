import os
from os import path
import shutil

class IFsClient:
    def list_dir(self, dir_path):
        """List files and directories in a given folder"""
        pass

    def change_dir(self, dir_path):
        """Change current directory to given path"""
        pass

    def remove(self, path):
        """Remove directory (recursively) or file"""
        pass

    def copy(self, source, destination):
        """Copy directory (recursively) or folder"""
        pass

    def exist(self, file_path):
        """check if file or folder exists"""
        pass


class FsClient(IFsClient):
    def list_dir(self, dir_path):
        return os.listdir(dir_path)

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
    
    def exists(self, file_path):
        return path.exists(file_path)
