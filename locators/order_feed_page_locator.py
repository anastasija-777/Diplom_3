from selenium.webdriver.common.by import By


class OrderFeedPageLocator:

    OVERLAY_LOCATOR = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    TEXT_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']")
    BUTTON_CONSTRUCTOR_LOCATOR = (By.XPATH, '//a[.//p[normalize-space(text())="Конструктор"]]')
    ORDER_LOCATOR = (By.XPATH, '//a[@class = "OrderHistory_link__1iNby"]')
    MODAL_ORDER_LOCATOR = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
    NUMBER_NEW_ORDER_LOCATOR = (By.XPATH, '//p[@class = "text text_type_digits-default"]')
    COUNTER_TOTAL_ORDERS_LOCATOR = (By.XPATH, '//div[@class="undefined mb-15"]/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]')
    COUNTER_ORDERS_TODAY_LOCATOR = (By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]')
    NUMBER_ORDER_IN_PROGRESS = (By.XPATH,'//li[@class="text text_type_digits-default mb-2"]')