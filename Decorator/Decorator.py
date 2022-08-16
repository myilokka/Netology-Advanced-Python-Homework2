import logging
import os

path = os.getenv('path_to_logs')
if path is None:
    path = 'logs.log'


def path_logger(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            logging.basicConfig(filename=path, level=logging.INFO, format='%(asctime)s %(message)s')
            logging.info(f'Функция {old_function.__name__} вызвана с аргументами: {args}, {kwargs}.')
            result = old_function(*args, **kwargs)
            logging.info(f'Результат работы функции {old_function.__name__} - {result}.')
            return result
        return new_function
    return logger
