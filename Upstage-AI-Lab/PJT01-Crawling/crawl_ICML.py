from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd


def crawl_ICML(year) :
    url = f'https://icml.cc/virtual/{year}/papers.html'
    browser = webdriver.Chrome()
    
    browser.get(url)
    
    wait = WebDriverWait(browser, 60)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pp-card')))
    
    containers = browser.find_elements(By.CLASS_NAME, 'pp-card')
    
    data_list = []
    
    for container in containers :
        title = container.find_element(By.CLASS_NAME, 'card-title').text
        authors = container.find_element(By.CLASS_NAME, 'card-subtitle').text.split(',')
        poster_url = container.find_element(By.CLASS_NAME, 'pp-card-header').find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        data = {
            'Title' : title,
            'Authors' : authors,
            'url' : poster_url,
            'Keywords' : list()
        }
        
        data_list.append(data)
        
    df = pd.DataFrame(data_list)
    return df