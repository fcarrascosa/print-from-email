from os import getenv


def from_host(keys):
    config = {};
    for key in keys:
        if getenv(key):
            config[key] = getenv(key)
    return config
