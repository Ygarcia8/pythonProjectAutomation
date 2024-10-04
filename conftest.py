import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import PAYMENT_GATEWAY_URL, BANK_PROJECT_URL




@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_valid_login(setup):
    setup.get("TEST_SITE_URL")
    setup.find_element(By.NAME, 'uid').send_keys("1303")
    setup.find_element(By.NAME, 'password').send_keys("Guru99")
    setup.find_element(By.NAME, 'btnLogin').click()
    assert "Welcome" in setup.page_source

# Fixture for Payment Gateway Project
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(PAYMENT_GATEWAY_URL)
    request.cls.driver = driver
    yield
    driver.quit()

# Fixture for Bankproject
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(BANK_PROJECT_URL)
    request.cls.driver = driver
    yield
    driver.quit()
