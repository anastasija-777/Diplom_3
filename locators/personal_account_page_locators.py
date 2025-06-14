from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    OVERLAY_LOCATOR = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    TEXT_PROFILE_LOCATOR = (By.XPATH, "//a[text()='Профиль']")
    HYPERLINK_ORDER_HISTORY_LOCATOR = (By.XPATH, "//a[text()='История заказов']")
    HYPERLINK_EXIT_LOCATOR = (By.XPATH, "//button[text()='Выход']")





