from Base import InitiateDriver
from Library import ConfigReader
from ConfigurationFiles import Elements


def test_Invalid_data_Registration():
    driver = InitiateDriver.start_browser()

    driver.find_element_by_xpath(Elements.elements.username).send_keys("Hello World 2")
    driver.find_element_by_xpath(Elements.elements.mail).send_keys("TungHuynh2@gmail.com")
    driver.find_element_by_xpath(Elements.elements.password).send_keys("12345622222")
    driver.find_element_by_css_selector(Elements.elements.phone_number).send_keys("1234567988")
    driver.find_element_by_css_selector(Elements.elements.address).send_keys("123 ABC")

    InitiateDriver.close_browser()
