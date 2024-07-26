import pytest
from selenium.webdriver.common.by import By


@pytest.mark.exception_tc01
def test_find_row_2(driver):
    # Open Web page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    # Click Add button
    add_button = driver.find_element(By.ID, "add_btn")
    add_button.click()
    # Verify Row 2 is displayed
    second_row = driver.find_element(By.XPATH, value="//div[@id='row2']/input[@class='input-field']")
    assert second_row.is_displayed(), "Error. Row two is not displayed on the web page"
