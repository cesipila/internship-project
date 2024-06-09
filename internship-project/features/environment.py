from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

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

    ### IN THE EVENT OF FIREFOX ONLY TESTS ###
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('--window-size=1920,1080')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
     #    options=options,
      #   service=service
    #)

    ### BROWSERS WITH DRIVERS: provide pathto the driver file ###
    # service = Service(executable_path='/Users/cesip/python-selenium-automation/geckodriver.exe'
    # context.driver = webdriver.Firefox(service=service)

    ### IN THE EVENT OF SAFARI ONLY TESTS: MAC OS ONLY ###
    # context.driver = webdriver.Safari()

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # Documentation https://www.browserstack.com/docs/automate/selenium/select-browsers-and-devices#Legacy_Integration
    bs_user = 'charles_mh6rSj'
    bs_key = 'VeMdA4R28ndDtbpZGFir'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Sonoma',
        'browserName': 'chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)  # access to main_page, header, search_result_page


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    scenario_name = scenario.name
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario_name)


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