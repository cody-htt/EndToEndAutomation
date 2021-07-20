from configparser import ConfigParser


def read_config_data(section, key):
    config = ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")  # From project level should 1 '.', from internal level need 2 '.'
    if config.has_section(section):
        return config.get(section, key)
    else:
        return "No Section found"


def fetch_element_locators(section, key):
    config = ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")  # From project level should 1 '.', from internal level need 2 '.'
    if config.has_section(section):
        return config.get(section, key)
    else:
        return "No Section found"


# print(fetch_element_locators('Registration', 'mail'))
