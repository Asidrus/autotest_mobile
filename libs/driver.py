from appium import webdriver


class WebDriver:
    platformName: str
    platformVersion: str
    deviceName: str
    app: str

    IP: str = '127.0.0.1'
    Port: str = '4723'

    driver = None

    def __init__(self, **kwargs):
        """
        Generate driver
        @:param kwargs:
        @:param platformName: 'Android', 'IOS'
        @:param platformVersion: '12', '15.3'
        @:param deviceName: 'Pixel 5a'
        @:param app: 'app.apk' is default
        @:param IP: IP address for appium server
        @:param Port: Port for appium server
        """

        for key in kwargs.keys():
            if key == 'platformName':
                self.platformVersion = kwargs['platformName']
            elif key == 'platformVersion':
                self.platformVersion = kwargs['platformVersion']
            elif key == 'deviceName':
                self.deviceName = kwargs['deviceName']
            elif key == 'app':
                self.app = kwargs['app']
            elif key == 'IP':
                self.IP = kwargs['IP']
            elif key == 'Port':
                self.Port = kwargs['Port']

    def run(self):
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "11",
            "app": "/home/kali/python/autotest_mobile/Система обучения АкадемСити_1.5.2_apkcombo.com.apk",
            # "app": "./Система обучения АкадемСити_1.5.2_apkcombo.com.apk",
            "automationName": "UiAutomator2",
        }
        self.driver = webdriver.Remote(f"http://{self.IP}:{self.Port}/wd/hub",
                                       desired_capabilities=desired_capabilities)
