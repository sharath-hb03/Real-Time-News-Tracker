# news/views.py
import requests
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

API_KEY = ''  # Replace with your actual API key

def fetch_trending_news(request):
    # Get the current time and calculate the time 24 hours ago
    from_time = timezone.now() - timedelta(hours=24)
    from_time = from_time.isoformat()

    # Fetch 15 general trending news articles for the homepage
    url = f'https://newsapi.org/v2/everything?q=trending&from={from_time}&sortBy=publishedAt&apiKey={API_KEY}'
    
    response = requests.get(url)
    news_data = response.json()
    trending_articles = news_data.get('articles', [])[:15]  # Limit to 15 articles
    
    return render(request, 'news/home.html', {'trending_articles': trending_articles})

# news/views.py

def fetch_subtopic_news(request, subtopic):
    from_time = timezone.now() - timedelta(hours=24)
    from_time = from_time.isoformat()

    url = f'https://newsapi.org/v2/everything?q={subtopic}&from={from_time}&sortBy=publishedAt&apiKey={API_KEY}'
    
    response = requests.get(url)
    news_data = response.json()
    subtopic_articles = news_data.get('articles', [])[:6]  # Limit to 5 articles

    return render(request, 'news/subtopic_news.html', {'articles': subtopic_articles, 'subtopic': subtopic})
 
