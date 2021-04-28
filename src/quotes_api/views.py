from rest_framework import generics

from quotes.models import Quote, QuoteTag, Author

from .serializers import QuoteSerializer, AuthorSerializer, QuoteTagSerializer


class QuoteApiView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class AuthorApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class QuoteTagApiView(generics.ListAPIView):
    queryset = QuoteTag.objects.all()
    serializer_class = QuoteTagSerializer
