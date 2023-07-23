import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_something(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/')

        self.assertTrue('To-Do' in browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
