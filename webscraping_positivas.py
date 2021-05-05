from selenium import webdriver
import time
import wget

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

DRIVER_PATH = '/Users/javi/Documents/Python/Detector de pajaros/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://ebird.org/media/catalog?view=List&mediaType=p&sort=obs_date_desc')

for i in range(10):
    show_more = driver.find_element_by_id('show_more')
    show_more.click()
    time.sleep(10)

all_img = driver.find_elements_by_tag_name('img')

current_photo = 0
for i in all_img:
    current_photo += 1
    print(current_photo)
    url = i.get_attribute("src")
    wget.download(url, './positivas/')
    print(url)
 

print(all_img.__len__())    