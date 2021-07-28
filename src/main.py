from environment import get_environment
from config import verify_config

REQUIRED_DATA = [
    'ORG_EMAIL',
    'USER_NAME',
    'PASSWORD',
    'SERVER_URI',
    'SERVER_PORT',
    'PREFIX_TO_PRINT',
    'PRINTER_NAME'
]

CONFIG = get_environment(REQUIRED_DATA)

verify_config(REQUIRED_DATA, CONFIG)
