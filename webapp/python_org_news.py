import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.news.models import News
from webapp.db import db

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_python_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_sity = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in news_sity:
            title = news.find('a').text
            url = news.find('a')['href']
            pub = news.find('time').text
            try:
                pub = datetime.strptime(pub, '%Y-%m-%d')
            except ValueError:
                pub = datetime.now()
            save_news(title, url, pub)

def save_news(title, url, pub):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, pub=pub)
        db.session.add(new_news)
        db.session.commit()
            
