from selenium import webdriver


class TestPersonalAccount:

    def test_click_button_personal_account(self,driver,open_login_page,main_page,login_page,personal_account_page,body_user):
        body = body_user
        email = body['email']
        password = body['password']
        login_page.wait_overlay_hide()
        login_page.write_email(email)
        login_page.write_password(password)
        login_page.wait_overlay_hide()
        login_page.click_button_login()
        main_page.wait_overlay_hide()
        main_page.click_button_personal_account()
        personal_account_page.wait_overlay_hide()
        personal_account_page.check_text_profile()

    def test_click_hyperlink_order_history(self,driver,open_login_page,main_page,login_page,personal_account_page,body_user):
        body = body_user
        email = body['email']
        password = body['password']
        login_page.wait_overlay_hide()
        login_page.write_email(email)
        login_page.write_password(password)
        login_page.wait_overlay_hide()
        login_page.click_button_login()
        main_page.wait_overlay_hide()
        main_page.click_button_personal_account()
        personal_account_page.wait_overlay_hide()
        personal_account_page.click_hyperlink_order_history()
        personal_account_page.check_current_page_order_history()

    def test_click_hyperlink_exit(self,driver,open_login_page,main_page,login_page,personal_account_page,body_user):
        body = body_user
        email = body['email']
        password = body['password']
        login_page.wait_overlay_hide()
        login_page.write_email(email)
        login_page.write_password(password)
        login_page.wait_overlay_hide()
        login_page.click_button_login()
        main_page.wait_overlay_hide()
        main_page.click_button_personal_account()
        personal_account_page.wait_overlay_hide()
        personal_account_page.click_hyperlink_exit()
        personal_account_page.check_current_login_page()

