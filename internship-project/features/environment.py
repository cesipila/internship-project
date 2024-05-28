from allure_behave.formatter import AllureFormatter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


from app.application import Application
from support.logger import logger

# Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature


def browser_init(context):
#     """
#     :param context: Behave context
#     """

### IN THE EVENT OF CHROME ONLY TESTS ###
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

### IN THE EVENT OF FIREFOX ONLY TESTS ###
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

### BROWSERS WITH DRIVERS: provide pathto the driver file ###
# service = Service(executable_path='/Users/cesip/python-selenium-automation/geckodriver.exe'
# context.driver = webdriver.Firefox(service=service)

### IN THE EVENT OF SAFARI ONLY TESTS: MAC OS ONLY ###
# context.driver = webdriver.Safari()

### HEADLESS MODE ###
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# service = Service(ChromeDriverManager().install())
# context.driver = webdriver.Chrome(
#     options=options,
#     service=service
# )

### BROWSERSTACK ###
# Register for Browserstack, then grab it from https://www.browserstack.com/accounts/settings
# bs_user = 'add username'
# bs_key = 'add_key_fromsite'
# url = f'http://{bs_user}:{bs_key}@hub.browserstack.com/wd/hub'
#
# options = Options()
# bstack_options = {
#     'os' : 'Windows',
#     'osVersion' : '10',
#     'browserName' : 'Firefox',
#     'sessionName' : scenario_name
# }
# options.set_capability('bstack:options', bstack_options)
# context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    #print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        context.app.base_page.save_screenshot(step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
