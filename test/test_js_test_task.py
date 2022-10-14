import pytest

"""
Тесты для запроса 'GET https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name'

** Основной кейс
Запрос с параметрами search и sort_field со значениями Alcatel и name, соответсвенно
ОР - Все поля name содержат указанное значение в параметре search И элементы отсортированы по полю name

"""

def test_alcatel_sorted_result(send_request): 

    for product in send_request:
        flag_Alcatel = True
        if "Alcatel" not in product.name:
            flag_Alcatel = False
            break

    list_of_sorted_products = sorted(send_request, key= lambda product: getattr(product, 'name'))
    flag_is_sorted = send_request == list_of_sorted_products

    assert flag_Alcatel 
    assert flag_is_sorted
