from django.contrib import admin
from home.models import SurveyQuestion, SurveyAnswer, SurveyComplete


class SurveyAnswerInline(admin.TabularInline):
    model = SurveyAnswer


class SurveyQuestionAdmin(admin.ModelAdmin):
    model = SurveyQuestion
    inlines = [
        SurveyAnswerInline,
    ]


class SurveyCompleteAdmin(admin.ModelAdmin):
    list_display = ('session', 'question', 'answer')

admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(SurveyComplete, SurveyCompleteAdmin)
admin.site.site_header = 'Survey App'
admin.site.site_title = 'Survey App'
