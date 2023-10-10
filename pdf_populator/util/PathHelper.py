import sys
import os
from os import listdir
from os.path import isfile, join


class PathHelper:

    def __init__(self, debug_mode: bool):
        self.debug_mode = debug_mode


    def findFolderPath(self, folder_name: str):

        if self.debug_mode:
            # Get the absolute path to the directory containing the script
            curr_dir = os.path.dirname(os.path.abspath(__file__))
        else:
            # Get the absolute path to the directory containing the executable
            curr_dir = os.path.dirname(sys.executable)
        
        # Check if the folder exists in the current directory
        folder_path = os.path.join(curr_dir, folder_name)
        if os.path.exists(folder_path):
            return folder_path

        # Check if the folder exists one level up
        parent_dir = os.path.dirname(curr_dir)
        folder_path = os.path.join(parent_dir, folder_name)
        if os.path.exists(folder_path):
            return folder_path
        
        # Check if the folder exists two levels up
        parent_parent_dir = os.path.dirname(parent_dir)
        folder_path = os.path.join(parent_parent_dir, folder_name)
        if os.path.exists(folder_path):
            return folder_path

        # If the folder is not found in either locations, return None
        return None
    
    def loadFilesInFolder(self, folder_path):
        return [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
