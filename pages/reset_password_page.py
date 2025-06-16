import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from curl import reset_password_url


class ResetPasswordPage(BasePage):

    @allure.step('Ожидаем переход на страницу изменения пароля')
    def wait_reset_password_url(self):
        return self.wait_url(reset_password_url)

    @allure.step('Ждем пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        return self.wait_for_element_hide(ResetPasswordPageLocators.OVERLAY_LOCATOR)

    @allure.step('Кликаем по кнопке показать/скрыть пароль')
    def click_button_show_password(self):
        self.click_on_element(ResetPasswordPageLocators.BUTTON_SHOW_PASSWORD)

    @allure.step('Проверяем появление поля "Пароль"')
    def check_wait_text_password_recovery(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.TEXT_PASSWORD_RECOVERY)

    @allure.step('Проверяем что поле Пароль стало активно')
    def check_field_active(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.FIELD_PASSWORD_ACTIV)

