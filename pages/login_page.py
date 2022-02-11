from pages.page import Page

from appium.webdriver.common.appiumby import By


class LoginPage(Page):
    nameLocator = 'android.widget.EditText'
    passwordLocator = 'android.widget.EditText'
    submitLocator = 'android.widget.Button'

    def login(self, login, password):
        self.sleep(5)
        self.driver.find_elements(By.CLASS_NAME, self.nameLocator)
        loginField = self.driver.find_elements(By.CLASS_NAME, self.nameLocator)[0]
        passwordField = self.driver.find_elements(By.CLASS_NAME, self.passwordLocator)[1]

        button = self.selectElement(self.driver.find_elements(By.CLASS_NAME, self.submitLocator),
                                    {'content-desc': 'войти'})

        self.fill(login, loginField)
        self.fill(password, passwordField)
        # self.click(button)
        button.click()
