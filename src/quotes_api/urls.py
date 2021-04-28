from django.urls import path

from .views import QuoteApiView, AuthorApiView, QuoteTagApiView

urlpatterns = [
    path('', QuoteApiView.as_view(), name='quote_api'),
    path('author/', AuthorApiView.as_view(), name='author_api'),
    path('quote_tag/', QuoteTagApiView.as_view(), name='quote_tag_api'),
]
