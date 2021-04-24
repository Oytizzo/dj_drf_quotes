from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()

    def __str__(self):
        return self.name


class QuoteTag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return  self.tag_name


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    quote_tag = models.ManyToManyField(QuoteTag)

    def __str__(self):
        return self.quote
