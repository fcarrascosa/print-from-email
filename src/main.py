from environment_utils import get_config

REQUIRED_DATA = [
    'ORG_EMAIL',
    'USER_NAME',
    'PASSWORD',
    'SERVER_URI',
    'SERVER_PORT',
    'PREFIX_TO_PRINT',
    'PRINTER_NAME'
]

CONFIG = get_config(REQUIRED_DATA)
