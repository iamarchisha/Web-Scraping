import selenium
import os
from selenium import webdriver

# Put the path for your ChromeDriver here
DRIVER_PATH = os.path.join('./Web-Scraping/Driver','chromedriver.exe')
wd = webdriver.Chrome(executable_path= DRIVER_PATH)


from search_and_download import search_and_download

search_term = "flower"
search_and_download(
    search_term = search_term,
    driver_path = DRIVER_PATH,
    target_path = os.path.join('./Web-Scraping','images'),
    number_images = 10
)