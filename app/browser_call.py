import subprocess, shlex
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--kiosk')
options.add_argument('--incognito')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=options)

# if not use selenium
def call_browser(url):
    # chrome options
    # --kiosk: fullscreen mode
    # --incognito: secret mode (not use cache)
    # --disable-gpu: if not use this option in raspi, errors occurr
    cmd = 'chromium-browser ' + url + ' --incognito --disable-gpu'
    args = shlex.split(cmd)
    ret = subprocess.call(args)

def call_selenium_browser(url):    
    browser.get(url)

def close_window():
    browser.close()

def click_by_position(x, y) -> None:

    actions = ActionChains(browser)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
    whole_page = browser.find_element(By.TAG_NAME, "body")
    actions.move_to_element_with_offset(whole_page, 0, 0)

    # MOVE TO DESIRED POSITION THEN CLICK
    actions.move_by_offset(x, y)
    actions.click()

    actions.perform()