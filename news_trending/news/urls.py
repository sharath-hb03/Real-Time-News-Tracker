# news/urls.py
from django.urls import path
from .views import fetch_trending_news, fetch_subtopic_news

urlpatterns = [
    path('', fetch_trending_news, name='home'),  # Home page shows 15 trending news
    path('news/<str:subtopic>/', fetch_subtopic_news, name='subtopic_news'),  # Subtopic pages
]
