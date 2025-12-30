import os

class File:
    def __init__(self,path,extension):
        self.path = path
        self.name = os.path.basename(path)
        self.extension = extension
    
    def __repr__(self) -> str:
        return f"{self.name} in {self.path} of type {self.extension}"
