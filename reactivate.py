from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import datetime as dt 

class Reactivate:
    def __init__(self, headless = True):
        self.headless = headless
        self.options = Options()
        self.service = Service(ChromeDriverManager().install())
    def get_url(self):
        if self.headless:
            self.options.add_argument("--headless")
            self.options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(
            options = self.options,
            service = self.service
        )
        self.driver.get("https://rafaelcoelho.streamlit.app/")
        self.driver.maximize_window()
    def search_get_up_button(self):
        time.sleep(10)
        try:
            self.get_up_button = self.driver.find_element(
                By.XPATH,
                '//button[text() = "Yes, get this app back up!"]'
            )
            if self.get_up_button.is_displayed():
                self.get_up_button.click()
                print(self.get_up_button.text)
        except NoSuchElementException:
            print("Button not found.")
            pass

bot = Reactivate()
bot.get_url()
bot.search_get_up_button()