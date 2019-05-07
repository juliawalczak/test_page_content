# -*- coding: utf-8" -*

import unittest
from selenium import webdriver


class Wsb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_wsb(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/")

        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)

    def test_wsb_wroclaw(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/wroclaw/")
        self.assertIn(u"Wrocławiu", driver.title)

    def test_wsb_chorzow(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/chorzow/")
        self.assertIn(u"Chorzowie", driver.title)

    def test_gdansk(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/gdansk/")
        self.assertIn(u"Gdańsku", driver.title)

    def tearUp(self):
        self.driver.quit()


if __name__ == "main__":
    unittest.main()