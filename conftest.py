import datetime
import pytest
import logging
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.0.105")
    parser.addoption("--base_url", default="http://192.168.0.105:8081/", help="default ip")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")
    parser.addoption("--drivers", default="C:\\drivers\\", help="Path to drivers")
    parser.addoption("--remote", action="store_true", help="Run tests remoted")
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    headless = request.config.getoption("--headless")
    drivers_folder = request.config.getoption("--drivers")
    is_remote = request.config.getoption("--remote")
    version = request.config.getoption("--bv")

    executor_url = f"http://{executor}:4444/wd/hub"

    if is_remote:
        caps = {
            "browserName": browser,
            "BrowserVersion": version
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    else:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(
                executable_path=f"{drivers_folder}/chromedriver",
                options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=f"{drivers_folder}/geckodriver")
        elif browser == "MicrosoftEdge":
            driver = webdriver.Edge(executable_path=f"{drivers_folder}/msedgedriver")
        else:
            raise ValueError(f"Browser {browser} is not supported")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    driver.get(base_url)
    driver.base_url = base_url
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser, driver))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
