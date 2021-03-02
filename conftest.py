import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.8.131")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--base_url", action="store", default="http://demo.opencart.com")
    parser.addoption("--reference_url", action="store")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    mobile = request.config.getoption("--mobile")
    base_url = request.config.getoption("--base_url")
    reference_url = request.config.getoption("--reference_url")

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        # "screenResolution": "1280x720",
        "name": "Mikhail",
        'acceptSslCerts': True,
        "selenoid:options": {
            "enableVNC": True
        },
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {
            'args': []
        }
    }

    if browser == "chrome" and mobile:
        caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    driver.reference_url = reference_url
    driver.base_url = base_url

    if not mobile:
        driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
