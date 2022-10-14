import pytest


BASE_URL = "https://www.lenvendo.ru/api/js-test-task"

   
class Url():
    def __init__(self, search: str = None, sort_field: str = None) -> str:
        self.search = search
        self.sort_field = sort_field

    def create_url(self):
        if self.search and self.sort_field:
            URL = BASE_URL + f'/?search={self.search}&sort_field={self.sort_field}'
        elif self.search and not self.sort_field:
            URL = BASE_URL + f'/?search={self.search}'
        elif not self.search and self.sort_field:
            URL = BASE_URL + f'/?sort_field={self.sort_field}'
        else:
            URL = BASE_URL + '/'
        return URL
        
@pytest.fixture()
def return_url():
    return Url()

