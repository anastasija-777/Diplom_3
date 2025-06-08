import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from curl import reset_password_url


class ResetPasswordPage(BasePage):

    @allure.step('Ожидаем переход на страницу изменения пароля')
    def wait_reset_password_url(self):
        self.wait_url(reset_password_url)

    def click_button_show_password(self):
        self.click_on_element(ResetPasswordPageLocators.BUTTON_SHOW_PASSWORD)

    def check_field_active(self):
        assert self.find_element_with_wait(ResetPasswordPageLocators.FIELD_PASSWORD_ACTIV)