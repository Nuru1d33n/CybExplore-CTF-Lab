from django.contrib import admin
from labs.models import LabCategory, LabTask, Progress, Comment

@admin.register(LabCategory)
class LabCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(LabTask)
class LabTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'flag', 'hint')
    list_filter = ('difficulty', 'category')
    search_fields = ('name', 'description', 'flag', 'hint')
    ordering = ('name',)
    readonly_fields = ('get_total_score',)  # Display the computed total score as readonly

    def get_total_score(self, obj):
        return obj.get_total_score()
    get_total_score.short_description = 'Total Score'

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'completed', 'completed_at', 'score')
    list_filter = ('completed', 'completed_at')
    search_fields = ('user__username', 'task__name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'created_at', 'content')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'task__name', 'content')
