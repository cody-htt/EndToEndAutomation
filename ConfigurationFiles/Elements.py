class elements:
    username = '//*[@id="tab-content1"]/form/input[2]'
    mail = '//*[@id="tab-content1"]/form/input[3]'
    password = '//*[@id="tab-content1"]/form/input[4]'
    repeat_password = '//*[@id="tab-content1"]/form/input[5]'
    phone_number = 'input[type="text"][name="phone"]'
    address = 'div.tab-content input[name="address"]'


print(elements.username)
