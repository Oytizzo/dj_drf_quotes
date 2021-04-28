from rest_framework import generics

from quotes.models import Quote, QuoteTag, Author

from .serializers import QuoteSerializer


class QuoteApiView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
