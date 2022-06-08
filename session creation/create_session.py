from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest
import json


class TestSession:
    driver = webdriver.Chrome()
    env_url = "https://swingers-crm-qa.azurewebsites.net"
    email = "admin@swingerstest.onmicrosoft.com"
    password = "Swingers123!@!"
    venue_id = "c18056ff-7aa6-4830-89a0-467189b17cde"

    @staticmethod
    def find_element(val, elem=None, by=By.CLASS_NAME) -> WebElement:
        if elem is None:
            elem = TestSession.driver
        element = WebDriverWait(elem, 10).until(EC.element_to_be_clickable((by, val)))
        return element

    @staticmethod
    def scroll_into(element):
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (TestSession.driver.execute_script(
            'return window.innerHeight') / 2) + TestSession.driver.execute_script('return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        TestSession.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    @staticmethod
    def click(element):
        TestSession.driver.execute_script("arguments[0].click();", element)

    def test_login(self):
        TestSession.driver.get(TestSession.env_url)
        TestSession.driver.maximize_window()

        login = self.find_element("btn-login")
        login.click()
        sleep(3)
        TestSession.driver.switch_to.window(TestSession.driver.window_handles[1])

        email = self.find_element("i0116", TestSession.driver, by=By.ID)
        email.send_keys(TestSession.email)

        self.find_element("idSIButton9", TestSession.driver, by=By.ID).click()

        password = self.find_element("i0118", TestSession.driver, by=By.ID)
        password.send_keys(TestSession.password)
        self.find_element("idSIButton9", TestSession.driver, by=By.ID).click()

        self.find_element("idSIButton9", TestSession.driver, by=By.ID).click()
        TestSession.driver.switch_to.window(TestSession.driver.window_handles[0])
        sleep(2)

    def test_add_Session(self):
        TestSession.driver.get(f"{TestSession.env_url}/Venues-Management/Venues/{TestSession.venue_id}/Venue-Sessions")

        sleep(4)
        new_config = self.find_element("btn-add-new")
        new_config.click()

        session_type = self.find_element("btn-add-hexagon")
        session_type.click()

        number_of_tee = self.find_element("numberOfTeeOffsPerSession", TestSession.driver, By.NAME)
        number_of_tee.send_keys(12)

        save = self.find_element("btn-dark-blue.btn-save")
        save.click()

        submit = self.find_element("btn-gold")
        submit.click()

        sleep(2)

        for i in range(7):
            self.weekdays_fill()

    def apply_times(self, period):
        boxes = period.find_elements(by=By.CLASS_NAME, value="form-check-label")
        self.find_element("form-check-label", period)

        self.click(boxes[0])
        self.click(boxes[2])

        apply = self.find_element("btn-dark-blue", period, by=By.CLASS_NAME)

        apply.click()

    def apply_days(self):
        periods = self.driver.find_elements(by=By.CLASS_NAME, value="session-period-setup")
        for p in periods:
            self.apply_times(p)
        # self.find_element("btn-dark-blue.btn-save.mr-0").click()

    def weekdays_fill(self):
        weekdays = self.driver.find_element(by=By.CLASS_NAME, value="list-weekdays.sticky")
        unapplied = self.find_element("unapplied", weekdays)
        weekday = self.find_element("weekday", unapplied)

        self.scroll_into(weekday)

        ActionChains(self.driver).move_to_element(unapplied).click(weekday).perform()

        self.apply_days()
