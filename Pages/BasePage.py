from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
   


class BasePageClass:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://HR:test@qa.digift.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
   

    def do_click(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()

    
    def is_element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return bool(element)
    
    
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return element.text


    