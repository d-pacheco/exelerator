import os
import sys


def findFolderPath(folder_name):

    # Get the absolute path to the directory containing the script
    executable_dir = os.path.dirname(sys.executable)
    
    # Check if the folder exists in the current directory
    folder_path = os.path.join(executable_dir, folder_name)
    if os.path.exists(folder_path):
        return folder_path

    # Check if the folder exists one level up
    parent_dir = os.path.dirname(executable_dir)
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
