from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from behave import fixture, use_fixture

from app.application import Application
from support.logger import logger


# Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    #     "clientHints": {"platform": "Android", "mobile": True}
    # }
    #
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Initialize WebDriver with options
    # context.driver = webdriver.Chrome(options=chrome_options)
    #
    # # Set up browser settings
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.wait = WebDriverWait(context.driver, timeout=15)
    #
    # # Assume 'Application' is a custom class to manage your app's pages
    # context.app = Application(context.driver)  # access to main_page, header, search_result_page

    ### IN THE EVENT OF FIREFOX ONLY TESTS ###
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--window-size=1920,1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #    options=options,
    #   service=service
    # )

    ### BROWSERS WITH DRIVERS: provide pathto the driver file ###
    # service = Service(executable_path='/Users/cesip/python-selenium-automation/geckodriver.exe'
    # context.driver = webdriver.Firefox(service=service)

    ### IN THE EVENT OF SAFARI ONLY TESTS: MAC OS ONLY ###
    # context.driver = webdriver.Safari()

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # Documentation https://www.browserstack.com/docs/automate/selenium/select-browsers-and-devices#Legacy_Integration
    # bs_user = 'charles_mh6rSj'
    # bs_key = 'VeMdA4R28ndDtbpZGFir'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Sonoma',
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ### BROWSERSTACK MOBILE OPTIONS ###
    bs_user = 'charles_mh6rSj'
    bs_key = 'VeMdA4R28ndDtbpZGFir'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # Capabilities for BrowserStack and mobile device
    bstack_options = {
        'osVersion': '11.0',  # Android version
        'deviceName': 'Google Pixel 4',  # Device name
        'realMobile': 'true',  # Indicate testing on a real device
        'projectName': 'Mobile Testing Project',
        'buildName': 'Mobile Build',
        'sessionName': scenario_name
    }

    # Set up options for Chrome (or the desired browser)
    options = Options()
    options.set_capability('bstack:options', bstack_options)
    options.set_capability('browserName', 'chrome')  # Set browser to Chrome
    options.set_capability('browserstack.debug', 'true')  # Enable debug logs

    # Initialize WebDriver for BrowserStack remote server
    context.driver = webdriver.Remote(command_executor=url, options=options)

    ### THESE CONFIGURATIONS NOT TIED TO ANY BROWSER OR MOBILE BUT ARE GLOBAL ###
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)  # access to main_page, header, search_result_page


def before_scenario(context, scenario):
    """
    Setup actions before each scenario.
    :param context: Behave context
    :param scenario: Current scenario
    """
    # print('\nStarted scenario: ', scenario.name)
    scenario_name = scenario.name
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario_name)


def before_step(context, step):
    """
    Actions to perform before each step.
    :param context: Behave context
    :param step: Current step
    """
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    """
    Actions to perform after each step.
    :param context: Behave context
    :param step: Current step
    """
    if step.status == 'failed':
        print('\nStep failed: ', step)
        context.app.base_page.save_screenshot(step)


def after_scenario(context, scenario):
    """
    Cleanup actions after each scenario.
    :param context: Behave context
    :param scenario: Current scenario
    """
    if hasattr(context, 'driver'):
        context.driver.delete_all_cookies()
        context.driver.quit()
