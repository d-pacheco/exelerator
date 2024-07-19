import os


class MainMenuOptions:
    POPULATE_PDF = 0
    RELOAD = 1
    EXIT = 3
    options = [
        ("Populate PDF from a template", POPULATE_PDF),
        ("Reload excel files", RELOAD),
        ("Exit", EXIT)
    ]


class MenuSelector:
    @staticmethod
    def select_template_file(template_files):
        print("Select which file you would like to generate from template:")
        return display_file_selection(template_files)

    @staticmethod
    def select_data_file(excel_files):
        print("Select which file you would like to populate your template with:")
        return display_file_selection(excel_files)

    @staticmethod
    def display_option_menu():
        print("\nMenu Options")
        options = MainMenuOptions.options
        valid_input = False
        while not valid_input:
            for i in range(len(options)):
                print(f"{i + 1}. {options[i][0]}")
            user_input = input("Select an option: ")
            try:
                index = int(user_input)
                if index < 1 or index > len(options):
                    continue
                return options[index - 1][1]
            except Exception as e:
                pass


def display_file_selection(file_names):
    index = 1
    for file_name in file_names:
        print("\t{index}. {file_name}".format(index=index, file_name=file_name))
        index += 1

    selected_file = ""
    valid_input = False
    while not valid_input:
        user_input = input("Select a file from above: ")
        try:
            index = int(user_input)
            selected_file = file_names[index - 1]
            valid_input = True
        except Exception:
            print(f"The selection you made was invalid. Please select a number next to the file name.")
    return selected_file


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
