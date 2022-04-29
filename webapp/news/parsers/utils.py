import requests

from webapp.news.models import News
from webapp.db import db

def get_html(url):
    headers = {
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def save_news(title, url, pub):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, pub=pub)
        db.session.add(new_news)
        db.session.commit()