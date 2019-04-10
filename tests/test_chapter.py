from selene.conditions import visible
from selene.api import *
from input import variables as v
import time


class TestChapter:
    chapter = None

    def test_chapter(self, book_setup):
        self.chapter = book_setup
        ss('span.title').element_by(have.text(self.chapter.title())).click()
        time.sleep(10)


if __name__ == '__main__':
    import pytest
    pytest.main()
