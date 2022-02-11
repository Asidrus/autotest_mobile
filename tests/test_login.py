import allure
import pytest
#
from pages.login_page import LoginPage
from credentials import SDO_LOGIN, SDO_PASSWORD
# Test naming
suite_name = "Мобильное приложение android"
test_name = "Проверка формы log in"
severity = "Сritical"
#

rerunInfo = {}
reruns = 0 # добавить getoption


def pytest_generate_tests(metafunc):
    metafunc.parametrize("data", ['once'])
    metafunc.parametrize("headers", [{"Test": test_name}])
    metafunc.parametrize("reruns, rerunInfo", [(reruns, rerunInfo)])
    metafunc.parametrize("setupDriver", [{
        "app": "./Система обучения АкадемСити_1.5.2_apkcombo.com.apk",
    }], indirect=True)


@allure.feature(suite_name)
@allure.story(test_name)
@allure.severity(severity)
@pytest.mark.flaky(reruns=reruns)
def test_login(request, setupDriver, reporter, data, isLastTry):
    driver = setupDriver
    with reporter.allure_step('Инициализация драйвера', True, False, True, isLastTry):
        page = LoginPage(driver)
    with reporter.allure_step('Вход в личный кабинет', True, False, True, isLastTry):
        page.login(SDO_LOGIN, SDO_PASSWORD)
