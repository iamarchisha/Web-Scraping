import os
from selenium import webdriver
from get_image_url import fetch_image_url
from persist_image import persist_image

def search_and_download(
    search_term:str,
    driver_path:str,
    target_path:str,
    number_images:int):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_url(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
     
    for elem in res:
        if elem is not None:
            persist_image(target_folder,elem)