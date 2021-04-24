from django.contrib import admin

from .models import Quote, QuoteTag, Author

admin.site.register(Quote)
admin.site.register(QuoteTag)
admin.site.register(Author)
