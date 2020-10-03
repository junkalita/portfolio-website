from django.contrib import admin
from .models import Blog,BlogCategory,ContactForm,Comment
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["blog_title", "blog_published"]}),
        ("URL", {'fields': ["slug"]}),
        ("Blog Category", {'fields': ["category"]}),
        ("Content", {"fields": ["blog_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogCategory)
admin.site.register(ContactForm)
admin.site.register(Comment)
