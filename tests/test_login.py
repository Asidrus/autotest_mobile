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
        "app": "/app/app.apk",
    }], indirect=True)


@allure.feature(suite_name)
@allure.story(test_name)
@allure.severity(severity)
@pytest.mark.flaky(reruns=reruns)
def test_login(request, setupDriver, reporter, data, isLastTry):
    driver = setupDriver
    with reporter.allure_step('Инициализация драйвера', True, False, True, not isLastTry):
        page = LoginPage(driver)
        driver.save_screenshot("screen1.png")
    with reporter.allure_step('Вход в личный кабинет', True, False, True, not isLastTry):
        page.login(SDO_LOGIN, SDO_PASSWORD)
        driver.save_screenshot("screen2.png")
        # assert False
