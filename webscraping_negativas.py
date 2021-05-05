from selenium import webdriver
import time
import wget
import requests

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

DRIVER_PATH = '/Users/javi/Documents/Python/Detector de pajaros/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://pixabay.com/es/images/search/fotos%20-bird%20%7C%20-birds%7C-ave%7C-aves/')


all_img = []
for i in range(2):
    images = driver.find_elements_by_class_name('photo-result-image')
    for i in images:
        url = i.get_attribute("src")
        if url[-3:] == 'gif':
            break
        all_img.append(url)
        print(url)
        #wget.download(url, './negativas/')
    
    button = driver.find_elements_by_class_name('pure-button')
    button[6].click()
    time.sleep(10)

print(all_img.__len__())    