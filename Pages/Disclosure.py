import time

from Locators.Locators import MyLocators


class Disclosure:

    def __init__(self, driver):
        self.driver = driver
        self.XPath_Disclosure_Background = MyLocators.XPath_Disclosure_Background
        self.XPath_Next_Document_2 = MyLocators.XPath_Next_Document_2

    def click_Disclosure_Backgound(self):
        self.driver.find_element_by_xpath(self.XPath_Disclosure_Background).click()
        time.sleep(1)

    def click_Next_Document(self):
        self.driver.find_element_by_xpath(self.XPath_Next_Document_2).click()
        time.sleep(1)