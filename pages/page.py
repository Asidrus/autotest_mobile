from appium.webdriver.common.by import By
from time import sleep


class Page:
    """
    base class for POM
    """
    driver = None

    TIMEOUT = 5
    STEPTIME = .5

    def __init__(self, driver) -> None:
        self.driver = driver

    def __data2xpath__(self, data):
        if type(data) == dict:
            tag = data["tag"] if "tag" in data.keys() else "*"
            attrib = {}
            if "attrib" in data.keys():
                attrib = data["attrib"]
            else:
                for key in data.keys():
                    if key != "tag":
                        attrib[key] = data[key]
        elif type(data) == list:
            tag = ""
            attrib = {}
            for item in data:
                for key in item.keys():
                    if key == "tag":
                        tag = item[key]
                    else:
                        attrib[key] = item[key]
            tag = "*" if tag == "" else tag
        elif type(data) == str:
            return data
        else:
            raise TypeError(f"Не могу преобразовать {data=} типа {type(data)} к xpath")
        atts = ''
        for att in attrib:
            atts = atts + f" and @{att}='{attrib[att]}'"
        atts = '[' + atts[5:] + ']'
        return f"//{tag}{atts}"

    def attribute(self, elem, attrib):
        return elem.get_attribute(attrib)

    def sleep(self, time=self.STEPTIME):
        sleep(time)

    def findElement(self, xpath, element=None):
        xpath = self.__data2xpath__(xpath)
        if element:
            return WebDriverWait(self.driver, self.TIMEOUT, self.STEPTIME).until(
                lambda elem: element.find_element(By.XPATH, xpath))
        else:
            return WebDriverWait(self.driver, self.TIMEOUT, self.STEPTIME).until(
                lambda elem: self.driver.find_element(By.XPATH, xpath))

    def fill(self, text: str, input: object = None, xpath: str = None) -> None:
        """Typing the text into input field

        :@param text: text
        :@param input: input element
        "@param xpath: xpath of element
        """
        if input is None:
            if xpath is not None:
                input = self.findElement(self.__data2xpath__(xpath))
            else:
                raise Exception("Input или xpath не должны быть None")
        try:
            input.clear()
        except:
            Exception(f"Не удалось очистить поле {self.__data2xpath__(self.attributes(input))}, {input}")
        try:
            for symbol in text:
                self.sleep(.05)
                input.send_keys(symbol)
        except:
            Exception(
                f"Не удалось записать текст '{text}' в поле {self.__data2xpath__(self.attributes(input))}, {input}")

    def click(self, elem: object = None, xpath: str = None) -> None:
        if elem is None:
            if xpath is not None:
                elem = self.findElement(self.__data2xpath__(xpath))
            else:
                raise Exception("Elem или xpath не должны быть None")
        self.driver.execute_script(f"window.scrollTo(0, {elem.location['y'] - 400})")
        start = time()
        while time() - start < self.TIMEOUT:
            try:
                elem.click()
                return True
            except:
                sleep(self.STEPTIME)
        raise TimeoutError(f"Не удалось кликнуть на элемент {self.__data2xpath__(self.attributes(elem))}, {elem}")

    def selectElement(self, elements: list, pattern: dict):
        for arg in elements:
            for key in pattern.keys():
                attr = self.attribute(arg, key)
                if attr is not None:
                    if attr.lower() in pattern[key]:
                        return arg