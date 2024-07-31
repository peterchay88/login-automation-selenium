from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_web_page(self):
        self.driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        wait = WebDriverWait(self.driver, 10)
        # Type username student into username field
        wait.until(EC.visibility_of_element_located(self.__username_field))
        self.driver.find_element(self.__username_field). send_keys(username)
        # Type password Password123 into password field
        wait.until(EC.visibility_of_element_located(self.__password_field))
        self.driver.find_element(self.__password_field).send_keys(password)
        # Push submit button
        wait.until(EC.visibility_of_element_located(self.__submit_button))
        self.driver.find_element(self.__submit_button).click()
