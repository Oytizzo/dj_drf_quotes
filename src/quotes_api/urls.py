from django.urls import path

from .views import QuoteApiView

urlpatterns = [
    path('', QuoteApiView.as_view(), name='quote_api_view'),
]
