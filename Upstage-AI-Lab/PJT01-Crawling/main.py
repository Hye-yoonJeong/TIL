import crawl_ICML as crawl
import os
import pandas as pd
import create_wordcloud as wc

# os.mkdir(r'.\urlList')
# os.mkdir(r'.\wordcloud')

years = [i for i in range(2020, (2023+1))]

path_urlList = '.\\urlList'

for year in years :
    # df = crawl.crawl_ICML(year)
    # df.to_csv(f'{path_urlList}\\urlList{year}.csv', index = False)
    
    df = pd.read_csv(f'{path_urlList}\\urlList{year}.csv')
    
    title_data = df['Title'].to_string()
    wc.create_wordcloud(title_data, f'ICML{year}')   
    