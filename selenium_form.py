# Automate test cases for page https://the-internet.herokuapp.com/login
from selenium import webdriver
running_program = 1


# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
def valid_login():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element_by_id('username').send_keys('tomsmith')
    browser.find_element_by_id('password').send_keys('SuperSecretPassword!')
    browser.find_element_by_css_selector('.fa').click()
    assert 'Secure Area' in browser.page_source
    browser.quit()


# 2. Login with invalid creds and check validation error
def invalid_login():
    browser = webdriver.Chrome()
    browser.get('https://the-internet.herokuapp.com/login')
    browser.find_element_by_id('username').send_keys('SOMEBODY')
    browser.find_element_by_id('password').send_keys('SuperSecretPassword')
    browser.find_element_by_css_selector('.fa').click()
    assert 'Your username is invalid' in browser.page_source
    browser.quit()


# 3. Logout from app and assert you successfully logged out
def logout():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element_by_id('username').send_keys('SOMEBODY')
    browser.find_element_by_id('password').send_keys('SuperSecretPassword')
    browser.find_element_by_css_selector('.fa').click()
    browser.find_element_by_css_selector('#content > div > a > i').click()
    assert 'You logged out of the secure area' in browser.page_source
    browser.quit()


if running_program == 1:
    valid_login()
    invalid_login()
    logout()
    if SystemExit.code != 0:
        print('All 3 test cases SUCCESSFULLY passed.')
    else:
        print('There was an error occured.')
