from selenium import webdriver

TEST_DATA = {
    'single_input': 'My best message here!!',
    'two_input_first': 333,
    'two_input_second': 444
}


def main():
    browser = webdriver.Chrome()
    browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    browser.maximize_window()
    browser.implicitly_wait(5)

    if browser.find_element_by_id("at-cv-lightbox-close").size != 0:
        browser.find_element_by_id("at-cv-lightbox-close").click()

    browser.find_element_by_css_selector("input#user-message").send_keys(TEST_DATA['single_input'])
    browser.find_element_by_css_selector("form#get-input button").click()

    assert browser.find_element_by_id("display").text == TEST_DATA['single_input']

    browser.find_element_by_css_selector('#sum1').send_keys(TEST_DATA['two_input_first'])
    browser.find_element_by_css_selector('#sum2').send_keys(TEST_DATA['two_input_second'])
    browser.find_element_by_css_selector('#gettotal > button').click()

    assert browser.find_element_by_css_selector('#displayvalue').text == '777'

    browser.quit()


if __name__ == "__main__":
    main()
    if SystemExit.code != 0:
        print("Test passed")
