import allure
from pages.base_page import BasePage
from curl import restore_password_url
from locators.restore_password_page_locators import RestorePasswordPageLocators


class RestorePasswordPage(BasePage):

    @allure.step('Ожидаем появление поля  Email')
    def wait_field_email(self):
        return self.find_element_with_wait(RestorePasswordPageLocators.FIELD_EMAIL_LOCATOR)

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
        return self.wait_url(restore_password_url)

