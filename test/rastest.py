import sys
from selenium import webdriver

browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.google.com/')