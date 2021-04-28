from rest_framework import generics

from quotes.models import Quote, QuoteTag, Author

from .serializers import QuoteSerializer, AuthorSerializer


class QuoteApiView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class AuthorApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
