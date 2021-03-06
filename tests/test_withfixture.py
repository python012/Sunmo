import time
from selenium.webdriver.common.by import By
import sys
sys.path.append('..')
from utils.log import logger


class TestBaiDu(object):

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def test_search_0(self, driver_fixture): # chrome_driver from /conftest.py
        logger.info("Sample log info: test_search_0 is launched now.")
        driver_fixture.find_element(*self.locator_kw).send_keys(u'selenium 测试')
        driver_fixture.find_element(*self.locator_su).click()
        time.sleep(2)
        links = driver_fixture.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self, driver_fixture):
        logger.info("Sample log info: test_search_1 is launched now.")
        driver_fixture.find_element(*self.locator_kw).send_keys('Python selenium')
        driver_fixture.find_element(*self.locator_su).click()
        time.sleep(2)
        links = driver_fixture.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)
