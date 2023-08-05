import time
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


#firefox
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()

#chrome
# Define a fixture that sets up the driver and manages cookies
@pytest.fixture(scope="module")
def driver_setup():
    # setup
    driver = webdriver.Chrome()
    driver.get('https://sound.orf.at/')

    #the cookie check implemented here to click the buton whenever it pops up...???maybe
    # try:
    #     # If there's a cookie popup, find the 'Alle Cookies akzeptieren' button and click it
    #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#didomi-notice-learn-more-button"))).click()
    #
    # except:
    #     print("No cookie popup found")

    yield driver  # provide the fixture value
    # teardown
    driver.quit()

def test_basic_search(driver):
    driver.get("https://sound.orf.at/")
    expectation = EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
    cookies_button = WebDriverWait(driver, 10).until(expectation)
    cookies_button.click()

    expectation = EC.presence_of_element_located((By.CSS_SELECTOR,".open-search-button"))
    search_button = WebDriverWait(driver, 10).until(expectation)
    search_button.click()

    expectation = EC.presence_of_element_located((By.CSS_SELECTOR,".text-input > input:nth-child(2)"))
    search_field = WebDriverWait(driver, 10).until(expectation)
    search_field.send_keys("Mozart")

    expectation = EC.presence_of_element_located((By.CSS_SELECTOR,".search-results-list"))
    unordered_list = WebDriverWait(driver, 10).until(expectation)
    result_list = unordered_list.find_elements(By.TAG_NAME,"li")
    headline = result_list[0].find_element(By.CSS_SELECTOR,".headline").text
    subtitle = result_list[0].find_element(By.CSS_SELECTOR,".subtitle").text
    assert "Mozart" in headline or "Mozart" in subtitle



def test_number_of_radiosenders(driver):
    expectation = EC.presence_of_element_located((By.CSS_SELECTOR,".search-results-list"))
    unordered_list = WebDriverWait(driver, 10).until(expectation)
    result_list = unordered_list.find_elements(By.TAG_NAME,"li")
    test = result_list[0].find_element(By.CSS_SELECTOR, ".search-results-list span")#.search-results-list span. This will select all span elements within elements with the class .search-results-list.
    #or like below, we can step through every element:
    #test = result_list[0].find_element(By.CSS_SELECTOR, ".search-results-list > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
    print('\nTest Details:')
    print(f"Session ID : {test.parent.session_id}")
    print(f"Element : {test.id}")

    radiostations = {}
    for li_element in result_list:
        #radiostation_district = li_element.find_element(By.CSS_SELECTOR, "#uniqueID").text
        radiostation_district = li_element.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
        if radiostation_district in radiostations.keys():
            radiostations[radiostation_district] += 1
        else:
            radiostations[radiostation_district] = 1
    print("\nRadiostations:")
    print(radiostations)

    assert len(radiostations.keys()) >= 2

