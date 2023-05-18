import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_presence(self, selector, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((selector, text))
        )

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger

    def go_to(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def scroll_page(self, height):
        self.driver.execute_script(f"window.scrollBy(0,{height});")
