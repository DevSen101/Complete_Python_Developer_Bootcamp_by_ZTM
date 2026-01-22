from selenium import webdriver
import time
chrome_browser = webdriver.Chrome()

chrome_browser.fullscreen_window()
# chrome_browser.maximize_window()
time.sleep(10)