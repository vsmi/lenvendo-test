import pytest, requests

class Product():
    def __init__(self, name: str = None, image: str = None, price: int = None):
        self.name = name
        self.image = image
        self.price = price 

"""
Тесты для запроса 'GET https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name'

** Основной кейс
1 тест-кейс - Запрос с параметрами search и sort_field со значениями Alcatel и name, соответсвенно
ОР - Все поля name содержат указанное значение в параметре search И элементы отсортированы по полю name

**** Доп кейсы
2 тест-кейс - Запрос только параметром search со значением Alcatel
ОР - Все поля name содержат указанное значение в параметре search И список элементов не отсортирован

3 тест-кейс - Запрос с параметрами search и sort_field со значениями Alcatel и price, соответсвенно
ОР - Все поля name содержат указанное значение в параметре search И элементы отсортированы по полю price

4 тест-кейс - Запрос без параметров
ОР - В ответе приходит отсортированный список Alcatel продуктов, поэтому тест фейлится
"""

@pytest.mark.parametrize("search, sort_field, flag_of_name, is_sorted", [
    ("Alcatel", "name", True, True),  # 1 тест-кейс
    ("Alcatel", None, True, False),   # 2 тест-кейс
    ("Alcatel", "price", True, True), # 3 тест-кейс
    (None, None, False, False)        # 4 тест-кейс
    ])


def test_alcatel_sorted_result(return_url, search, sort_field, flag_of_name, is_sorted):
    return_url.search = search
    return_url.sort_field = sort_field
    url = return_url.create_url()
    print("URL FOR TEST", url)
    res = requests.get(url)

    lst_of_products = [Product(product['name'], product['image'], product['price']) for product in res.json()["products"]]
                
    for product in lst_of_products:
        flag_Alcatel = True
        if "Alcatel" not in product.name:
            flag_Alcatel = False
            break

    if sort_field:
        list_of_sorted_products = sorted(lst_of_products, key= lambda product: getattr(product, sort_field))
        flag_is_sorted = lst_of_products == list_of_sorted_products
    else:
        flag_is_sorted = False

    assert flag_Alcatel == flag_of_name
    assert flag_is_sorted == is_sorted
    assert res.status_code == 200


