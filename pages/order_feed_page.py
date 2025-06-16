import allure
from pages.base_page import BasePage
from locators.order_feed_page_locator import OrderFeedPageLocator


class OrderFeedPage(BasePage):

    @allure.step('Подождать пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        return self.wait_for_element_hide(OrderFeedPageLocator.OVERLAY_LOCATOR)

    @allure.step('Кликаем по кнопке Конструктор')
    def click_button_constructor(self):
        self.click_on_element(OrderFeedPageLocator.BUTTON_CONSTRUCTOR_LOCATOR)

    @allure.step('Кликаем на заказ из Ленты заказов')
    def click_order(self):
        self.click_on_element(OrderFeedPageLocator.ORDER_LOCATOR)

    @allure.step('Находим номер нового заказа на странице "Лента заказов"')
    def find_number_order(self):
        return self.find_element_with_wait(OrderFeedPageLocator.NUMBER_NEW_ORDER_LOCATOR)

    @allure.step('Находим число сколько всего было сделано заказов')
    def counter_total_orders(self):
        return self.find_element_with_wait(OrderFeedPageLocator.COUNTER_TOTAL_ORDERS_LOCATOR)

    @allure.step('Находим число сколько было сделано заказов за сегодня')
    def counter_orders_today(self):
        return self.find_element_with_wait(OrderFeedPageLocator.COUNTER_TOTAL_ORDERS_LOCATOR)

    @allure.step('Находим наш номер заказа в разделе "В работе"')
    def find_number_in_progress(self):
        return self.find_element_with_wait(OrderFeedPageLocator.NUMBER_ORDER_IN_PROGRESS)

    @allure.step('Проверяем появление заголовка "Лента заказов"')
    def check_title_order_feed(self):
        return self.find_element_with_wait(OrderFeedPageLocator.TEXT_ORDER_FEED)

    @allure.step('Проверяем что откроется всплывающее окно с деталями')
    def check_appears_window_with_details(self):
        return self.find_element_with_wait(OrderFeedPageLocator.MODAL_ORDER_LOCATOR)



