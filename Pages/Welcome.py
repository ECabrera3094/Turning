import time

from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from Locators.Locators import MyLocators


class Welcome:

    # Constructor.
    def __init__(self, driver):

        self.driver = driver
        self.ID_Name = MyLocators.ID_Name
        self.ID_LastName = MyLocators.ID_LastName
        self.CSS_Dont_MiddleName = MyLocators.CSS_Dont_MiddleName
        self.XPath_Month = MyLocators.XPath_Month
        self.XPath_Day = MyLocators.XPath_Day
        self.XPath_Year = MyLocators.XPath_Year
        self.XPath_Gender = MyLocators.XPath_Gender
        self.ID_SSN = MyLocators.ID_SSN
        self.ID_ZipCode = MyLocators.ID_ZipCode
        self.ID_Email = MyLocators.ID_Email
        self.ID_Phone = MyLocators.ID_Phone
        self.XPath_DLS = MyLocators.XPath_DLS
        self.ID_DLN = MyLocators.ID_DLN
        self.dict_States = MyLocators.dict_States
        self.CSS_Certify_Information = MyLocators.CSS_Certify_Information
        self.XPath_Continue = MyLocators.XPath_Continue

    # Método de Instancia == Acción.
    def enter_Name(self):
        self.driver.find_element_by_id(self.ID_Name).send_keys("Emiliano")

    def enter_LastName(self):
        self.driver.find_element_by_id(self.ID_LastName).send_keys("Cabrera")

    def enter_MiddleName(self):
        self.driver.find_element_by_css_selector(self.CSS_Dont_MiddleName).click()

    def enter_Month(self, strMonth):
        myAction = ActionChains(self.driver)
        self.driver.find_element_by_xpath(self.XPath_Month).click()
        XPathMonth = "//li[contains(.,'" + str(strMonth) + "')]"
        XPathMonth = self.driver.find_element_by_xpath(XPathMonth)
        myAction.move_to_element(XPathMonth)
        myAction.click(XPathMonth)
        myAction.send_keys(Keys.ENTER)
        myAction.perform()
        time.sleep(0.5)

    def enter_Day(self, strDay):
        self.driver.find_element_by_xpath(self.XPath_Day).click()
        myAction = ActionChains(self.driver)
        strDay = int(strDay) + 1
        XPathDay = "//*[@id='menu-']/div[2]/ul/li[" + str(strDay) + "]"
        myAction.move_to_element(self.driver.find_element_by_xpath(XPathDay)).click_and_hold().send_keys(Keys.ENTER).perform()

    def enter_Year(self, strYear):
        self.driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div[2]/div[3]/div/div/form/div[5]/div/div[3]/div/div").click()
        myAction = ActionChains(self.driver)
        myAction.move_to_element(self.driver.find_element_by_xpath("//div[@id='menu-']/div[2]/ul/li[48]")).click_and_hold().send_keys(Keys.ENTER).perform()


    def enter_Gender(self, strGender):
        self.driver.find_element_by_xpath(self.XPath_Gender).click()
        if strGender == "Female":
            self.driver.find_element_by_xpath("//li[contains(.,'Female')]").click()
        elif strGender == "Male":
            self.driver.find_element_by_xpath("//li[contains(.,'Male')]").click()

    def enter_SSN(self):
        myAction = ActionChains(self.driver)
        textBox_SSN = self.driver.find_element_by_id("ssn")
        myAction.click_and_hold(textBox_SSN)
        myAction.send_keys_to_element(textBox_SSN, "001234567").send_keys(Keys.TAB)
        myAction.perform()
        time.sleep(0.5)

    def enter_ZipCode(self):
        myAction = ActionChains(self.driver)
        textBox_ZipCode = self.driver.find_element_by_id(self.ID_ZipCode)
        myAction.click_and_hold(textBox_ZipCode)
        myAction.send_keys_to_element(textBox_ZipCode, "16030")
        myAction.perform()
        time.sleep(0.5)

    def enter_Email(self):
        self.driver.find_element_by_id(self.ID_Email).send_keys("cabrerapereze@hotmail.com")

    def enter_Phone(self):
        self.driver.find_element_by_id(self.ID_Phone).send_keys("12345678900")

    def enter_DLS(self, strState):
        self.driver.find_element_by_xpath(self.XPath_DLS).click()
        XPathState = "//li[contains(.,'" + strState + "')]"
        XPathState = self.driver.find_element_by_xpath(XPathState)
        myAction = ActionChains(self.driver)
        myAction.move_to_element(XPathState)
        myAction.click(XPathState)
        myAction.send_keys(Keys.ENTER)
        myAction.perform()
        time.sleep(0.5)

    def enter_DLN(self):
        self.driver.find_element_by_id(self.ID_DLN).send_keys("01234567")

    def click_Certify_Information(self):
        self.driver.find_element_by_css_selector(self.CSS_Certify_Information).click()
        time.sleep(1)

    def click_Continue(self):
        self.driver.find_element_by_xpath(self.XPath_Continue).click()
        time.sleep(0.5)