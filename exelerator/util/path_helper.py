import sys
import os
from os import listdir
from os.path import isfile, join
from typing import List


class PathHelper:
    def __init__(self, debug_mode: bool):
        self.debug_mode = debug_mode

    def find_path(self, folder_name: str):
        if self.debug_mode:
            # Get the absolute path to the directory containing the script
            curr_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(curr_dir)
            root_dir = os.path.dirname(parent_dir)
        else:
            # Get the absolute path to the directory containing the executable
            root_dir = os.path.dirname(sys.executable)
        
        # Check if the folder exists in the current directory
        folder_path = os.path.join(root_dir, folder_name)
        if os.path.exists(folder_path):
            return folder_path

        # If the folder is not found in either locations, return None
        return None

    @staticmethod
    def load_files_in_folder(folder_path) -> List[str]:
        return [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
