from selenium.webdriver.common.by import By


class LoginPageLocators:

    HYPERLINK_RESTORE_PASSWORD_LOCATOR = (By.XPATH, "//a[text()='Восстановить пароль']")
    FiELD_EMAIL = (By.XPATH, "//label[text()='Email']")
    FIELD_PASSWORD = (By.XPATH, "//label[text()='Пароль']")
    OVERLAY_LOCATOR = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    TEXT_EMAIL_LOCATOR = (By.NAME, "name")
    TEXT_PASSWORD_LOCATOR = (By.NAME, "Пароль")
    BUTTON_LOGIN_LOCATOR = (By.XPATH, "//button[text()='Войти']")

