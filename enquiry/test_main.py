from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from xpaths import Xpaths
import pytest

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)
driver.maximize_window()


def find_element(val, elem=None, by=By.CLASS_NAME) -> WebElement:
    if elem is None:
        elem = driver
    element = WebDriverWait(elem, 10).until(EC.element_to_be_clickable((by, val)))
    return element


# driver.get("https://swingers-crm-qa.azurewebsites.net/Inquiries/Dashboard")
driver.get("https://swingers-crm-qa.azurewebsites.net/Inquiries/Edit/fcd93fef-9080-4333-198a-08da371e142c")
sleep(2)


def test_enquiry_requirements():
    third_party = find_element("react-select-dropdown__control")
    third_party.click()
    third_party = find_element("react-select-2-option-5", by=By.ID)
    third_party.click()

    venue_dropdown = find_element(Xpaths.enquiry_venue_dropdown, by=By.XPATH)
    venue_dropdown.click()

    venue = find_element(Xpaths.aruba_city, by=By.XPATH)
    venue.click()

    save = find_element(Xpaths.enquiry_requirements_save, by=By.XPATH)
    save.click()

    # do this for new ones

    # try:
    #     assign_to_me = find_element("//*[contains(text(), 'Assign to Me')]", by=By.XPATH)
    #     assign_to_me.click()
    # except:
    #     pass


def test_enquiry_space():
    space = find_element(Xpaths.enquiry_space, by=By.XPATH)
    driver.execute_script("arguments[0].click();", space)

    sleep(2)
    calendar = find_element("transparent-navigator-toggler")
    driver.execute_script("arguments[0].click();", calendar)

    calendar = find_element("date-navigator.navigator_default_month")
    days = driver.find_elements(by=By.CLASS_NAME,
                                value="date-navigator.navigator_default_day.date-navigator.navigator_default_cell")
    sleep(2)
    days[30].click()

    accept_place = find_element(Xpaths.space_accept_save, by=By.XPATH)
    accept_place.click()

    save_space = find_element(Xpaths.space_save, by=By.XPATH)
    save_space.click()
    # day = find_element("//*[contains(text(), '25')]", by=By.XPATH)
    # day.click()
    # box1 = find_element('//*[@id="root"]/div/div/div[2]/main/section/div[2]/div/div[2]/div[3]/div[3]/div[3]/div/div[2]/div[1]', by=By.XPATH)
    # box2 = find_element('//*[@id="root"]/div/div/div[2]/main/section/div[2]/div/div[2]/div[3]/div[3]/div[3]/div/div[2]/div[2]', by=By.XPATH)
    # # box2.click()
    # driver.execute_script("arguments[0].click();", box2)
    # actions2 = ActionChains(driver)
    # actions2.drag_and_drop(source=box1, target=box2)
    # matrix = find_element("scheduler_default_matrix")
    # boxes = matrix.find_elements(by=By.CLASS_NAME, value="scheduler_default_cell.scheduler_default_cellparent.group-sale-teeoff-color")
    # boxes[0].click()

    # slider = driver.find_element_by_css_selector("#o1Slider > div.slider-handle.min-slider-handle.round")
    # sleep(5)
    # move = ActionChains(driver)
    # move.click_and_hold(box1).move_by_offset(1000, 0).release().perform()
    # for i in boxes:
    #     print(i, i.text)
    #     print()
    # print(boxes)
