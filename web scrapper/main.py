from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the web driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define the URL to scrape
url = 'https://example.com/articles'  # Replace with the actual URL you want to scrape

# Navigate to the webpage
driver.get(url)

# Wait for dynamic content to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'article-title'))  # Adjust the class name as needed
)

# Extract and print the titles of the articles
titles = driver.find_elements(By.CLASS_NAME, 'article-title')  # Adjust the class name as needed
for title in titles:
    print(title.text)

# Close the driver
driver.quit()
