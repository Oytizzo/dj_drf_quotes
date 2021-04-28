from rest_framework import serializers

from quotes.models import Quote, QuoteTag, Author


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
