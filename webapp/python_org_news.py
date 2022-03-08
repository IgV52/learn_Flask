import requests
from bs4 import BeautifulSoup

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
            pud_date = news.find('time').text
            result_news.append({
                'title': title,
                'url': url,
                'pud_date': pud_date
            })
        return result_news
    return False

   
            
