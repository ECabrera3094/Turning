import time

from Locators.Locators import MyLocators


class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.XPath_Agreement = MyLocators.XPath_Agreement
        self.XPath_ReviewData = MyLocators.XPath_ReviewData

    def click_Agreement(self):
        self.driver.find_element_by_xpath(self.XPath_Agreement).click()
        time.sleep(1)

    def click_ReviewData(self):
        self.driver.find_element_by_xpath(self.XPath_ReviewData).click()
        time.sleep(1)