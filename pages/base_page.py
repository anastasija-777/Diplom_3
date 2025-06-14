import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    @allure.step('Инициализация драйвера')
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Находим элемент на странице')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Находим элемент после ожидания его появления на странице')
    def find_element_with_wait(self,locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем переход на новую страницу {url}')
    def wait_url(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        element.click()

    @allure.step('Получаем текст из элемента')
    def get_text_from_element(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Подождать пока элемент станет невидимым')
    def wait_for_element_hide(self,locator):
        WebDriverWait(self.driver,20).until(EC.invisibility_of_element_located(locator))

    @allure.step('Проверяем текущий url')
    def check_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Кликаем по элементу')
    def click_on_element_script(self,locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)














