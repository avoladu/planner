from django.contrib import admin
from boards.models import *

class BoardAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    search_fields = ["title"]

class BoardColumnAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "board", "sort_index"]
    search_fields = ["title"]

class BoardCardAdmin(admin.ModelAdmin):
    list_display = ["id", "board", "column", "title", "sort_index"]
    search_fields = ["title"]

class BoardCardCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "card", "message"]

class BoardUserAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "board", "is_owner", "is_readonly"]

class BoardUserExecutorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "card"]
    search_fields = ["user"]


admin.site.register(Board, BoardAdmin)
admin.site.register(BoardColumn, BoardColumnAdmin)
admin.site.register(BoardCard, BoardCardAdmin)
admin.site.register(BoardCardComment, BoardCardCommentAdmin)
admin.site.register(BoardUser, BoardUserAdmin)
admin.site.register(BoardUserExecutor, BoardUserExecutorAdmin)
