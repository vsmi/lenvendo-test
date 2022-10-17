import re
from Pages.BasePage import BasePageClass
import pytest
from selenium.webdriver.common.by import By

class BasePageElements:
    locator_of_cards = (By.XPATH, "/html/body/div[1]/div[2]/form/div[3]")
    locator_of_result = (By.XPATH, "/html/body/div[1]/div[2]/form/div[3]/div[3]/div[2]")
    

def test_1(driver):
    testpage  = BasePageClass(driver)
    testpage.go_to_site()
   
    testpage.find_element(BasePageElements.locator_of_cards)

    for i in range(1,7):
        xpath_of_element = f"/html/body/div[1]/div[2]/form/div[3]/div[2]/ul/li[{i}]"
        locator_of_card = (By.XPATH, xpath_of_element)
        if not locator_of_card:
            flag_cards_available = False
        else:
            testpage.do_click(locator_of_card)
            flag_cards_available = True

    assert flag_cards_available == True
 


