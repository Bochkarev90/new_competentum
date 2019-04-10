from pages.base_page import BasePage


class BookPage(object):
    contentsTab_button = 'button[role="tab"]:nth-child(1)'
    notebookTab_button = 'button[role="tab"]:nth-child(2)'
    studyToolsTab_button = 'button[role="tab"]:nth-child(3)'
