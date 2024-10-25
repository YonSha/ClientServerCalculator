import inspect
import logging
import time


class Logger:

    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s : %(levelname)-3s : %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

        self.change_log_level()

    def change_log_level(self, level=logging.INFO):
        logging.getLogger().setLevel(level)

    def logging_error(self, value):
        logging.info(f'---- {value} ----')

    def logging_info(self, value):
        logging.info(f'---- {value} ----')

    def logging_debug(self, value):
        logging.info(f'---- {value} ----')

    def info_enter_function(self):
        logging.info(f'---- {"Function " + inspect.stack()[1][3] + " Enter"} ----')
        time.sleep(1)

    def info_exit_function(self):
        logging.info(f'---- {"Function " + inspect.stack()[1][3] + " Exit"} ----')


def enter_exit_wrapper(func):
    def inner(*args, **kwargs):
        logging.info(f'---- {"Function " + func.__name__ + " Enter"} ----')
        result = func(*args, **kwargs)
        logging.info(f'---- {"Function " + func.__name__ + " Exit"} ----')
        return result

    return inner
