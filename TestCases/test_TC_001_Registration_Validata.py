import pytest

from DataGenerate import DataGen
from Base import InitiateDriver
from Pages import RegistrationPage


@pytest.mark.parametrize('data', DataGen.data_generator())
def test_Validate_Registration(data):
    driver = InitiateDriver.start_browser()

    register = RegistrationPage.registration_class(driver)
    register.enter_username(data[0])
    register.enter_email(data[1])
    register.enter_password(data[2])
    register.repeat_enter_password(data[3])
    register.enter_address(data[4])

    InitiateDriver.close_browser()
    # driver.close()
