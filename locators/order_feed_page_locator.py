from selenium.webdriver.common.by import By


class OrderFeedPageLocator:

    OVERLAY_LOCATOR = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    BUTTON_CONSTRUCTOR_LOCATOR = (By.XPATH, '//a[.//p[normalize-space(text())="Конструктор"]]')
    ORDER_LOCATOR = (By.XPATH, '//a[@class = "OrderHistory_link__1iNby"]')
    MODAL_ORDER_LOCATOR = (By.XPATH, '//div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')