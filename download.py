# Download file interacting with the page

from selenium import webdriver
from selenium.webdriver.common.by import By

def downloader(url, id_download_button):
    
    driver = webdriver.Chrome("./chromedriver76")
    driver.get(url)
    
    btn_download = driver.find_element(By.ID, id_download_button)
    btn_download.click()
    #driver.close()

with open("./list.txt") as f:
    while True:
        link = f.readline()
        downloader(link, 'dlbutton')
        if not link: break
