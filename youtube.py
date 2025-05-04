from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

# Step 1: Open Shorts homepage
driver.get("https://www.youtube.com/shorts")

# Step 2: Click the first Shorts thumbnail
wait = WebDriverWait(driver, 15)
first_short = wait.until(EC.element_to_be_clickable((By.XPATH, '(//a[contains(@href, "/shorts/")])[1]')))
driver.execute_script("arguments[0].scrollIntoView();", first_short)
time.sleep(1)
first_short.click()

# Step 3: Wait for player to load
time.sleep(15)

# Step 4: Scroll slightly down to force video tag to load
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# Step 5: Mute and play the video via JS
driver.execute_script("""
    const video = document.querySelector('video');
    if (video) {
        video.muted = true;
        video.play().catch(err => console.log('Play error:', err));
    } else {
        console.log('Video not found');
    }
""")

# Step 6: Let it play
time.sleep(10)

driver.quit()

