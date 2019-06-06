from django.contrib import admin

# Register your models here.
from blog.models import NewReporter, NewArticle

admin.site.register(NewReporter)
admin.site.register(NewArticle)
