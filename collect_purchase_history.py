from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

def load_cookies_and_visit():
    driver = webdriver.Chrome()
    driver.get("https://www.showroom-live.com/")
    with open("cookies.txt", "r") as file:
        for line in file:
            name, value = line.strip().split(':')
            driver.add_cookie({"name": name, "value": value})
    driver.get("https://www.showroom-live.com/point/hist")
    
    data = []
    while True:
        # get table data
        time.sleep(2)  # wait for the website load
        rows = driver.find_elements(By.XPATH, '//table[@class="table-type-02 fs-b4"]/tbody/tr')
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            data.append([col.text for col in cols])

        # click next button
        next_page_link = driver.find_elements(By.LINK_TEXT, '次のページ»')
        if next_page_link:
            next_page_link[0].click()
        else:
            break

    # write csv
    with open('purchase_history.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['date/time', 'item', 'ShowGold', 'Who'])
        writer.writerows(data)

    driver.quit()

load_cookies_and_visit()
