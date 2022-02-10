import allure
import pytest
#
from config import logger, TELEGRAMBOT_IP, TELEGRAMBOT_PORT
from libs.network import Client
from libs.reporter import Reporter
# Test naming
suite_name = "Мобильное приложение android"
test_name = "Проверка формы log in"
severity = "Сritical"
#

rerunInfo = {}
reruns = 2 # добавить getoption


def pytest_generate_tests(metafunc):
    metafunc.parametrize("data", [i for i in range(3)])
    metafunc.parametrize("reruns, rerunInfo", [(reruns, rerunInfo)])


@allure.feature(suite_name)
@allure.story(test_name)
@allure.severity(severity)
@pytest.mark.flaky(reruns=reruns)
def test_formSending(request, setupDriver, data, isLastTry):
    driver = setupDriver


# from appium import webdriver
# # from appium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# 
# from time import sleep
# 
# 
# def findElementFromList(driver, className, attr, value):
#     elements = driver.find_elements(By.CLASS_NAME, className)
#     for element in elements:
#         if element.get_attribute(attr) == value:
#             return element
#     return None
# 
# 
# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "12",
#     # "deviceName": "Pixel 5 API 30",
#     "app": "/home/kali/python/autotest_mobile/Система обучения АкадемСити_1.5.2_apkcombo.com.apk",
#     "automationName": "UiAutomator2",
#     # "appium:udid": "emulator-5556",
#     # "appium:udid": "first_avd"
#     # "appium:udid": "em-1488",
# }
# 
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
# 
# sleep(5)
# driver.save_screenshot("screen1.png")
# inputs = driver.find_elements(By.CLASS_NAME, "android.widget.EditText")
# 
# login = inputs[0]
# password = inputs[1]
# button = findElementFromList(driver, 'android.widget.Button', 'content-desc', 'Войти')
# 
# login.click()
# sleep(0.1)
# login.send_keys("")
# 
# password.click()
# sleep(0.1)
# password.send_keys("")
# 
# sleep(0.1)
# button.click()
# sleep(5)
# driver.save_screenshot("screen2.png")
# driver.hide_keyboard()
# sleep(10)
