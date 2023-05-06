from selenium import webdriver
from selenium.webdriver.common.by import By
from enum import Enum


class Identifiers(Enum):
    FINANCE_LINK = "//*[@id='root_6']"
    MARKET_DATA_LINK = "//*[contains(@title, 'Market Data')]"
    CALENDAR_LINKS = "//*[contains(@href,'//uk.finance.yahoo.com/calendar/') and contains(@title,'Calendar')]"
    CALENDAR_DATES_XPATH = "//*[@id='fin-cal-events']/div[2]/ul"
    HOME_PAGE = "//*[@id='ybar-logo']"
    CALENDAR_REDIRECT = "https://uk.finance.yahoo.com/calendar/"


class MarketData:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def click_on_finance_link(self):
        self.driver.find_element(By.XPATH, Identifiers.FINANCE_LINK.value).click()

    def click_on_market_data_link(self):
        self.driver.find_element(By.XPATH, Identifiers.MARKET_DATA_LINK.value).click()

    def click_on_calendar_link(self):
        # self.driver.find_element(By.XPATH, Identifiers.CALENDAR_LINKS.value).click()
        self.driver.get(Identifiers.CALENDAR_REDIRECT.value)

    def get_all_calender_elements(self):
        dropdown_ul = self.driver.find_element(By.XPATH, Identifiers.CALENDAR_DATES_XPATH.value)
        return dropdown_ul.find_elements(By.TAG_NAME, 'li')

    def get_home_page_name(self):
        return self.driver.find_element(By.XPATH, Identifiers.HOME_PAGE.value).get_property('innerText')

    def get_all_dates(self):
        date_elements = self.get_all_calender_elements()
        dates = [each_element.find_element(By.TAG_NAME, 'div').get_property('innerText') for each_element in
                 date_elements]
        return dates

    def match_date(self, dateToMatch) -> bool:
        if dateToMatch in self.get_all_dates():
            return True
        return False

    def get_finance_link_name(self):
        return self.driver.find_element(By.XPATH, Identifiers.FINANCE_LINK.value).get_property('innerText')
