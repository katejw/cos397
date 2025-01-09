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
base_url = "https://entertain.naver.com/ranking"
driver.get(base_url)

def extract(soup):
    ranking = soup.find('ul', {'id': 'ranking_list'})
    articles = ranking.find_all('li')[:5]
    results = []
    for i, article in enumerate(articles, start=1):
        title_area = article.find('div', {'class': 'tit_area'})
        if title_area:
            title = title_area.get_text(strip=True)
        else:
            title = "no title found"
        
        link_area = article.find('a', {'class': 'thumb_area'})
        if link_area and 'href' in link_area.attrs:
            link = link_area['href']
            full_url = link
            results.append((i, title, full_url))
        else:
            results.append((i, title, "no link found"))
    return results


with open('top_articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Rank', 'Title', 'URL'])

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    today_results = extract(soup)
    for rank, title, url in today_results:
        writer.writerow(['Today', rank, title, url])

    for day in range(1, 3650):
        try:
            prev_date = datetime.now() - timedelta(days=day)
            date = prev_date.strftime('%Y-%m-%d')

            prev_day_link = driver.find_element(By.CSS_SELECTOR, f".pagenavi_day a[data-day='{date}']")

            prev_day_link.click()
            time.sleep(1)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            previous_results = extract(soup)
            for rank, title, url in previous_results:
                writer.writerow([f"Day -{day}", rank, title, url])
        except Exception as e:
            print(f"error for prev day {day}: {e}")

driver.quit()
