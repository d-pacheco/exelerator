import sys
import time

from colorama import init, Fore, Style
import logging
from exelerator.util.path_helper import PathHelper
from exelerator.version_manager import VersionManager
from exelerator.menu_selector import MenuSelector, MainMenuOptions, clear_screen
from exelerator.exceptions.exelerator_exception import ExeleratorException
from exelerator.exelerator import Exelerator
from exelerator.util.logger import configure_logger
from exelerator.util.config import Config

DEBUG_MODE = False
if DEBUG_MODE:
    print("RUNNING IN DEBUG MODE")

CURRENT_VERSION = 1.9

init()  # Initialize colorama
configure_logger(DEBUG_MODE)
logger = logging.getLogger("exelerator")

if '--upgraded' in sys.argv:
    VersionManager.delete_old_executable_versions()


def print_startup_messages():
    print(Fore.CYAN + "#############################################")
    print(Fore.CYAN + "#                                           #")
    print(Fore.CYAN + "#           Welcome to Exelerator           #")
    print(Fore.CYAN + f"#                   v{CURRENT_VERSION}                    #")
    print(Fore.CYAN + "#                                           #")
    print(Fore.CYAN + "#############################################")

    if VersionManager.has_internet() and not VersionManager.is_latest_version(CURRENT_VERSION):
        print(Fore.RED + "!!! New version is available !!!")
        # print(Fore.RED + "Download it from: https://github.com/d-pacheco/exelerator/releases/latest")
        user_input = input(Fore.RED + "Would you like to download this new release (y/n)?: ")
        if user_input.lower() == "y":
            VersionManager.download_latest_release()
    print(Style.RESET_ALL)


def main():
    print_startup_messages()
    config = Config()
    path_helper = PathHelper(DEBUG_MODE)
    pdf_populater = Exelerator(path_helper, config)

    try:
        wb_wrapper = pdf_populater.load_workbook()

        exit_program = False
        while not exit_program:
            main_menu_selection = MenuSelector.display_option_menu()
            if main_menu_selection == MainMenuOptions.POPULATE_PDF:
                pdf_populater.populate_pdf(wb_wrapper)
            elif main_menu_selection == MainMenuOptions.RELOAD:
                wb_wrapper = pdf_populater.load_workbook()
            elif main_menu_selection == MainMenuOptions.EXIT:
                exit_program = True

    except Exception as pdf_populater_exception:
        raise pdf_populater_exception


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Exiting...")
        clear_screen()
    except ExeleratorException as e:
        logger.error(f"An error has occurred: {e}")
        time.sleep(1)
        input("Press Enter to exit...")
        clear_screen()
