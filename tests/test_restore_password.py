import allure
from selenium import webdriver


class TestRestorePassword:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_restore_password_page_through_button_log_in_account(self,driver,
                                                                    open_login_page,
                                                                    login_page,
                                                                    restore_password_page,
                                                                    create_user):
        with allure.step('Ожидаем когда оверлейн исчезнет'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по гиперссылке "Восстановить пароль"'):
            login_page.click_on_hyperlink_restore_password()
        with allure.step('Ожидаем пока появится поле Email'):
            restore_password_page.wait_field_email()
        with allure.step('Проверяем что перешли на страницу "Восстановление пароля"'):
            assert restore_password_page.check_current_page_restore_password_page


    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_write_email_and_click_button_recover(self, driver,
                                                  open_restore_password_page,
                                                  restore_password_page,
                                                  reset_password_page,
                                                  create_user):
        with allure.step('Создаем нового пользователя'):
            response = create_user
            response_json =  response.json()
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = response_json['user']['email']
        with allure.step('Кликаем по полю email'):
            restore_password_page.click_on_field_email()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            restore_password_page.write_email_in_field(email)
        with allure.step('Кликаем по кнопке "Восстановить"'):
            restore_password_page.click_on_button_recover()
        with allure.step('Ждем пока оверлей станет невидимым'):
            reset_password_page.wait_overlay_hide()
        with allure.step('Ожиданием появления заголовка "Восстановление пароля"'):
            assert reset_password_page.check_wait_text_password_recovery

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_button_show_password_makes_field_active(self, driver,
                                                           open_restore_password_page,
                                                           restore_password_page,
                                                           reset_password_page,
                                                           create_user):
        with allure.step('Создаем нового пользователя'):
            response = create_user
            response_json = response.json()
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = response_json['user']['email']
        with allure.step('Кликаем по полю email'):
            restore_password_page.click_on_field_email()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            restore_password_page.write_email_in_field(email)
        with allure.step('Кликаем по кнопке "Восстановить"'):
            restore_password_page.click_on_button_recover()
        with allure.step('Ожидаем переход на страницу изменения пароля'):
            reset_password_page.wait_reset_password_url()
        with allure.step('Кликаем по кнопке показать/скрыть пароль'):
            reset_password_page.click_button_show_password()
        with allure.step('Проверяем что поле Пароль стало активно'):
            assert reset_password_page.check_field_active



