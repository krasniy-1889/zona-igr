from django.contrib import admin

from .forms import CommentModelAdminForm
from .models import Comment, GameDeveloper, Genre, Post, TorrentFile


# Inline models
class TorrentFileInline(admin.TabularInline):
    model = TorrentFile
    extra = 1


# Models
@admin.register(GameDeveloper)
class GameDeveloperAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "developer",
        "voiceover_language",
        "interface_language",
    ]
    filter_horizontal = ["genres"]
    inlines = [TorrentFileInline]
    show_full_result_count = False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentModelAdminForm
    list_display = ["id", "post", "user", "parent_id", "created_at"]
    search_fields = ["post__title", "user__username"]
    ordering = ["-id"]

    list_select_related = ["post", "user"]
    show_full_result_count = False

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request
        return form
