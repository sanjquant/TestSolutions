from selenium import webdriver
from selenium.webdriver.common.by import By
from enum import Enum


class BaseUrl(Enum):

    BASE_URL = "https://login.yahoo.com/?.intl=uk"


class Identifiers(Enum):

    USERNAME_XPATH = "//*[@id='login-username']"
    PASSWORD_XPATH = "//*[@id='login-passwd']"
    NEXT_USERNAME_BUTTON_XPATH = "//*[@id='login-signin']"
    NEXT_PASSWORD_BUTTON_XPATH = "//*[@id='login-signin']"


class Login:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = BaseUrl.BASE_URL.value
        self.driver.implicitly_wait(5)

    def launch_browser(self):
        self.driver.get(self.base_url)

    def set_username(self, username):
        self.driver.find_element(By.XPATH, Identifiers.USERNAME_XPATH.value).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, Identifiers.PASSWORD_XPATH.value).send_keys(password)

    def click_on_next_button(self):
        self.driver.find_element(By.XPATH, Identifiers.NEXT_USERNAME_BUTTON_XPATH.value).click()

    def click_on_next_password_button(self):
        self.driver.find_element(By.XPATH, Identifiers.NEXT_PASSWORD_BUTTON_XPATH.value).click()

    def close_browser(self):
        self.driver.close()
        self.driver.quit()

