from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import time
import driver
from selenium.webdriver.support.wait import WebDriverWait

from constants import BANK_PROJECT_URL


@pytest.mark.usefixtures("setup")
class TestForgotPassword:

    @pytest.fixture(autouse=True)
    def teardown(self):
        yield  # This will run the test
        self.driver.delete_all_cookies()  # Clear cookies after each test
        self.driver.get(BANK_PROJECT_URL)  # Reset the page for next test

    def test_forgot_password(self):
        try:
            here_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'here')]")))
            here_link.click()
            time.sleep(3)
            email_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "emailid")))
            email_field.send_keys("Yasno@gmail.com")

            submit_button = self.driver.find_element(By.NAME, "btnLogin")
            submit_button.click()

        except TimeoutException as e:
            print(f"Element not found: {str(e)}")
            assert False, "Test failed due to TimeoutException"

    def test_forgot_password_invalid_email(self):
        try:
            here_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'here')]")))
            here_link.click()
            time.sleep(3)
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "emailid")))
            email_field.send_keys("invalid_email_format")
            time.sleep(3)
            submit_button = self.driver.find_element(By.NAME, "btnLogin")
            submit_button.click()

            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='message9']"))).text
            time.sleep(3)
            assert "Email ID is not valid" in error_message

        except TimeoutException as e:
            print(f"Element not found: {str(e)}")
            assert False, "Test failed due to TimeoutException"
