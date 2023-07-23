import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/')

        self.assertTrue('Django' in browser.title)


if __name__ == '__main__':
    unittest.main()
