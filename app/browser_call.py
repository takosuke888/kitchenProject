import subprocess, shlex
import sys
from selenium import webdriver

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