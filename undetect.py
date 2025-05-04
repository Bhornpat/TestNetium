from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference('useAutomationExtension', False)
options.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0")

# Launch Firefox with these settings
driver = webdriver.Firefox(options=options)
driver.get("https://example.com")

