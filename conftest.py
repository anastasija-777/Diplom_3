import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from curl import create_user_url,main_url, delete_user_url, restore_password_url, login_user_api_url,login_user_page_url,order_feed_url
from pages.restore_password_page import RestorePasswordPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_history_page import OrderHistoryPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.order_feed_page import OrderFeedPage
from generators import generate_body_create_user


@allure.step('Создаем драйвер для браузеров Google Сhrome и Firefox')
@pytest.fixture(params = ["chrome","firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@allure.step('Открываем главную страницу')
@pytest.fixture(scope= 'function')
def open_main_page(driver):
    driver.get(main_url)

@allure.step('Открываем страницу "Восстановление пароля"')
@pytest.fixture(scope= 'function')
def open_restore_password_page(driver):
    driver.get(restore_password_url)

@allure.step('Открываем страницу авторизации')
@pytest.fixture(scope= 'function')
def open_login_page(driver):
    driver.get(login_user_page_url)

@allure.step('Открываем страницу Лента заказов')
@pytest.fixture(scope= 'function')
def open_order_feed_page(driver):
    driver.get(order_feed_url)

@allure.step('Создаем объект главной страницы')
@pytest.fixture(scope= 'function')
def main_page(driver):
    return MainPage(driver)

@allure.step('Создаем объект страницы авторизации')
@pytest.fixture(scope= 'function')
def login_page(driver):
    return LoginPage(driver)

@allure.step('Создаем объект страницы "Восстановление пароля"')
@pytest.fixture(scope= 'function')
def restore_password_page(driver):
    return RestorePasswordPage(driver)

@allure.step('Создаем объект страницы "Восстановление пароля" для изменения пароля')
@pytest.fixture(scope= 'function')
def reset_password_page(driver):
    return ResetPasswordPage(driver)

@allure.step('Создаем объект страницы "Личный кабинет"')
@pytest.fixture(scope= 'function')
def personal_account_page(driver):
    return PersonalAccountPage(driver)

@allure.step('Создаем объект страницы "Лента заказов"')
@pytest.fixture(scope= 'function')
def order_feed_page(driver):
    return OrderFeedPage(driver)

@allure.step('Создаем объект страницы "История заказов"')
@pytest.fixture(scope= 'function')
def order_history_page(driver):
    return OrderHistoryPage(driver)

@allure.step('Создаем нового пользователя и после теста удаляем данного пользователя.')
@pytest.fixture(scope = "function")
def create_user():
    body = generate_body_create_user()
    response = requests.post(create_user_url,data = body)

    yield response
    if response.status_code == 200:
        json_response = response.json()
        token = json_response['accessToken']
        headers = {'Authorization': token}
        requests.delete(delete_user_url,headers = headers)

@allure.step('Создаем нового пользователя, передаем данные для авторизации в тест и после теста удаляем данного пользователя.')
@pytest.fixture(scope = "function")
def body_user():
    body = generate_body_create_user()
    requests.post(create_user_url,data = body)
    email = body['email']
    password = body['password']
    body_login = {
                   "email": email,
                   "password": password
                }

    yield body_login
    response = requests.post(login_user_api_url, data = body_login)
    json_response = response.json()
    token = json_response['accessToken']
    headers = {'Authorization': token}
    requests.delete(delete_user_url, headers=headers)

