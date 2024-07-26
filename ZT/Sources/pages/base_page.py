from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://passport.yandex.ru"
        self.login_field = (By.ID, "passp-field-login")
        self.password_field = (By.ID, "passp-field-passwd")
        self.sign_in_button = (By.XPATH, "//button[@type='submit']")
        self.password_recovery_link = (By.LINK_TEXT, "Вспомнить пароль")
        self.error_message = (By.XPATH, "//div[@data-t='error-message']")

    def load(self):
        self.browser.get(self.url)

    def login(self, username, password):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.login_field)).send_keys(username)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.sign_in_button)).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.password_field)).send_keys(password)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.sign_in_button)).click()

    def click_password_recovery(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.password_recovery_link)).click()

    def get_error_message(self):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.error_message)).text

    def get_page_source(self):
        return self.browser.page_source