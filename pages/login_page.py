import allure
from pages.base_page import BasePage
from curl import login_url
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step('Ожидаем переход на страницу авторизации')
    def wait_login_url(self):
        self.wait_url(login_url)

    @allure.step('Ожидаем загрузки гиперссылки "Восстановить пароль" и кликаем по ней')
    def click_on_hyperlink_restore_password(self):
        self.click_on_element(LoginPageLocators.HYPERLINK_RESTORE_PASSWORD_LOCATOR)

    def write_email(self,email):
        self.click_on_element(LoginPageLocators.FiELD_EMAIL)
        element = self.find_element_with_wait(LoginPageLocators.TEXT_EMAIL_LOCATOR)
        element.send_keys(email)

    def write_password(self,password):
        self.click_on_element(LoginPageLocators.FIELD_PASSWORD)
        element = self.find_element_with_wait(LoginPageLocators.TEXT_PASSWORD_LOCATOR)
        element.send_keys(password)

    @allure.step('Подождать пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        self.wait_for_element_hide(LoginPageLocators.OVERLAY_LOCATOR)

    def click_button_login(self):
        self.click_on_element(LoginPageLocators.BUTTON_LOGIN_LOCATOR)





