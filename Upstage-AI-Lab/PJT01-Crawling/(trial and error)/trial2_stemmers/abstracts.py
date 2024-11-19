import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')

def get_abstract(url) :
    time.sleep(3)
    
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(3)
    
    wait = WebDriverWait(browser, 60)
    wait.until(EC.presence_of_element_located((By.ID, 'abstractExample')))
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    abstract_element = soup.find('div', {'id': 'abstractExample'})
    
    if abstract_element.find('p') is not None :
        abstract = abstract_element.find('p').text.strip()
    else :
        abstract = abstract_element.text.strip()
        
    return abstract

def analyse_abstract(text) :
    pp_abstract = preprocess_text(text)
    keywords_abstract = get_main_keywords(pp_abstract)
    keywords_df = keywords_to_df(keywords_abstract)
    return keywords_df
    
    
def preprocess_text(text) :
    tokens = word_tokenize(text)
        
    stop_words = set(stopwords.words('english'))
    punctuations = {'.', ',', ':', ';', '?', '!', '(', ')'}
    exclude_words = {'abstract', 'via'}
    stop_words.update(punctuations, exclude_words)
    
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]
    
    
    # stemmer = PorterStemmer()
    # stemmer = LancasterStemmer()
    # stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    
    wnl = WordNetLemmatizer()
    lemmatized_tokens = [wnl.lemmatize(token) for token in filtered_tokens]
    
    # return stemmed_tokens
    return lemmatized_tokens

def get_main_keywords(tokens, n = 10) :
    freq_dist = FreqDist(tokens)
    main_keywords = freq_dist.most_common(n)
    return main_keywords

def keywords_to_df(keywords):
    df = pd.DataFrame(keywords, columns = ['keyword', 'frequency'])
    return df