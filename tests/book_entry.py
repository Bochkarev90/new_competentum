from input import variables as v
from tests.login import Login


class BookEntry:
    def __init__(self, book_name):
        self.browser = Login(v.browser, v.revel, v.username, v.password).login()
        self._book_name = book_name

    def book_entry(self):
        """
        Находит название книги на странице и заходит в нее
        """
        pass
