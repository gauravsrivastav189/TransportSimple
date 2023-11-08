from django.contrib import admin

from .models import Question, Answer, Like


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['body', 'question', 'author']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['answer', 'user']
