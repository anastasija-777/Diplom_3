from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    BUTTON_SHOW_PASSWORD = (By.XPATH, "//*[contains(@class,'input__icon input__icon-action')]/*[(local-name()='svg')]")
    FIELD_PASSWORD_ACTIV = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")


