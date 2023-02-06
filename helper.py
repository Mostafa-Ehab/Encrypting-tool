import os

class PathControl:
    def __init__(self):
        os.chdir("/")

    def list_files(self):
        files = os.scandir()
        return files

    def set_dir(self, file):
        if os.path.isdir(file):
            os.chdir(file)
            return True
        return False

    def back(self):
        pass