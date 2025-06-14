import allure
from pages.base_page import BasePage
from locators.order_history_page_locator import OrderHistoryPageLocators


class OrderHistoryPage(BasePage):

    @allure.step('Находим номер заказа на странице "История заказов"')
    def find_number_order(self):
        return self.find_element_with_wait(OrderHistoryPageLocators.NUMBER_NEW_ORDER_LOCATOR)


    @allure.step('Кликаем по кнопке "Лента заказов" на странице "История заказов"')
    def click_button_order_feed(self):
        element = self.find_element_with_wait(OrderHistoryPageLocators.BUTTON_ORDER_FEED_LOCATOR)
        element.click()

