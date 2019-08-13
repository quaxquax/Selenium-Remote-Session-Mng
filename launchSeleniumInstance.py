#!/home/quax/anaconda3/bin/python
import requests
from lxml import html
import os, base64, time, random, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options


if __name__ == '__main__':

    # session_id =''

    PROXY = "localhost:8080"
# Fill in as needed
    myUser=
    myUserPW=
    myURL=
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True

    options = Options()
#    options.headless = True
    options.headless = False

    firefox_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY
    }

    driver = webdriver.Firefox(options=options, capabilities=firefox_capabilities)
    executor_url = driver.command_executor._url  # pylint: disable=W0212
    session_id = driver.session_id
    print(executor_url)
    print(session_id)

    driver.get(myURL)

    time.sleep(random.triangular(1.5, 3.5))

    driver.find_element_by_id('username').send_keys(myUser)
    driver.find_element_by_id('password').send_keys(base64.b85decode(myUserPW).decode('ascii'))
    driver.find_element_by_xpath('//button[text()="Sign in"]').click()
    if driver.page_source.find("Adding a phone number") != -1:
        # Click
        skipButton = driver.find_element_by_xpath('//button[text()="Skip"]')
        skipButton.click()

    while(1):
        time.sleep(9999)
