# Automate test cases for page https://the-internet.herokuapp.com/login
from selenium import webdriver


def main():
    # 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element_by_id('username').send_keys('tomsmith')
    browser.find_element_by_id('password').send_keys('SuperSecretPassword!')
    browser.find_element_by_css_selector('.fa').click()
    assert 'Secure Area' in browser.page_source
    browser.quit()

    # 2. Login with invalid creds and check validation error
    browser = webdriver.Chrome()
    browser.get('https://the-internet.herokuapp.com/login')
    browser.find_element_by_id('username').send_keys('tomsmith')
    browser.find_element_by_id('password').send_keys('SuperSecretPassword')
    browser.find_element_by_css_selector('.fa').click()
    assert 'Your username is invalid' or 'Your password is invalid' in browser.page_source
    browser.quit()

    # 3. Logout from app and assert you successfully logged out
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element_by_id('username').send_keys('tomsmith')
    browser.find_element_by_id('password').send_keys('SuperSecretPassword!')
    browser.find_element_by_css_selector('.fa').click()
    browser.find_element_by_css_selector('#content > div > a > i').click()
    assert 'You logged out of the secure area' in browser.page_source
    browser.quit()


if __name__ == '__main__':
    main()
    if SystemExit.code != 0:
        print("All 3 Test Cases Successfully Passed.")
    else:
        print("There was an Error occurred.")