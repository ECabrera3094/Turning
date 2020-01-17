import time

from Locators.Locators import MyLocators


class Right:

    def __init__(self, driver):
        self.driver = driver
        self.XPath_Summary_Rights = MyLocators.XPath_Summary_Rights
        self.XPath_Next_Document = MyLocators.XPath_Next_Document

    def click_Summary_Rights(self):
        self.driver.find_element_by_xpath(self.XPath_Summary_Rights).click()
        time.sleep(1)

    def click_Next_Document(self):
        self.driver.find_element_by_xpath(self.XPath_Next_Document).click()
        time.sleep(1)