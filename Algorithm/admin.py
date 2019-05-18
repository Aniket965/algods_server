from django.contrib import admin

# Register your models here.

from .models import Code,Category,Language,Algorithm

admin.site.register(Code)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Algorithm)