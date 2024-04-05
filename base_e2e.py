import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5173/login")

    def tearDown(self) -> None:
        self.driver.quit()

    def input_text(self, test_id: str, text: str):
        field = self.driver.find_element(By.XPATH, f"//*[@data-testid='{test_id}']")
        field.click()
        field.send_keys(text)

    def click_button(self, test_id: str):
        self.__click_element(test_id=test_id)

    def click_link(self, test_id: str):
        self.__click_element(test_id=test_id)

    def select_option_value(self, test_id: str, value: str):
        select = Select(
            self.driver.find_element(By.XPATH, f"//*[@data-testid='{test_id}']")
        )
        select.select_by_value(value)

    def assert_visible(self, test_id: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[@data-testid='{test_id}']"))
        )
        self.assertTrue(element.is_displayed())

    def assert_contains_text(self, test_id: str, text: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[@data-testid='{test_id}']"))
        )
        self.assertTrue(text in element.text)

    def assert_modal_contains(self, modal_test_id: str, **kwargs):
        self.assert_visible(test_id=modal_test_id)
        for key, value in kwargs.items():
            self.assert_contains_text(test_id=f"{modal_test_id}-{key}", text=value)

    def __click_element(self, test_id: str):
        clickable = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[@data-testid='{test_id}']"))
        )
        clickable.click()
