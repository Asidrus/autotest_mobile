import pytest


def pytest_addoption(parser):
    parser.addoption("--invisible", action='store_true', help="Run on virtual display")
    parser.addoption("--adaptive", action='store_true', help="Run as mobile user agent")
    parser.addoption("--local", action='store_true', help="Run on local machine")
    parser.addoption("--fn", type=str, help="Path of file")
    parser.addoption("--site", type=str, help="Url of site")
    parser.addoption("--parse", action='store_true', help="Parse site on urls")
    parser.addoption("--fDebug", action='store_true', help="Debug flag")


@pytest.fixture(scope='function')
def isLastTry(reruns, rerunInfo, data):
    if data in rerunInfo.keys():
        rerunInfo[data] = rerunInfo[data] + 1
    else:
        rerunInfo[data] = 0
    return reruns == rerunInfo[data]


@pytest.fixture(scope="session")
def setupDriver(request):
    opt = lambda o: request.config.getoption(o)
    # Driver = WebDriver(invisible=opt("--invisible"),
    #                    adaptive=opt("--adaptive"),
    #                    remote=not opt("--local"),
    #                    logs=True,
    #                    **request.param)
    # Driver.run()
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "12",
        # "app": "/home/kali/python/autotest_mobile/Система обучения АкадемСити_1.5.2_apkcombo.com.apk",
        "app": "./Система обучения АкадемСити_1.5.2_apkcombo.com.apk",
        "automationName": "UiAutomator2",
        # "appium:udid": "emulator-5556",
    }
    Driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    yield Driver
    del Driver