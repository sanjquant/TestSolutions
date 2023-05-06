from pathlib import Path
from selenium import webdriver
from enum import Enum
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import calendar
import pandas as pd


class FILEDIRECTORY(Enum):
    FEATURE_FILE_DIR = "featureFiles"
    FILE_DIR_NAME = "files"
    DRIVER_DIR = "driver"
    CREDENTIALS_FILE_NAME = "Credentials.xlsx"


class DAYSOFWEEK(Enum):
    WEEK_DAYS: list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


class MONTHS(Enum):
    LIST_OF_MONTHS: list = ["Jan", "Feb", "Mar", "Apr", "May","Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]


class Util:

    def __init__(self, featurefileName):
        self.BASE_DIR: str = None
        self.featurefileName = featurefileName
        self.featurefiledir: str = FILEDIRECTORY.FEATURE_FILE_DIR.value
        self.file_dir = FILEDIRECTORY.FILE_DIR_NAME.value
        self.driver_dir = FILEDIRECTORY.DRIVER_DIR.value
        self.get_parent()

    def get_parent(self):
        self.BASE_DIR = Path(__file__).resolve().parent
        print(self.BASE_DIR)

    def get_feature_file_dir(self):
        return self.BASE_DIR.joinpath(self.featurefiledir).joinpath(self.featurefileName)

    def get_test_data_file_path(self, filename):
        return self.BASE_DIR.joinpath(self.file_dir).joinpath(filename)

    def get_driver_path(self):
        return self.BASE_DIR.joinpath(self.driver_dir).joinpath("chromedriver.exe")

    def get_chrome_driver(self):
        driver: webdriver = webdriver.Chrome(executable_path=self.get_driver_path())
        return driver

    def get_driver_chome_service(self):
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def get_todays_date(self):
        DAY_OF_WEEK = DAYSOFWEEK.WEEK_DAYS.value[calendar.weekday(datetime.today().year, datetime.today().month, datetime.today().day)]
        DAY = datetime.today().day
        MON = MONTHS.LIST_OF_MONTHS.value[datetime.today().month-1]
        return f"{DAY}{MON}{DAY_OF_WEEK}"

    def read_excel_data(self):
        df = pd.read_excel(self.get_test_data_file_path(FILEDIRECTORY.CREDENTIALS_FILE_NAME.value))
        return df
