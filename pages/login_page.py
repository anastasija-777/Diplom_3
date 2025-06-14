import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step('Ожидаем загрузки гиперссылки "Восстановить пароль" и кликаем по ней')
    def click_on_hyperlink_restore_password(self):
        self.click_on_element_script(LoginPageLocators.HYPERLINK_RESTORE_PASSWORD_LOCATOR)

    @allure.step('В поле Email пишем адрес электронной почты')
    def write_email(self,email):
        self.click_on_element_script(LoginPageLocators.FiELD_EMAIL)
        element = self.find_element_with_wait(LoginPageLocators.TEXT_EMAIL_LOCATOR)
        element.send_keys(email)

    @allure.step('В поле Пароль пишем пароль')
    def write_password(self,password):
        self.click_on_element_script(LoginPageLocators.FIELD_PASSWORD)
        element = self.find_element_with_wait(LoginPageLocators.TEXT_PASSWORD_LOCATOR)
        element.send_keys(password)

    @allure.step('Ждем пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        self.wait_for_element_hide(LoginPageLocators.OVERLAY_LOCATOR)

    @allure.step('Кликаем по кнопке "Войти"')
    def click_button_login(self):
        self.click_on_element_script(LoginPageLocators.BUTTON_LOGIN_LOCATOR)





