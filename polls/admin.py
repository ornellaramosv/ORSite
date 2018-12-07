from django.contrib import admin

from .models import Topic, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['topic_text']}),
        ('Date Created', {'fields': ['cre_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]
    list_display = ('topic_text', 'cre_date')
    list_filter = ['cre_date']
    search_fields = ['topic_text']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['choice_text']}),
        ('Votes',       {'fields': ['votes'], 'classes': ['collapse']}),
    ]
    list_display = ('choice_text', 'votes')
    search_fields = ['choice_text']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
