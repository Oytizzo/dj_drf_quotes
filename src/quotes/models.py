from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()


class QuoteTag(models.Model):
    tag_name = models.CharField(max_length=50)


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    quote_tag = models.ManyToManyField(QuoteTag)
