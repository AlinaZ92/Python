from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.mark.parametrize("item",
                         [
                             "Lexus",
                             "Mazda",
                             "BMW"
                         ])
@pytest.mark.Main
def test_search(browser, item):
    browser.get('http://www.ebay.com/')
    browser.find_element(By.ID, "gh-ac").send_keys(item)
    browser.find_element(By.ID, "gh-btn").click()
    browser.find_element(By.XPATH, '//*[@id="srp-river-results"]/ul/li[4]/div/div[2]/a/div/span/span').click()
    WebDriverWait(browser, 10)
    assert item in browser.title


def test_find_vehicle(browser):
    browser.get('http://www.ebay.com/')
    browser.find_element(By.LINK_TEXT, "Motors").click()
    year_dropdown = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.NAME, "Year")))
    year = Select(year_dropdown).select_by_visible_text("2020")
    make_dropdown = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.NAME, "Make")))
    make = Select(make_dropdown).select_by_visible_text("Aston Martin")
    model_dropdown = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.NAME, "Model")))
    model = Select(model_dropdown).select_by_visible_text("DBS")
    trim_dropdown = WebDriverWait(browser, timeout=6).until(EC.element_to_be_clickable((By.NAME, "Trim")))
    trim = Select(trim_dropdown).select_by_visible_text("Superleggera Coupe 2-Door")
    engine_dropdown = WebDriverWait(browser, timeout=4).until(EC.element_to_be_clickable((By.NAME, "Engine")))
    engine = Select(engine_dropdown).select_by_value("5.2L 5204CC V12 GAS DOHC Turbocharged")
    browser.find_element(By.CLASS_NAME, "motors-finder__find-btn").click()
