import allure
from pages.base_page import BasePage
from curl import order_history_url,login_user_page_url
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):

    @allure.step('Подождать пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        self.wait_for_element_hide(PersonalAccountPageLocators.OVERLAY_LOCATOR)

    @allure.step('Кликаем по гиперссылке "История заказов"')
    def click_hyperlink_order_history(self):
        element = self.find_element_with_wait(PersonalAccountPageLocators.HYPERLINK_ORDER_HISTORY_LOCATOR)
        element.click()

    @allure.step('Кликаем по гиперссылке "Выход"')
    def click_hyperlink_exit(self):
        element = self.find_element_with_wait(PersonalAccountPageLocators.HYPERLINK_EXIT_LOCATOR)
        element.click()

    @allure.step('Проверяем появление текста "Профиль"')
    def check_text_profile(self):
        self.find_element_with_wait(PersonalAccountPageLocators.TEXT_PROFILE_LOCATOR)

    @allure.step('Проверяем что перешли на страницу "История заказов"')
    def check_current_page_order_history(self):
        self.wait_url(order_history_url)

    @allure.step('Проверяем что вышли из профиля')
    def check_current_login_page(self):
        self.wait_url(login_user_page_url)


