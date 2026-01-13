# automate_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random, string, time

def random_string(n=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# EDIT if your Laravel serve host/port is different
url = "http://127.0.0.1:8000/login"

# Use visible browser so you can watch it (remove options.add_argument to see)
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")   # uncomment only if you want headless
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get(url)
    wait = WebDriverWait(driver, 8)

    # Wait for possible email or username field
    email = None
    for selector in [(By.NAME, "email"), (By.ID, "email"), (By.CSS_SELECTOR, "input[type='email']"), (By.NAME, "username")]:
        try:
            email = wait.until(EC.presence_of_element_located(selector))
            break
        except:
            email = None

    password = None
    for selector in [(By.NAME, "password"), (By.ID, "password"), (By.CSS_SELECTOR, "input[type='password']")]:
        try:
            password = wait.until(EC.presence_of_element_located(selector))
            break
        except:
            password = None

    if email:
        email.clear()
        email.send_keys(f"{random_string(6)}@example.com")
    else:
        print("Email input not found - check the login page markup")

    if password:
        password.clear()
        password.send_keys(random_string(10))
    else:
        print("Password input not found - check the login page markup")

    # Optionally take a screenshot (saves in the same folder)
    time.sleep(0.5)
    driver.save_screenshot("login_page_screenshot.png")
    print("Saved screenshot: login_page_screenshot.png")
    time.sleep(1)
    
finally:
    driver.quit()
