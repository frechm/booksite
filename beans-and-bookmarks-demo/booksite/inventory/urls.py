from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    
]

