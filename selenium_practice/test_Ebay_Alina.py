from selenium.webdriver.common.by import By
import pytest


@pytest.mark.group1020
def test_example(browser):

    browser.get('http://www.ebay.com/')
    browser.find_element(By.ID, "gh-ac").send_keys("Lexus")
    browser.find_element(By.ID, "gh-btn").click()
    print("This is the current title: " + browser.title)
