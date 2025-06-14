import allure
from selenium import webdriver


class TestMainFunctionality:

    @allure.title('Проверяем переход по клику на кнопку «Лента заказов»')
    def test_switching_to_order_feed_page(self,driver,
                                          open_main_page,
                                          main_page,
                                          order_feed_page):
        with allure.step('Ждем когда исчезнет оверлей'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Лента заказов"'):
            main_page.click_button_order_feed()
        with allure.step('Ждем когда исчезнет оверлей'):
            order_feed_page.wait_overlay_hide()
        with allure.step('Проверяем появление заголовка "Лента заказов"'):
            assert order_feed_page.check_title_order_feed


    @allure.title('Проверяем переход по клику на кнопку «Конструктор»')
    def test_switching_to_main_page_by_button_constructor(self,driver,
                                                          open_order_feed_page,
                                                          main_page,
                                                          order_feed_page):
        with allure.step('Ждем когда исчезнет оверлей'):
            order_feed_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке Конструктор'):
            order_feed_page.click_button_constructor()
        with allure.step('Ждем когда исчезнет оверлей'):
            main_page.wait_overlay_hide()
        with allure.step('Проверяем появление текста "Соберите бургер" на главной странице'):
            assert main_page.check_current_text_assemble_burger

    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient_fluorescent_bun_shows_ingredient_details(self, driver,
                                                                          open_main_page,
                                                                          main_page):
        with allure.step('Ждем когда исчезнет оверлей'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем на ингредиент "Флюоресцентная булка"'):
            main_page.click_ingredient_fluorescent_bun()
        with allure.step('Проверяем появление окна с деталями ингредиента'):
            assert main_page.check_modal_ingredient_details

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_click_on_cross_button_close_page_ingredient_details(self, driver,
                                                                 open_main_page,
                                                                 main_page):
        with allure.step('Ждем когда исчезнет оверлей'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем на ингредиент "Флюоресцентная булка"'):
            main_page.click_ingredient_fluorescent_bun()
        with allure.step('Закрываем окно с деталями ингредиента кликая на крестик'):
            main_page.click_cross_button()
        with allure.step('Проверяем что окно с деталями ингредиента закрывается при нажатии на крестик'):
            assert main_page.check_close_modal_ingredient_details

    @allure.title('Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_after_drag_and_drop_ingredient_counter_increases(self, driver,
                                                              open_main_page,
                                                              main_page):
        with allure.step('Перетаскиваем ингредиента Соус Spicy-X в поле "Перетяните булочку сюда (верх)"'):
            main_page.drag_and_drop_ingredient_sauce_spicy_x()
        with allure.step('Проверяем что Соус Spicy-X появился в заказе'):
            assert main_page.check_add_ingredient_sauce_spicy_x

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ.')
    def test_logged_in_user_can_place_an_order(self, driver,
                                               open_login_page,
                                               main_page,
                                               login_page,
                                               body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем когда исчезнет оверлей'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем когда исчезнет оверлей'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Войти"'):
            login_page.click_button_login()
        with allure.step('Ждем когда исчезнет оверлей'):
            main_page.wait_overlay_hide()
        with allure.step('Перетаскиваем ингредиента Флюоресцентная булка в поле "Перетяните булочку сюда (верх)"'):
            main_page.drag_and_drop_fluorescent_bun()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            main_page.click_button_place_an_order()
        with allure.step('Проверяем появление номера заказа в появившемся окне'):
            assert main_page.check_visible_text_order_id




