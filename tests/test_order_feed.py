import allure
from selenium import webdriver


class TestOrderFeed:

    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_appears_window_with_details(self,driver,
                                                     open_order_feed_page,
                                                     order_feed_page):
        with allure.step('Кликаем на заказ из Ленты заказов'):
            order_feed_page.click_order()
        with allure.step('Проверяем что откроется всплывающее окно с деталями'):
            assert order_feed_page.check_appears_window_with_details

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_create_order_is_displayed_in_order_history_and_order_feed(self, driver,
                                                                       open_login_page,
                                                                       main_page,
                                                                       login_page,
                                                                       personal_account_page,
                                                                       order_history_page,
                                                                       order_feed_page,
                                                                       body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Войти"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Перетаскиваем ингредиента Флюоресцентная булка в поле "Перетяните булочку сюда (верх)"'):
            main_page.drag_and_drop_fluorescent_bun()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            main_page.click_button_place_an_order()
        with allure.step('Находим номер заказа'):
            main_page.wait_visible_number_order()
        with allure.step('Кликаем на крестик для закрытия страницы с номером заказа'):
            main_page.click_cross_button()
        with allure.step('Кликаем на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()
        with allure.step('Ожидаем когда оверлей исчезнет'):
            personal_account_page.wait_overlay_hide()
        with allure.step('Кликаем на гиперссылку "История заказов"'):
            personal_account_page.click_hyperlink_order_history()
        with allure.step('Находим номер заказа, к-ый создали на странице "История заказов"'):
            element_order_history = order_history_page.find_number_order()
            number_order_history = element_order_history.text
        with allure.step('Кликаем на кнопку Лента Заказов'):
            order_history_page.click_button_order_feed()
        with allure.step('Находим номер заказа, к-ый создали на странице "Лента заказов"'):
            element_order_feed = order_feed_page.find_number_order()
            number_order_feed = element_order_feed.text
        with allure.step('Проверяем, что номер заказа на странице "История заказов" и на странице "Лента заказов" совпадают'):
            assert number_order_history == number_order_feed


    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_total_orders_after_create_new_order_increase(self, driver,
                                                                       open_login_page,
                                                                       main_page,
                                                                       login_page,
                                                                       order_feed_page,
                                                                       body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем на кнопку Лента Заказов'):
            main_page.click_button_order_feed()
        with allure.step('Ждем когда оверлей исчезнет'):
            order_feed_page.wait_overlay_hide()
        with allure.step('Находим число сколько выполнено заказов за все время'):
            element = order_feed_page.counter_total_orders()
            total_orders = element.text
        with allure.step('Кликаем по кнопке "Конструктор" для перехода на главную страницу'):
            order_feed_page.click_button_constructor()
        with allure.step('Перетаскиваем ингредиента Флюоресцентная булка в поле "Перетяните булочку сюда (верх)"'):
            main_page.drag_and_drop_fluorescent_bun()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            main_page.click_button_place_an_order()
        with allure.step('Находим номер заказа'):
            main_page.wait_visible_number_order()
        with allure.step('Кликаем на крестик для закрытия страницы с номером заказа'):
            main_page.click_cross_button()
        with allure.step('Кликаем на кнопку Лента Заказов'):
            main_page.click_button_order_feed()
        with allure.step('Находим число сколько выполнено заказов за все время'):
            new_element = order_feed_page.counter_total_orders()
            new_total_orders = new_element.text
        with allure.step('Проверяем, что число сколько выполнено за все время заказов увеличилось на один'):
            assert int(total_orders) < int(new_total_orders)

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_orders_today_after_create_new_order_increase(self, driver,
                                                                 open_login_page,
                                                                 main_page,
                                                                 login_page,
                                                                 order_feed_page,
                                                                 body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Кликаем на кнопку Лента Заказов'):
            main_page.click_button_order_feed()
        with allure.step('Ждем когда оверлей исчезнет'):
            order_feed_page.wait_overlay_hide()
        with allure.step('Находим число сколько выполнено заказов за сегодня'):
            element = order_feed_page.counter_orders_today()
            orders_today = element.text
        with allure.step('Кликаем по кнопке "Конструктор" для перехода на главную страницу'):
            order_feed_page.click_button_constructor()
        with allure.step('Перетаскиваем ингредиента Флюоресцентная булка в поле "Перетяните булочку сюда (верх)"'):
            main_page.drag_and_drop_fluorescent_bun()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            main_page.click_button_place_an_order()
        with allure.step('Находим номер заказа'):
            main_page.wait_visible_number_order()
        with allure.step('Кликаем на крестик для закрытия страницы с номером заказа'):
            main_page.click_cross_button()
        with allure.step('Кликаем на кнопку Лента Заказов'):
            main_page.click_button_order_feed()
        with allure.step('Находим число сколько выполнено заказов за сегодня'):
            new_element = order_feed_page.counter_orders_today()
            new_orders_today = new_element.text
        with allure.step('Проверяем, что число сколько выполнено за все время заказов увеличилось на один'):
            assert int(orders_today) < int(new_orders_today)

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_after_create_new_order_add_in_progress_section(self, driver,
                                                                 open_login_page,
                                                                 main_page,
                                                                 login_page,
                                                                 order_feed_page,
                                                                 body_user):
        with allure.step('Создаем нового пользователя'):
            body = body_user
        with allure.step('Получаем email пользователя из ответа на запрос "Создание пользователя"'):
            email = body['email']
        with allure.step('Получаем пароль пользователя из ответа на запрос "Создание пользователя"'):
            password = body['password']
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Пишем в поле Email адрес электронной почты'):
            login_page.write_email(email)
        with allure.step('Пишем в поле Пароль пароль созданного пользователя'):
            login_page.write_password(password)
        with allure.step('Ждем пока оверлей станет невидимым'):
            login_page.wait_overlay_hide()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            login_page.click_button_login()
        with allure.step('Ждем пока оверлей станет невидимым'):
            main_page.wait_overlay_hide()
        with allure.step('Перетаскиваем ингредиента Флюоресцентная булка в поле "Перетяните булочку сюда (верх)"'):
            main_page.drag_and_drop_fluorescent_bun()
        with allure.step('Кликаем по кнопке "Оформить заказ"'):
            main_page.click_button_place_an_order()
        with allure.step('Находим номер заказа'):
            element = main_page.wait_visible_number_order()
            number_order = element.text
        with allure.step('Кликаем на крестик для закрытия страницы с номером заказа'):
            main_page.click_cross_button()
        with allure.step('Кликаем на кнопку Лента Заказов'):
            main_page.click_button_order_feed()
        with allure.step('Ждем когда оверлей исчезнет'):
            order_feed_page.wait_overlay_hide()
        with allure.step('Находим наш номер заказа в разделе "В работе"'):
            element = order_feed_page.counter_orders_today()
            number_order_in_progress = element.text
        with allure.step('Проверяем что созданный заказ появился в разделе "В работе"'):
            assert number_order == number_order_in_progress











