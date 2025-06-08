import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import main_url


class MainPage(BasePage):

    @allure.step('Кликаем на главной странице по кнопке "Войти в аккаунт"')
    def click_button_log_in_account(self):
        self.click_on_element(MainPageLocators.BUTTON_LOG_IN_ACCOUNT_LOCATOR)

    @allure.step('Подождать пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_LOCATOR)

    def click_button_personal_account(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT_LOCATOR)

    @allure.step('Ожидаем переход на главную страницу')
    def wait_main_url(self):
        self.wait_url(main_url)

    def click_button_order_feed(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED_LOCATOR)
        element.click()

    @allure.step('Проверяем что перешли на страницу "Лента заказов"')
    def check_current_text_assemble_burger(self):
        self.find_element_with_wait(MainPageLocators.TEXT_ASSEMBLE_BURGER_LOCATOR)

    def click_ingredient_fluorescent_bun(self):
        self.click_on_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN_LOCATOR)

    def check_modal_ingredient_details(self):
        self.find_element_with_wait(MainPageLocators.TEXT_INGREDIENT_DETAILS_LOCATOR)

    def click_cross_button(self):
        self.click_on_element(MainPageLocators.CROSS_BUTTON_LOCATOR)

    def check_close_modal_ingredient_details(self):
        self.wait_for_element_hide(MainPageLocators.CROSS_BUTTON_LOCATOR)

    def drag_and_drop_ingredient_sauce_spicy_x(self):
        source = self.find_element_with_wait(MainPageLocators.SAUCE_SPICY_X_LOCATOR)
        target = self.find_element_with_wait(MainPageLocators.DRAG_THE_BUN_HERE_TOP)
        self.drag_and_drop_element(source, target)

    def check_add_ingredient_sauce_spicy_x(self):
        self.find_element_with_wait(MainPageLocators.COUNTER_SAUCE_SPICY_X_LOCATOR)

    def drag_and_drop_fluorescent_bun(self):
        source = self.find_element_with_wait(MainPageLocators.INGREDIENT_FLUORESCENT_BUN_LOCATOR)
        target = self.find_element_with_wait(MainPageLocators.DRAG_THE_BUN_HERE_TOP)
        self.drag_and_drop_element(source, target)

    def click_button_place_an_order(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_PLACE_AN_ORDER_LOCATOR)
        element.click()

    def check_visible_text_order_id(self):
        self.find_element_with_wait(MainPageLocators.TEXT_ORDER_ID_LOCATOR)






    