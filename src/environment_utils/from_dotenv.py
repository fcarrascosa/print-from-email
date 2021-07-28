from os import path, getcwd
from dotenv import dotenv_values


def from_dotenv():
    return dotenv_values(path.join(getcwd(), '..', 'config', 'config.env'))
