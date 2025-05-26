from selenium import webdriver
import pytest
from utils.Loging import logger


@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome()
    logger.info("🚀..Launching Chrome..🚀")
    driver.maximize_window()
    request.cls.driver = driver
    driver.get("https://www.goindigo.in/")
    yield
    driver.quit()
    logger.info("🛑...Closing Chrome...🛑")


