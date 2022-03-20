from flask import Blueprint, current_app, render_template

from webapp.weather import weather_by_city
from webapp.news.models import News

blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    title = "Новости Python"
    weather = weather_by_city(current_app.config['COUNTRY'])
    news_list = News.query.order_by(News.pub.desc()).all()
    return render_template('news/index.html', page_title=title, weather=weather, news_list=news_list)