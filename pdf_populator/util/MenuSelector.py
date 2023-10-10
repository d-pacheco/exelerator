import os
from os import listdir
from os.path import isfile, join
from .MenuOptions import MainMenuOptions

class MenuSelector:

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def GetMainMenuSelection(self):
        return self.DisplayOptionMenu(MainMenuOptions.options)

    def SelectTemplateFile(self, template_files):
        print("Select which file you would like to generate from template:")
        return DisplayFileSelection(template_files)
        
    def SelectDataFile(self, excel_files):
        print("Select which file you would like to populate your template with:")
        return DisplayFileSelection(excel_files)
    
    def DisplayOptionMenu(self, options):
        valid_input = False
        while not valid_input:
            self.clear_screen()
            for i in range(len(options)):
                print(f"{i+1}. {options[i][0]}")
            user_input = input("Select an option: ")
            try:
                index = int(user_input)
                if index < 1 or index > len(options):
                    continue
                return options[index - 1][1]
            except:
                pass

def DisplayFileSelection(file_names):
    index = 1
    for file_name in file_names:
        print("\t{index}. {file_name}".format(index=index, file_name=file_name))
        index += 1

    valid_input = False
    while not valid_input:
        user_input = input("Select a file from above: ")
        try:
            index = int(user_input)
            selected_file = file_names[index - 1]
            valid_input = True
        except Exception:
            print(f"The selection you made was invalid. Please try again.")
    return selected_file
