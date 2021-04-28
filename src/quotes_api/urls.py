from django.urls import path

from .views import QuoteApiView, AuthorApiView

urlpatterns = [
    path('', QuoteApiView.as_view(), name='quote_api_view'),
    path('author/', AuthorApiView.as_view(), name='author_api_view'),
]
