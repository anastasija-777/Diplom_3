from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    NUMBER_NEW_ORDER_LOCATOR = (By.XPATH, "//p[@class='text text_type_digits-default']")
    BUTTON_ORDER_FEED_LOCATOR = (By.XPATH, "//p[text()='Лента Заказов']")
