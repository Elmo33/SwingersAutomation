from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest
import json


class TestBooking:
    driver = webdriver.Chrome()
    env_url = "https://swingers-cms-uat.azurewebsites.net/us/locations/nyc/book-now"
    day = 'July 27, 2022'
    months_after = 1  # how many months later is the day that you are booking
    time = '6:30pm - 8:00pm'
    guests = 10
    package_number = 2

    def click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def find_element(self, val, elem=None, by=By.CLASS_NAME) -> WebElement:
        if elem is None:
            elem = self.driver
        element = WebDriverWait(elem, 10).until(EC.element_to_be_clickable((by, val)))
        self.scroll_into(element)
        return element

    def scroll_into(self, element):
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (self.driver.execute_script(
            'return window.innerHeight') / 2) + self.driver.execute_script('return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def test_initialize(self):
        self.driver.maximize_window()
        self.driver.get(TestBooking.env_url)

        cookie_window = self.find_element("cookies-action-btns")
        accept_cookies = self.find_element("btn.btn-gold", cookie_window)
        self.click(accept_cookies)

    def test_booking(self):
        def next_month(months):
            for i in range(months):
                sleep(2)
                arrow = self.find_element("react-calendar__navigation__arrow.react-calendar__navigation__next-button")
                arrow.click()

        def increment_people(people):
            for i in range(people):
                plus = self.find_element("btn-increment")
                self.click(plus)

        next_month(self.months_after)
        increment_people(self.guests - 1)

        calendar = self.find_element("react-calendar__month-view__days")
        booking_day = self.find_element(f"//*[@aria-label='{self.day}']", calendar, by=By.XPATH)

        sleep(2)
        booking_day.click()

        nomad = self.find_element("venue-time-slot")

        hours = self.find_element(f"//*[contains(text(), '{self.time}')]", nomad, by=By.XPATH)
        hours.click()

    def test_packages(self):
        self.find_element("col-1of5")  # don't ask why this is here
        packages = self.driver.find_elements(by=By.CLASS_NAME, value="col-1of5")

        add_to_cart = self.find_element("btn.btn-gold-transparent", packages[self.package_number])
        add_to_cart.click()

    def test_review_chart(self):
        custom_tip = self.find_element("custom-tip")
        custom_tip = self.find_element("input", custom_tip, by=By.TAG_NAME)
        custom_tip.send_keys("5")

        summary = self.find_element("summary")
        checkout = self.find_element("btn.btn-dark-blue", summary)
        checkout.click()

    def test_your_details(self):
        xpath = '//*[@id="root"]/div/div/div/div/div/div[2]/section/div/form'

        self.find_element(f'{xpath}/div[1]/div/input', by=By.XPATH).send_keys("email@gmail.com")  # email

        self.find_element(f'{xpath}/div[2]/div[1]/div/input', by=By.XPATH).send_keys("John")  # first name
        self.find_element(f'{xpath}/div[2]/div[2]/div/input', by=By.XPATH).send_keys("Lennon")  # last name
        self.find_element(f'{xpath}/div[2]/div[3]/div/input', by=By.XPATH).send_keys("5555555555")  # phone num
        self.find_element(f'{xpath}/div[2]/div[4]/div/input', by=By.XPATH).send_keys("06")  # mm
        self.find_element(f'{xpath}/div[2]/div[4]/div/input[2]', by=By.XPATH).send_keys("05")  # dd
        self.find_element(f'{xpath}/div[2]/div[4]/div/input[3]', by=By.XPATH).send_keys("2001")  # YYYY
        self.find_element(f'{xpath}/div[2]/div[5]/div/input', by=By.XPATH).send_keys("address")  # address
        self.find_element(f'{xpath}/div[2]/div[6]/div/input', by=By.XPATH).send_keys("street")  # street
        self.find_element(f'{xpath}/div[2]/div[7]/div/input', by=By.XPATH).send_keys("adress 2")  # adress 2
        self.find_element(f'{xpath}/div[2]/div[8]/div/input', by=By.XPATH).send_keys("1234")  # zip
        self.find_element(f'{xpath}/div[2]/div[9]/div/input', by=By.XPATH).send_keys("city")  # city
        self.find_element(f'{xpath}/div[2]/div[10]/div/input', by=By.XPATH).send_keys("state")  # state
        self.find_element(f'{xpath}/div[2]/div[11]/div/label/span', by=By.XPATH).click()

        submit = self.find_element("btn.btn-dark-blue")
        submit.click()

        non_refund = self.find_element("non-refund")
        agree = self.find_element("checkmark", non_refund)
        agree.click()

        adult = self.find_element("adulthood")
        agree = self.find_element("checkmark", adult)
        agree.click()

        terms = self.find_element("accept-terms")
        agree = self.find_element("checkmark", terms)
        agree.click()

        submit = self.find_element("btn.btn-dark-blue")
        submit.click()

    def test_payment(self):
        iframe = self.find_element('//*[@id="payment-element"]/div/iframe', by=By.XPATH)
        self.driver.switch_to.frame(iframe)

        card_number = self.find_element('number', by=By.NAME)
        card_number.send_keys('4242424242424242')

        expiration = self.find_element('Field-expiryInput', by=By.ID)
        expiration.send_keys('0523')

        cvc = self.find_element('Field-cvcInput', by=By.ID)
        cvc.send_keys('666')

        self.driver.switch_to.default_content()

        client_details = self.find_element("form-client-details")
        pay = self.find_element("btn.btn-gold", client_details)
        pay.click()
