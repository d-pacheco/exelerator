import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from colorama import Fore, Style

FILE_SIZE = 1024 * 1024 * 100  # 100 MB
BACKUP_COUNT = 5  # keep up to 5 files


class ColoredFormatter(logging.Formatter):
    # Define colors for different log levels
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA
    }

    def format(self, record):
        # Get the original message
        log_msg = super().format(record)

        # Apply the color based on the log level
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        log_msg = color + log_msg + Style.RESET_ALL

        return log_msg


def configure_logger(debug: bool):
    Path("./logs/").mkdir(parents=True, exist_ok=True)
    if debug:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO

    exelerator_logger = logging.getLogger("exelerator")
    exelerator_logger.setLevel(logging_level)
    logging_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

    # File Handler
    file_handler = RotatingFileHandler(
        filename="./logs/pdf_populater.log",
        mode="a+",
        maxBytes=FILE_SIZE,
        backupCount=BACKUP_COUNT,
        encoding='utf-8'
    )
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(logging_formatter)
    exelerator_logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(ColoredFormatter())
    exelerator_logger.addHandler(console_handler)
