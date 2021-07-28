def verify_config(required_data, config):
    is_valid = True
    for key in required_data:
        if config.get(key) in [None, '']:
            print(key + ' env config is missing.')
            is_valid = False
    return is_valid
