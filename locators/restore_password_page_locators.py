from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:

    FIELD_EMAIL_LOCATOR = (By.XPATH, "//label[text()='Email']")
    BUTTON_RECOVER_LOCATOR = (By.XPATH, "//button[text()='Восстановить']")
    TEXT_EMAIL_LOCATOR = (By.NAME, "name")
