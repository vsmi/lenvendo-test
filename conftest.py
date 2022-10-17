import pytest, requests
from selenium import webdriver

# Фикстуры для API теста

BASE_URL = "https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name"

   
class Product():
    def __init__(self, name: str = None, image: str = None, price: int = None):
        self.name = name
        self.image = image
        self.price = price        


@pytest.fixture()
def send_request():
    res = requests.get(BASE_URL)

    lst_of_products = [Product(product['name'], product['image'], product['price']) for product in res.json()["products"]]

    return lst_of_products



# Фикстуры для UI теста
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver

    driver.close()
