from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import time
from constants import  PAYMENT_GATEWAY_URL



class TestPaymentGateway:
    def setup_method(self):
        # WebDriver setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(PAYMENT_GATEWAY_URL)

    def teardown_method(self):
        self.driver.quit()
        time.sleep(3)
    def test_select_item_and_buy(self):
        select_element = Select(self.driver.find_element(By.NAME, 'quantity'))
        time.sleep(3)
        # Select option by visible text or by index.
        select_element.select_by_index(3)  # selects second item

        # Click the Buy button
        self.driver.find_element(By.XPATH, "//*[@id='three']/div/form/div/div[8]/ul/li/input").click()
        time.sleep(3)

        assert "Payment Process" in self.driver.page_source
        time.sleep(3)

    def test_fill_credit_card(self):
        # Select an item and go to the payment process page
        self.test_select_item_and_buy()

        # Fill in fake credit card details
        self.driver.find_element(By.NAME, 'card_nmuber').send_keys("1234567812345678")
        self.driver.find_element(By.NAME, 'cvv_code').send_keys("123")

        # Select expiration month
        select_month = Select(self.driver.find_element(By.NAME, 'month'))
        select_month.select_by_visible_text("12")  # December

        # Select expiration year
        select_year = Select(self.driver.find_element(By.NAME, 'year'))
        select_year.select_by_visible_text("2025")
        time.sleep(3)

        # Click 'Pay' button
        self.driver.find_element(By.NAME, 'submit').click()

        # Assert a success message or error message
        assert "Payment success" in self.driver.page_source or "Transaction failed" in self.driver.page_source
        time.sleep(5)


