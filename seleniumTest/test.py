from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import threading

# WebDriver configuration
chrome_driver_path = "PATHTOYOURDRIVER"
#chrome_driver_path = "/mnt/c/chromedriver-linux64/chromedriver"
chrome_options = Options()
service = Service(executable_path=chrome_driver_path)

# Available credentials
credentials = [
    ("admin", "admin"),
    ("johnd", "foo"),
    ("janed", "ddd")
]

def automate_browser(instance_id, username, password):
    # Configure Chrome browser with Selenium
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navigate to the login page
    driver.get("http://localhost:8080")
    
    # Wait for the page to fully load
    time.sleep(2)

    for x in range(10):  # Use a smaller number for quick tests
        # Locate the username and password fields
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Enter the credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[text()=' Login']")
        login_button.click()
        time.sleep(2)  # Wait for the page to redirect

        # Enter text in the new task field
        text_field = driver.find_element(By.XPATH, '//input[@placeholder="New task"]')
        text_field.send_keys(f"Task entry #{x}")

        # Simulate adding items
        add_button = driver.find_element(By.XPATH, "//button[text()='Add todo']")
        add_button.click()
        time.sleep(1)

        # Enter text in the new task field
        text_field = driver.find_element(By.XPATH, '//input[@placeholder="New task"]')
        text_field.send_keys(f"Anything {x}")

        # Simulate adding items
        add_button = driver.find_element(By.XPATH, "//button[text()='Add todo']")
        add_button.click()
        time.sleep(1)

        # Simulate deleting items
        delete_buttons = driver.find_elements(By.XPATH, "//button[@class='btn btn-danger']")
        if delete_buttons:
            delete_buttons[0].click()  # Click the first delete button found
        else:
            print("Delete button not found.")
        time.sleep(1)

        # Log out
        logout_button = driver.find_element(By.XPATH, "//button[text()='Logout']")
        logout_button.click()
        time.sleep(1)

# Number of instances
num_instances = 3

# Create and start threads
threads = []
for i in range(num_instances):
    username, password = credentials[i]
    thread = threading.Thread(target=automate_browser, args=(i, username, password))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
