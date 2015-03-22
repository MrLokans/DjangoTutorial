from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Representation order

class QuestionAdmin(admin.ModelAdmin):

    # Splits into groups
    list_filter = ['pub_date']
    search_fields = ['question_text']

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None, {"fields": ['question_text']}),
        ('Date information', {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline] # Adds choices to Question admin
    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)