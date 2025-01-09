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

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

with open("character_f.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    urls = []
    next(csv_reader)
    for row in csv_reader:
        url = row[1]
        urls.append(url)

def scrape_text(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    
    try:
        driver.get(url)
        time.sleep(3)
        content_div = driver.find_element(By.CLASS_NAME, "_article_content")
        return content_div.text
    except Exception as e:
        print(f"error scraping {url}: {e}")
        return None
    finally:
        driver.quit()

with open("character_drugs_f.txt", "w", newline="", encoding="utf-8") as txtfile:
    csv_writer = csv.writer(txtfile)
    csv_writer.writerow(["Content"])
    for url in urls:
        article_text = scrape_text(url)
        if article_text:
            csv_writer.writerow([article_text])
