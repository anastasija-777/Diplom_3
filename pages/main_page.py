import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Ждем пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        return self.wait_for_element_hide(MainPageLocators.OVERLAY_LOCATOR)

    @allure.step('Кликаем на главной странице по кнопке "Войти в аккаунт"')
    def click_button_log_in_account(self):
        self.click_on_element(MainPageLocators.BUTTON_LOG_IN_ACCOUNT_LOCATOR)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT_LOCATOR)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_button_order_feed(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED_LOCATOR)
        element.click()

    @allure.step('Кликаем на ингредиент "Флюоресцентная булка"')
    def click_ingredient_fluorescent_bun(self):
        self.click_on_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN_LOCATOR)

    @allure.step('Закрываем окно с деталями ингредиента кликая на крестик')
    def click_cross_button(self):
        self.click_on_element(MainPageLocators.CROSS_BUTTON_LOCATOR)

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_button_place_an_order(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_PLACE_AN_ORDER_LOCATOR)
        element.click()

    @allure.step('Перетаскиваем ингредиента Соус Spicy-X в поле "Перетяните булочку сюда (верх)"')
    def drag_and_drop_ingredient_sauce_spicy_x(self):
        source = self.find_element_with_wait(MainPageLocators.SAUCE_SPICY_X_LOCATOR)
        target = self.find_element_with_wait(MainPageLocators.DRAG_THE_BUN_HERE_TOP)
        self.drag_and_drop_element(source, target)

    @allure.step('Перетаскиваем ингредиента Флюоресцентная булка в поле "Перетяните булочку сюда (верх)"')
    def drag_and_drop_fluorescent_bun(self):
        source = self.find_element_with_wait(MainPageLocators.INGREDIENT_FLUORESCENT_BUN_LOCATOR)
        target = self.find_element_with_wait(MainPageLocators.DRAG_THE_BUN_HERE_TOP)
        self.drag_and_drop_element(source, target)

    @allure.step('Ожидаем когда появится номер заказа')
    def wait_visible_number_order(self):
        return self.find_element_with_wait(MainPageLocators.NUMBER_ORDER_LOCATOR)

    @allure.step('Проверяем появление текста "Соберите бургер" на главной странице')
    def check_current_text_assemble_burger(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_ASSEMBLE_BURGER_LOCATOR)

    @allure.step('Проверяем появление окна с деталями ингредиента')
    def check_modal_ingredient_details(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_INGREDIENT_DETAILS_LOCATOR)

    @allure.step('Проверяем что окно с деталями ингредиента закрывается при нажатии на крестик')
    def check_close_modal_ingredient_details(self):
        return self.wait_for_element_hide(MainPageLocators.CROSS_BUTTON_LOCATOR)

    @allure.step('Проверяем что Соус Spicy-X появился в заказе')
    def check_add_ingredient_sauce_spicy_x(self):
       return self.find_element_with_wait(MainPageLocators.COUNTER_SAUCE_SPICY_X_LOCATOR)

    @allure.step('Проверяем появление номера заказа в появившемся окне')
    def check_visible_text_order_id(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_ORDER_ID_LOCATOR)







    