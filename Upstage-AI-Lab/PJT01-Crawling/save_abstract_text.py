import pandas as pd
import random
import abstracts_lemmatize as abst

df_2023 = pd.read_csv('.\\urlList\\urlList2023.csv')

random_seed = 42
random.seed(random_seed)
n = 10

rand_nums = random.sample(range(400), n)

year = 2023

for i in range(n):
    url = df_2023.loc[rand_nums[i], 'url']
    abstract = abst.get_abstract(url)
    
    file_path = f'.\\random_abstracts\\text\\{year}_{rand_nums[i]}.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(abstract)