import time

from Locators.Locators import MyLocators


class Confirmation:

    def __init__(self, driver):
        self.driver = driver
        self.ID_Name_Confirm = MyLocators.ID_Name_Confirm
        self.XPath_Draw_Signature = MyLocators.XPath_Draw_Signature
        self.XPath_Indicate_Agreement = MyLocators.XPath_Indicate_Agreement
        self.XPath_Submit = MyLocators.XPath_Submit

    def enter_Name_Confirm(self):
        self.driver.find_element_by_id(self.ID_Name_Confirm).send_keys("Emiliano")
        time.sleep(1.5)

    def draw_Signature(self):
        self.driver.find_element_by_xpath(self.XPath_Draw_Signature).click()
        time.sleep(1.5)

    def click_Indicate_Agreement(self):
        self.driver.find_element_by_xpath(self.XPath_Indicate_Agreement).click()
        time.sleep(1.5)

    def click_Submit(self):
        self.driver.find_element_by_xpath(self.XPath_Submit).click()
        time.sleep(1.5)