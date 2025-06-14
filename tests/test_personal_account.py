import allure
from selenium import webdriver


class TestPersonalAccount:

    @allure.title('Проверяем переход по клику на кнопку «Личный кабинет»')
    def test_click_button_personal_account(self,driver,
                                           open_login_page,
                                           main_page,
                                           login_page,
                                           personal_account_page,
                                           body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Войти"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Личный кабинет"'):
            main_page.click_button_personal_account()
        with allure.step('Ждем пока оверлей станет невидимым'):
            personal_account_page.wait_overlay_hide()
        with allure.step('Проверяем появление текста "Профиль"'):
            assert personal_account_page.check_text_profile

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_click_hyperlink_order_history(self,driver,
                                           open_login_page,
                                           main_page,
                                           login_page,
                                           personal_account_page,
                                           body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Войти"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Личный кабинет"'):
            main_page.click_button_personal_account()
        with allure.step('Ждем пока оверлей станет невидимым'):
            personal_account_page.wait_overlay_hide()
        with allure.step('Кликаем по гиперссылке "История заказов"'):
            personal_account_page.click_hyperlink_order_history()
        with allure.step('Проверяем что перешли на страницу "История заказов"'):
            assert personal_account_page.check_current_page_order_history

    @allure.title('Проверить выход из аккаунта')
    def test_click_hyperlink_exit(self,driver,
                                  open_login_page,
                                  main_page,
                                  login_page,
                                  personal_account_page,
                                  body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Войти"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Личный кабинет"'):
            main_page.click_button_personal_account()
        with allure.step('Ждем пока оверлей станет невидимым'):
            personal_account_page.wait_overlay_hide()
        with allure.step('Кликаем по гиперссылке "Выход"'):
            personal_account_page.click_hyperlink_exit()
        with allure.step('Проверяем что вышли из профиля'):
            assert personal_account_page.check_current_login_page

