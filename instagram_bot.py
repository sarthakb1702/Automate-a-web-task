from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "test.account2145"
PASSWORD = "mypass123"
TARGET_USER = "cbitosc"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.instagram.com/")
    wait = WebDriverWait(driver, 15)

    # Login
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    print(" Logged in")

    # Save Login Info popup
    try:
        save_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]"))
        )
        save_btn.click()
        print(" Clicked Save Login Info")
    except:
        print("ℹ Save Login Info popup not shown")

    # Notifications popup
    try:
        notif_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
        )
        notif_btn.click()
        print("Dismissed Notifications popup")
    except:
        print("ℹ No Notifications popup")

    # Go directly to profile
    driver.get(f"https://www.instagram.com/{TARGET_USER}/")
    time.sleep(5)

    # Follow account
    try:
        follow_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header//button[normalize-space()='Follow']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", follow_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", follow_btn)
        print("Followed the account using JS click")
    except:
        print("ℹ Already following or Follow button not clickable")

    # Extract profile stats
    profile_info = {}
    try:
        stat_labels = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//header//ul/li")
        ))
        if len(stat_labels) >= 3:
            profile_info["Posts"] = stat_labels[0].text.split('\n')[0]
            profile_info["Followers"] = stat_labels[1].text.split('\n')[0]
            profile_info["Following"] = stat_labels[2].text.split('\n')[0]
        else:
            profile_info["Posts"] = profile_info["Followers"] = profile_info["Following"] = "N/A"
        print("Extracted profile stats")
    except Exception as e:
        print(f" Could not extract stats: {e}")
        profile_info["Posts"] = profile_info["Followers"] = profile_info["Following"] = "N/A"

    # Save to text file
    with open("cbitosc_info.txt", "w", encoding="utf-8") as f:
        for k, v in profile_info.items():
            f.write(f"{k}: {v}\n")

    print("Stats saved to cbitosc_info.txt")

    time.sleep(10)

finally:
    driver.quit()
    print("Browser closed")
