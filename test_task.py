import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture
def driver(request):
    email = "rockthismustaine@gmail.com"
    pwd = "Strongpwd13"
    browser = webdriver.Chrome('/Users/kostyafrolov/Downloads/chromedriver2') #set path to webdriver
    browser.get("https://stackoverflow.com")
    browser.find_element_by_css_selector('a.login-link.btn-clear').click()
    browser.find_element_by_css_selector('[name="email"]').send_keys(email)
    browser.find_element_by_css_selector('[name="password"]').send_keys(pwd)
    browser.find_element_by_css_selector('#submit-button').click()

    def resource_teardown():
        browser.quit()

    request.addfinalizer(resource_teardown)

    return browser

class Testset():

    def test_login(self,driver):
        sleep(2)
        assert len(driver.find_elements_by_css_selector('.my-profile.js-gps-track')) != 0
        self.login_page = driver.current_url
        return self.login_page

    def test_search_field(self,driver):
        sleep(3)
        driver.find_element_by_css_selector('.js-search-field').send_keys("python")
        driver.find_element_by_css_selector('.btn-topbar-primary.js-search-submit').click()
        question = driver.find_element_by_xpath('//*[@id="questions"]/div[1]/div[2]/h3/a')
        title = question.text
        question.click()
        question_header = driver.find_element_by_css_selector('.question-hyperlink').text
        assert str(title) == str(question_header)
        
# Second part
# For downloading 
# wget --mirror -p --convert-links -P ./Desktop www.walla.co.il 
