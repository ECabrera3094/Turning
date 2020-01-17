import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.Welcome import Welcome
from Pages.Rights import Right
from Pages.Disclosure import Disclosure
from Pages.Authorization import Authorization
from Pages.Confirmation import Confirmation


class Turning(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('Drivers/chromedriver')
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_Turning(self):
        driver = self.driver
        driver.get("https://partners.turning.io/apply/Turn%20Technologies/45941fa4-829f-4901-a7df-273f7db7e78c")

        # Explicit Wait
        try:
            textBox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "firstName"))
            )
        except:
            driver.refresh()

        # Creamos el Objeto 'login' INSTANCIANDO a la Clase MyLoginPage().
        welcome = Welcome(driver)
        welcome.enter_Name()
        welcome.enter_LastName()
        welcome.enter_MiddleName()
        welcome.enter_Month("April")
        welcome.enter_Day("25")
        welcome.enter_Year("1971")
        welcome.enter_Gender("Male")
        welcome.enter_SSN()
        welcome.enter_ZipCode()
        welcome.enter_Email()
        welcome.enter_Phone()
        welcome.enter_DLS("Texas")
        welcome.enter_DLN()
        welcome.click_Certify_Information()
        welcome.click_Continue()

        rights = Right(driver)
        rights.click_Summary_Rights()
        rights.click_Next_Document()

        disclosure = Disclosure(driver)
        disclosure.click_Disclosure_Backgound()
        disclosure.click_Next_Document()

        authorization = Authorization(driver)
        authorization.click_Agreement()
        authorization.click_ReviewData()

        confirmation = Confirmation(driver)
        confirmation.enter_Name_Confirm()
        confirmation.draw_Signature()
        confirmation.click_Indicate_Agreement()
        confirmation.click_Submit()

        message = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/p[2]/span/span")))

    @classmethod
    def tearDownClass(cls):
        print('END of TestCase.')
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()