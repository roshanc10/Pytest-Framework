import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
driver = None
options = Options()
options.add_argument("start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--headless')              ###optional
options.add_argument("--disable-notifications")
path=r'C:\Users\Abhishek\Desktop\1roshan\pytest_selenium\chromedriver_win32_83\chromedriver.exe'

@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    #driver.get("http://demoqa.com/automation-practice-form")
    driver.get("http://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()

@pytest.fixture(params=[{"userid": "user", "userpass": "password"}])
def getDatacred(request):
    return request.param

'''
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
'''