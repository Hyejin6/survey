from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline] # Choice 모델 클레스 같이 보기

    list_filter = ['pub_date'] # 필터 사이드바
    search_fields = ['question_text'] # 검색 박스

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)