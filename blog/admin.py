from django.contrib import admin
from blog.models import Post, Tag


class AdminPost(admin.ModelAdmin):
    last_display = ("title", "admin_img", "author")
    readonly_fields = ("admin_img", "created", "updated", "views")
    list_filter = ("author", "tags")
    search_fields = ("title", "short_desc", "tags")
    # fieldsets = ((None, {"fields": ("admin_img", "title", "author", "tags", "created", "updated", "views")}),)


admin.site.register(Post, AdminPost)
admin.site.register(Tag)
