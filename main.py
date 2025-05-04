from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome browser
# driver = webdriver.Chrome()  # or provide path: Chrome(executable_path="path/to/chromedriver")
driver = webdriver.Firefox()  # or provide path: Chrome(executable_path="path/to/chromedriver")

# Open a website
driver.get("https://www.google.com")

# Find the search bar, enter a query and press Enter
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(3)

# Close the browser
driver.quit()

