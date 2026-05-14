from django.contrib import admin, messages
from .models import Women, Category, TagPost, Husband


class MarriedFilter(admin.SimpleListFilter):
    title = "Married"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("married", "Married"),
            ("not_married", "Not Married"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        elif self.value() == "not_married":
            return queryset.filter(husband__isnull=True)
        return queryset

    def queryset(self, request, queryset):
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        elif self.value() == "not_married":
            return queryset.filter(husband__isnull=True)
        return queryset


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = [ "title", "slug", "content", "cat", "husband", "tags", "is_published"]
    #readonly_fields = ["slug"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    #filter_vertical = ("tags",)
    exclude = ["time_create", "time_update"]
    list_display = ("title", "time_create", "is_published", "cat", "brief_info")
    list_display_links = ("title",)
    ordering = ["-time_create", "title"]
    list_editable = ("is_published",)
    search_fields = ["title", "cat__name"]
    list_filter = (MarriedFilter, "is_published", "cat")
    list_per_page = 10

    actions = ["set_published", "set_draft"]

    @admin.display(description="short info", ordering="content")
    def brief_info(self, women: Women):
        return f" Info about {len(women.content)} simbols"

    @admin.action(description="Set published")
    def set_published(self, request, queryset):
        queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(
            request, f"{queryset.count()} posts were successfully marked as published."
        )

    @admin.action(description="Set draft")
    def set_draft(self, request, queryset):
        queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(
            request,
            f"{queryset.count()} posts were successfully marked as draft.",
            messages.WARNING,
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ["id"]


# admin.site.register(Women, WomenAdmin)
