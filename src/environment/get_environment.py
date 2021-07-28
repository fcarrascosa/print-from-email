from . import from_host, from_dotenv


def get_environment(keys):
    config = from_dotenv()
    config.update(from_host(keys))
    return config
