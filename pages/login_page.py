from .page import Page


class LoginPage(Page):

    nameLocator = ''
    passwordLocator = ''
    submitLocator = ''

    def login(self, login, password):

        # self.fill(login, input=self.selectElement(self.findElements("//input"), self._name_))
        # self.fill(password, self.selectElement(self.findElements("//input"), self._password_))
        # self.click(self.selectElement(self.findElements("//button"), self._button_))