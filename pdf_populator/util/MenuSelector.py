from os import listdir
from os.path import isfile, join


def SelectTemplateFile(template_path):
    template_files = [f for f in listdir(template_path) if isfile(join(template_path, f))]
    if len(template_files) != 0:
        print("Select which file you would like to generate from template:")
        return DisplayFileSelection(template_files)
    else:
        print(f"There are no template files available to select from")
        return None
    
def SelectDataFile(data_path):
    data_files = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    if len(data_files) != 0:
        print("Select which file you would like to populate your template with:")
        return DisplayFileSelection(data_files)
    else:
        print(f"There are no excel files available to select from")
        return None

def DisplayFileSelection(file_names):
    index = 1
    for file_name in file_names:
        print("\t{index}. {file_name}".format(index=index, file_name=file_name))
        index += 1

    valid_input = False
    while not valid_input:
        user_input = input("Select a file from below: ")
        try:
            index = int(user_input)
            selected_file = file_names[index - 1]
            valid_input = True
        except Exception:
            print(f"The selection you made was invalid. Please try again.")
    return selected_file