import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.exception_tc01
def test_find_row_2(driver):
    # Open Web page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    # Click Add button
    add_button = driver.find_element(By.ID, "add_btn")
    add_button.click()
    # Verify Row 2 is displayed
    second_row = (WebDriverWait(driver, 10).
                  until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input[@class='input-field']"))))
    assert second_row.is_displayed()
