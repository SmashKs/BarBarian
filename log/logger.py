import logging
from datetime import datetime
from os import path

from log import LOGGER_FORMAT, LOGGER_TIME_FORMAT


class Logger:
    @staticmethod
    def new_file_setting(file_path):  # type: (str) -> None
        file_handler = logging.FileHandler(file_path, 'a')
        formatter = logging.Formatter(fmt=LOGGER_FORMAT,
                                      datefmt=LOGGER_TIME_FORMAT)
        file_handler.setFormatter(formatter)

        log = logging.getLogger()  # Root logger.
        for handler in log.handlers[:]:  # Remove all old handlers.
            log.removeHandler(handler)
        log.addHandler(file_handler)  # Set the new handler

    @staticmethod
    def basic_setting():
        file_path = Logger.create_log_file(Logger.get_today())

        logging.basicConfig(level=logging.DEBUG,
                            format=LOGGER_FORMAT,
                            datefmt=LOGGER_TIME_FORMAT,
                            filename=file_path,
                            filemode='a')

    @staticmethod
    def create_log_file(today):  # type: (str) -> str
        file_path = f'log/daily/{today}.log'
        if not path.exists(file_path):
            with open(file_path, 'x'):
                pass
            Logger.new_file_setting(file_path)

        return file_path

    @staticmethod
    def get_today_with_time():  # type: () -> str
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_today():  # type: () -> str
        return datetime.now().strftime('%Y-%m-%d')
