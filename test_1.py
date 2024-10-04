from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import time
from constants import TEST_SITE_URL


class TestLogin:

    def setup_method(self):
        # WebDriver setup (adjust for your WebDriver)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(TEST_SITE_URL)

    def teardown_method(self):
        # Close browser after test
        self.driver.quit()

    def test_valid_login(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("1303")
        self.driver.find_element(By.NAME, 'password').send_keys("Guru99")
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(2)
        assert "Welcome" in self.driver.page_source

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("8945")
        self.driver.find_element(By.NAME, 'password').send_keys("559")
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(3)
        try:
            # Switch to the alert
            alert = self.driver.switch_to.alert

            # Get the text from the alert
            alert_text = alert.text

            # Assert that the alert text contains the expected message
            assert "User or Password is not valid" in alert_text

            # Accept the alert (close it)
            alert.accept()
        except TimeoutException:
            # Handle the case where no alert is present within the expected time
            assert False, "Expected alert did not appear."


        except NoAlertPresentException:
            # Handle the case where no alert is present (if necessary)
            assert False, "Alert not found when expected"

    def test_empty_credentials(self):
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(3)
        alert = self.driver.switch_to.alert

        # Get the text from the alert
        alert_text = alert.text

        # Verify the alert message
        assert "User or Password is not valid" in alert_text, f"Unexpected alert text: {alert_text}"

        # Accept the alert to close it
        alert.accept()
        time.sleep(3)
    def test_reset_button(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("1303")
        self.driver.find_element(By.NAME, 'password').send_keys("Guru99")
        self.driver.find_element(By.NAME, 'btnReset').click()
        # Assert that fields are cleared
        assert self.driver.find_element(By.NAME, 'uid').get_attribute('value') == ""
        assert self.driver.find_element(By.NAME, 'password').get_attribute('value') == ""
        time.sleep(3)

