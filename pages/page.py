from appium.webdriver.common.appiumby import By
from time import sleep, time


class Page:
    """
    base class for POM mobile testing
    """
    webdriver = None
    driver = None

    TIMEOUT = 5
    STEPTIME = .5

    def __init__(self, driver) -> None:
        self.webdriver = driver
        self.driver = driver.driver

    def attribute(self, elem, attrib):
        return elem.get_attribute(attrib)

    def sleep(self, timing=None):
        timing_ = .05 if timing is None else timing
        sleep(timing_)

    def selectElement(self, elements: list, pattern: dict):
        for element in elements:
            for key in pattern.keys():
                attr = self.attribute(element, key)
                if attr is not None:
                    if attr.lower() in pattern[key]:
                        return element

    def fill(self, text: str, input: object = None, xpath: str = None):

        try:
            input.click()
            self.sleep()
            input.send_keys(text)
            self.driver.hide_keyboard()
        except:
            Exception(f'Не удалось заполнить поле {input}')