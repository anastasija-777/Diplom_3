from selenium import webdriver


class TestRestorePassword:

    def test_go_restore_password_page_through_button_log_in_account(self,driver,open_main_page,main_page,login_page,restore_password_page,create_user):
        main_page.wait_overlay_hide()
        main_page.click_button_log_in_account()
        login_page.wait_login_url()
        login_page.click_on_hyperlink_restore_password()
        restore_password_page.wait_login_url()
        restore_password_page.check_current_page_restore_password_page()

    def test_write_email_and_click_button_recover(self, driver, open_restore_password_page, restore_password_page, create_user):
        response = create_user
        response_json =  response.json()
        email = response_json['user']['email']
        restore_password_page.click_on_field_email()
        restore_password_page.write_email_in_field(email)
        restore_password_page.click_on_button_recover()
        restore_password_page.check_current_page_reset_password_page()

    def test_click_button_show_password_makes_field_active(self, driver, open_restore_password_page, restore_password_page,reset_password_page,create_user):
        response = create_user
        response_json = response.json()
        email = response_json['user']['email']
        restore_password_page.click_on_field_email()
        restore_password_page.write_email_in_field(email)
        restore_password_page.click_on_button_recover()
        reset_password_page.wait_reset_password_url()
        reset_password_page.click_button_show_password()
        reset_password_page.check_field_active()



