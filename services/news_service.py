import requests
from config import Config

def get_news_data():
    url = f'https://newsapi.org/v2/everything?q=disaster&apiKey={Config.NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    
    # Process articles
    news_data = [{"title": article["title"], "url": article["url"]} for article in articles]
    
    return news_data
