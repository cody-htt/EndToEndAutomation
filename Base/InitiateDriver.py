from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader


def start_browser():
    # noinspection PyGlobalUndefined
    global driver

    if ConfigReader.read_config_data('Details', 'Browser') == "Chrome":
        driver_path = "./Browserdriver/chromedriver.exe"  # ./Browserdriver/chromedriver.exe
        driver = Chrome(executable_path=driver_path)
    elif ConfigReader.read_config_data('Details', 'Browser') == "Firefox":
        driver_path = "./Browserdriver/geckodriver.exe"  # ./Browserdriver/geckodriver.exe
        driver = Firefox(executable_path=driver_path)
    else:
        driver_path = "./Browserdriver/chromedriver.exe"
        driver = Chrome(executable_path=driver_path)

    driver.maximize_window()
    driver.get(ConfigReader.read_config_data('Details', 'Application_URL'))
    return driver


def close_browser():
    driver.close()
