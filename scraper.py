from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
from keys import *
from time import sleep

CHROME_DRIVER_PATH = get_chromedriver_path()


def print_course():
    options = ChromeOptions()
    options.add_argument('--headless')
    driver = Chrome(CHROME_DRIVER_PATH, options=options)
    wait = WebDriverWait(driver, 20)
    driver.get('https://idp.polito.it/idp/x509mixed-login')
    wait.until(presence_of_element_located((By.ID, 'j_username')))
    driver.find_element_by_id('j_username').send_keys(get_username())
    driver.find_element_by_id('j_password').send_keys(get_password())
    sleep(1)
    driver.find_element_by_id('usernamepassword').click()
    WebDriverWait(driver, 20).until(presence_of_element_located((By.XPATH, '//*[@id="table_portali"]/div[2]/div/a')))
    driver.find_element_by_xpath('//*[@id="table_portali"]/div[2]/div/a').click()
    try:
        popup = driver.find_element_by_xpath('//*[@id="myModalRemindAbb"]/div/div/div[3]/a[4]')
    except NoSuchElementException:
        pass
    else:
        popup.click()
    sleep(2)
    return driver.find_element_by_xpath('//*[@id="portlet_container"]/div[3]/div/table/tbody/tr[8]/td[2]/a').text