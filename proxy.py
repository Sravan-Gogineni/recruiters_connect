import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
import time  
from dotenv import load_dotenv

load_dotenv()

# Define the proxy
proxy = "149.28.32.205:25936"

# Configure Chrome options to use the proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy}')

# Provide the path to the ChromeDriver executable
chrome_driver_path = "/usr/bin/chromedriver"  # Update this path if necessary

# Initialize the WebDriver with the proxy settings
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("http://www.google.com")
    time.sleep(5)  # Increase sleep time to ensure the page loads

    # Check if the page title is correct
    print("Page title:", driver.title)

    # Check if the search box is present
    search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_box.send_keys("LinkedIn")
    search_box.submit()
    time.sleep(5)
    
    # Check if LinkedIn link is present
    linked_in = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[12]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
    linked_in.click()
    time.sleep(2)
    
    sign_in = driver.find_element(By.XPATH, '/html/body/nav/div/a[2]')
    sign_in.click()
    time.sleep(3)
    
    email = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
    email.send_keys("johnabhraham286@gmail.com")
    time.sleep(4)
    
    password = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
    pass_key = os.getenv("pass")
    password.send_keys(pass_key)
    time.sleep(6)
    
    sign_in_button = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[4]/button')
    sign_in_button.click()
    time.sleep(5)
    
    search = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__collapsed-search-button')
    search.click()
    time.sleep(2)

    search_box = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
    search_box.send_keys("University Recruiter")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    try:
        people = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li[3]/button')
        driver.execute_script("arguments[0].click();", people)
        time.sleep(5)

        connect_buttons = driver.find_elements(By.XPATH, '//button[contains(@class, "artdeco-button--2") and contains(@class, "artdeco-button--secondary")]')
        time.sleep(2)
        for button in connect_buttons:
            if button.text == "Connect":
                driver.execute_script("arguments[0].click();", button)
                time.sleep(2)
                
                # Click the "Send without a note" button to send the connection request without a note
                send_now_button = driver.find_element(By.XPATH, '//button[@aria-label="Send without a note"]')
                driver.execute_script("arguments[0].click();", send_now_button)
                time.sleep(2)
                
                print("Connection request sent")

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()