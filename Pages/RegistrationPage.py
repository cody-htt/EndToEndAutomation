from ConfigurationFiles import Elements


# noinspection PyGlobalUndefined
class registration_class:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element_by_xpath(Elements.elements.username).send_keys(username)

    def enter_email(self, email):
        driver.find_element_by_xpath(Elements.elements.mail).send_keys(email)

    def enter_password(self, password):
        driver.find_element_by_xpath(Elements.elements.password).send_keys(password)

    def repeat_enter_password(self, password):
        driver.find_element_by_css_selector(Elements.elements.phone_number).send_keys(password)

    def enter_address(self, address):
        driver.find_element_by_css_selector(Elements.elements.address).send_keys(address)

#     driver.find_element_by_xpath(ConfigReader.fetch_element_locators('Registration', 'username')).send_keys(
#         "Hello World")
#     driver.find_element_by_xpath(ConfigReader.fetch_element_locators('Registration', 'mail')).send_keys(
#         "oh@gmail.com")
#     driver.find_element_by_xpath(ConfigReader.fetch_element_locators('Registration', 'password')).send_keys(
#         "123456")
#     driver.find_element_by_xpath(ConfigReader.fetch_element_locators('Registration', 'repeat_password')).send_keys(
#         "1234")
#     driver.find_element_by_css_selector(
#         ConfigReader.fetch_element_locators('Registration', 'phone_number')).send_keys("123")
#     driver.find_element_by_css_selector(ConfigReader.fetch_element_locators('Registration', 'address')).send_keys(
#         "123 A")
#
