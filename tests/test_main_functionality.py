from selenium import webdriver


class TestMainFunctionality:

    def test_switching_to_order_feed_page(self,driver,open_main_page,main_page,order_feed_page):
        main_page.wait_overlay_hide()
        main_page.click_button_order_feed()
        main_page.check_current_page_order_feed()

    def test_switching_to_main_page_by_button_constructor(self,driver,open_order_feed_page,main_page,order_feed_page):
        order_feed_page.wait_overlay_hide()
        order_feed_page.click_button_constructor()
        main_page.wait_overlay_hide()
        main_page.check_current_text_assemble_burger()

    def test_click_on_ingredient_fluorescent_bun_shows_ingredient_details(self, driver, open_main_page, main_page):
        main_page.wait_overlay_hide()
        main_page.click_ingredient_fluorescent_bun()
        main_page.check_modal_ingredient_details()

    def test_click_on_cross_button_close_page_ingredient_details(self, driver, open_main_page, main_page):
        main_page.wait_overlay_hide()
        main_page.click_ingredient_fluorescent_bun()
        main_page.click_cross_button()
        main_page.check_close_modal_ingredient_details()

    def test_after_drag_and_drop_ingredient_counter_increases(self, driver, open_main_page, main_page):
        main_page.drag_and_drop_ingredient_sauce_spicy_x()
        main_page.check_add_ingredient_sauce_spicy_x()

    def test_logged_in_user_can_place_an_order(self, driver, open_login_page, main_page,login_page,body_user):
        body = body_user
        email = body['email']
        password = body['password']
        login_page.wait_overlay_hide()
        login_page.write_email(email)
        login_page.write_password(password)
        login_page.wait_overlay_hide()
        login_page.click_button_login()
        main_page.wait_overlay_hide()
        main_page.drag_and_drop_fluorescent_bun()
        main_page.click_button_place_an_order()
        main_page.check_visible_text_order_id()




