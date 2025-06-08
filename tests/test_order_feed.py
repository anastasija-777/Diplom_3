from selenium import webdriver


class TestOrderFeed:

    def test_click_order_appears_window_with_details(self,driver,open_order_feed_page,order_feed_page):
        order_feed_page.click_order()
        order_feed_page.check_appears_window_with_details()

