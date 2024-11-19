## 파이썬 Flask
> mkdir upstage-flask-backend_re
> cd upstage-flask-backend_re

### 가상환경 구축
> python -m venv .venv

### 가상환경 activate
### windows
>.venv\Scripts\activate

### requirements.txt 생성
> pip freeze > requirements.txt 

##### to test in future
> set lambda function to crawl all 400 abstracts of each year's conference
> utilize RDS to save crawled data in db
> from these crawled abstracts, extract keywords and create wordcloud
> compare wordclouds from titles vs. keywords
> try sending wordcloud images and keywords via slackbot