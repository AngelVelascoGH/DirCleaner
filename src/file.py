import os

class File:
    def __init__(self,path,extension):
        self.path = path
        self.name = os.path.basename(path)
        self.extension = extension
    
    def __repr__(self) -> str:
        return f"{self.name} in {self.path} of type {self.extension}"

    def set_name(self,name):
        self.name = name

    def set_path(self,path):
        self.path = path

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def get_extension(self):
        return self.extension

    def set_extension(self,extension):
        self.extension = extension
