from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  
import os
from dotenv import load_dotenv

load_dotenv()

# Provide the path to the ChromeDriver executable
chrome_driver_path = "/usr/bin/chromedriver"  # Update this path if necessary

# Initialize the WebDriver without proxy settings
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://www.google.com")
    time.sleep(5)  # Increase sleep time to ensure the page loads

    # Check if the page title is correct
    print("Page title:", driver.title)

    # Check if the search box is present
    search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_box.send_keys("University Recruiter")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    try:
        # Find and click the "People" button
        people_button = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-pill--choice") and contains(@class, "search-reusables__filter-pill-button")]')
        driver.execute_script("arguments[0].click();", people_button)
        time.sleep(2)

        while True:
            connect_buttons = driver.find_elements(By.XPATH, '//button[contains(@class, "artdeco-button--2") and contains(@class, "artdeco-button--secondary")]')
            time.sleep(2)
            for button in connect_buttons:
                if button.text == "Connect":
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(2)
                    
                    # Click the "Send without a note" button to send the connection request without a note
                    send_now_button = driver.find_element(By.XPATH, '//button[@aria-label="Send without a note"]')
                    send_now_button.click()
                    time.sleep(2)
                    
                    print("Connection request sent")
                    time.sleep(2)
            time.sleep(2)
            
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next"]'))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(5)
            except (ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
                print(f"An error occurred while clicking the Next button: {e}")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

finally:
    driver.quit()