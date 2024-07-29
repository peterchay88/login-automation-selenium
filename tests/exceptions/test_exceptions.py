import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.exception_tc01
def test_no_such_element_exception(driver):
    # Open Web page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    # Click Add button
    add_button = driver.find_element(By.ID, "add_btn")
    add_button.click()
    # Verify Row 2 is displayed
    second_row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input[@class='input-field']"))
    )
    assert second_row.is_displayed(), "Error. Row two is not displayed on the web page"


@pytest.mark.exception_tc02
def test_element_not_interactable_exception(driver):
    # Open web page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    # Click add button
    add_button = driver.find_element(By.ID, "add_btn")
    add_button.click()
    # Wait for the second row to load
    second_row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input[@class='input-field']")))
    # Type text into the second input field
    second_row.send_keys("This is a test")
    # Click the save button by using By.name(“Save”)
    save_button = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
    save_button.click()
    # Verify Text is saved
    confirmation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "confirmation"))
    )
    assert confirmation.text == "Row 2 was saved"


@pytest.mark.exception_tc03
def test_invalid_element_state(driver):
    # Open webpage
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    # Clear input field
    edit_btn = driver.find_element(By.ID, "edit_btn")
    edit_btn.click()

    input_field = driver.find_element(By.XPATH, "//div[@id='row1']/input[@class='input-field']")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(input_field))
    input_field.clear()
    # Type text into the input field
    new_text = "this is a test"
    input_field.send_keys(new_text)

    save_btn = driver.find_element(By.ID, "save_btn")
    save_btn.click()
    # verify text changed
    assert input_field.get_attribute("value") == new_text, \
        f"Error unexpected value. Expected {new_text}. Actual {input_field.get_attribute('value')}"


@pytest.mark.exception_tc04
def test_stale_element_reference(driver):
    # Open page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    # Push add button
    add_btn = driver.find_element(By.ID, "add_btn")
    add_btn.click()

    # Verify instruction text element is no longer displayed
    wait = WebDriverWait(driver, 10)
    assert wait.until(EC.invisibility_of_element_located((By.ID, "instructions")),
                      "Error! instructions element still located on the page")
