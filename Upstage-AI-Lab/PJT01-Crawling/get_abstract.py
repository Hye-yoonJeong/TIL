import pandas as pd
import random
import abstracts_lemmatize as abst
import os

# os.mkdir(r'.\random_abstracts')
# os.mkdir(r'.\random_abstracts\text')

df_2023 = pd.read_csv('.\\urlList\\urlList2023.csv')
# print(df_2023.head())

random_seed = 42
random.seed(random_seed)
n = 10

rand_nums = random.sample(range(400), n)
print(rand_nums)

year = 2023

##### to directly crawl from each url
for i in range(n):
    url = df_2023.loc[rand_nums[i], 'url']
    abstract = abst.get_abstract(url)
    keywords_df = abst.analyse_abstract(abstract)
    keywords_df.to_csv(f'.\\random_abstracts\\keywords_{year}_{rand_nums[i]}.csv')


##### to test keyword extraction
##### open abstracts in saved in txt files
# for i in range(n):
#     file_path = rf'.\random_abstracts\text\{year}_{rand_nums[i]}.txt'
#     try :
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()
#         keywords_df = abst.analyse_abstract(text)
#         keywords_df.to_csv(f'.\\random_abstracts\\keywords_{year}_{rand_nums[i]}.csv')
        
#     except Exception as e :
#         print(f"Error opening file '{file_path}': {e}")