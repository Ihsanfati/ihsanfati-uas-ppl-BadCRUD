import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_1_open_login_page(self):
        self.browser.get('http://localhost/ihsanfati-uas-ppl-BadCRUD/login.php')
        expected_result = "Please sign in"
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    def test_2_invalid_username(self):
        self.browser.find_element(By.ID, "inputUsername").send_keys("usernametidakbenar")
        self.browser.find_element(By.ID, "inputPassword").send_keys("minda666!")
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_result = "Wrong username or password"
        actual_result = self.browser.find_element(By.XPATH, "//div[@class='checkbox mb-3']/label").text
        self.assertIn(expected_result, actual_result)

    def test_3_invalid_password(self):
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("passwordtidakbenar")
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_result = "Wrong username or password"
        actual_result = self.browser.find_element(By.XPATH, "//div[@class='checkbox mb-3']/label").text
        self.assertIn(expected_result, actual_result)

    def test_4_valid_credentials(self):
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("minda666!")
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_url = "http://localhost/ihsanfati-uas-ppl-BadCRUD/index.php"
        self.assertEqual(expected_url, self.browser.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')