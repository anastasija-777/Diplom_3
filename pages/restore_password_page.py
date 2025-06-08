import allure
from pages.base_page import BasePage
from curl import restore_password_url, reset_password_url
from locators.restore_password_page_locators import RestorePasswordPageLocators


class RestorePasswordPage(BasePage):

    @allure.step('Ожидаем переход на страницу "Восстановление пароля"')
    def wait_login_url(self):
        self.wait_url(restore_password_url)

    @allure.step('Кликаем по полю Email')
    def click_on_field_email(self):
        self.click_on_element(RestorePasswordPageLocators.FIELD_EMAIL_LOCATOR)

    @allure.step('Пишем в поле email пользователя')
    def write_email_in_field(self,email):
        element = self.find_element_with_wait(RestorePasswordPageLocators.TEXT_EMAIL_LOCATOR)
        element.send_keys(email)

    @allure.step('Кликаем по кнопке "Восстановить"')
    def click_on_button_recover(self):
        self.click_on_element(RestorePasswordPageLocators.BUTTON_RECOVER_LOCATOR)

    @allure.step('Проверяем что перешли на страницу "Восстановление пароля"')
    def check_current_page_restore_password_page(self):
        self.wait_url(restore_password_url)

    @allure.step('Проверяем что перешли на страницу изменения пароля')
    def check_current_page_reset_password_page(self):
        self.wait_url(reset_password_url)