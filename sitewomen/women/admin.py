from django.contrib import admin
from .models import  Women, Category, TagPost, Husband


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", "cat")
    list_display_links = ("id", "title")
    ordering = ["time_create", "title"]
    list_editable = ("is_published", )
    list_filter = ("is_published", "time_create")
    search_fields = ("title", "content")
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ["id"]    




# admin.site.register(Women, WomenAdmin)

