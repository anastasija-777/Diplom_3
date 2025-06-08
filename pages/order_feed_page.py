import allure
from pages.base_page import BasePage
from locators.order_feed_page_locator import OrderFeedPageLocator
from curl import main_url


class OrderFeedPage(BasePage):

    @allure.step('Подождать пока оверлей станет невидимым')
    def wait_overlay_hide(self):
        self.wait_for_element_hide(OrderFeedPageLocator.OVERLAY_LOCATOR)

    def click_button_constructor(self):
        self.click_on_element(OrderFeedPageLocator.BUTTON_CONSTRUCTOR_LOCATOR)

    @allure.step('Проверяем что перешли на страницу "Лента заказов"')
    def check_current_main_page(self):
        self.wait_url(main_url)

    def click_order(self):
        self.click_on_element(OrderFeedPageLocator.ORDER_LOCATOR)

    @allure.step('Проверяем что откроется всплывающее окно с деталями')
    def check_appears_window_with_details(self):
        self.find_element_with_wait(OrderFeedPageLocator.MODAL_ORDER_LOCATOR)