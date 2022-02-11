import pytest

from libs.network import Client
from libs.driver import WebDriver
from libs.reporter import Reporter
from config import TELEGRAMBOT_IP, TELEGRAMBOT_PORT
from config import APPIUM_IP, APPIUM_PORT
from config import logger


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
    params = request.param if request.param is not None else {}
    Driver = WebDriver(IP=APPIUM_IP, Port=APPIUM_PORT, **params)
    Driver.run()
    yield Driver
    del Driver


@pytest.fixture(scope='function')
def reporter(request, headers):
    reporter = Reporter(header=headers,
                        logger=logger,
                        telegram=Client(TELEGRAMBOT_IP, TELEGRAMBOT_PORT),
                        debug=int(request.config.getoption("--fDebug")))
    yield reporter
    del reporter
