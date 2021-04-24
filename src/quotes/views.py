from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Quote, QuoteTag, Author


class HomeView(ListView):
    template_name = 'quotes/home.html'
    model = Quote
