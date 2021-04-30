from django.urls import path

from .views import QuoteApiView, AuthorApiView, QuoteTagApiView, QuoteApiDetailView, QuoteApiNewView

urlpatterns = [
    path('quotes/', QuoteApiView.as_view(), name='quote_api'),
    path('author/', AuthorApiView.as_view(), name='author_api'),
    path('quote_tag/', QuoteTagApiView.as_view(), name='quote_tag_api'),
    path('quotes/<int:pk>/', QuoteApiDetailView.as_view(), name='quote_api_detail'),
    path('quotes/new/', QuoteApiNewView.as_view(), name='quote_api_new'),
]
