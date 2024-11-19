import pandas as pd

from wordcloud import WordCloud
from wordcloud import STOPWORDS

import matplotlib.pyplot as plt

# define stop words
stop_words = set(STOPWORDS)
exclude_words = {'learning', 'machine', 'via', 'model'}
stop_words.update(exclude_words)

def create_wordcloud(data, img_title) :
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stop_words).generate(data) 
    plt.figure(figsize=(10,5))
    plt.title(img_title)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    wordcloud.to_file(f'.\wordcloud\{img_title}.png')