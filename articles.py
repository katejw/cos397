from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime, timedelta
import csv

# set up chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# get urls to parse through
with open("character_f.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    urls = []
    next(reader)
    for row in reader:
        url = row[1]
        urls.append(url)

# scrape article content
def scrape_text(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    
    try:
        driver.get(url)
        time.sleep(3)
        content = driver.find_element(By.CLASS_NAME, "_article_content")
        return content.text
    except Exception as e:
        print(f"error scraping {url}: {e}")
        return None
    finally:
        driver.quit()

# put results in a txt file
with open("character_drugs_f.txt", "w", newline="", encoding="utf-8") as txtfile:
    writer = csv.writer(txtfile)
    writer.writerow(["Content"])
    for url in urls:
        text = scrape_text(url)
        if text:
            writer.writerow([text])
