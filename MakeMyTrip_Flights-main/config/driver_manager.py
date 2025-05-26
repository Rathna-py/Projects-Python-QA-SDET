from selenium import webdriver

driver = webdriver.Chrome()


def close_driver():
    driver.close()
