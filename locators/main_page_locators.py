from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_LOG_IN_ACCOUNT_LOCATOR = (By.XPATH, "//button[text()='Войти в аккаунт']")
    OVERLAY_LOCATOR = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    BUTTON_PERSONAL_ACCOUNT_LOCATOR = (By.XPATH, "//a[p[normalize-space()='Личный Кабинет']]")
    BUTTON_ORDER_FEED_LOCATOR = (By.XPATH, '//a[.//p[normalize-space(text())="Лента Заказов"]]')
    TEXT_ASSEMBLE_BURGER_LOCATOR = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_FLUORESCENT_BUN_LOCATOR = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    TEXT_INGREDIENT_DETAILS_LOCATOR = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CROSS_BUTTON_LOCATOR = (By.XPATH, "//section[1]/div[@class = 'Modal_modal__container__Wo2l_']/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    SAUCE_SPICY_X_LOCATOR = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    DRAG_THE_BUN_HERE_TOP = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")
    COUNTER_SAUCE_SPICY_X_LOCATOR = (By.XPATH, ".//span[contains(text(),'Соус Spicy-X')]")
    BUTTON_PLACE_AN_ORDER_LOCATOR = (By.XPATH, ".//button[text()='Оформить заказ']")
    TEXT_ORDER_ID_LOCATOR = (By.XPATH, ".//p[text()='идентификатор заказа']")






