from django.shortcuts import render
from home.models import SurveyQuestion, SurveyAnswer, SurveyComplete
from home.functs import *

def dashboard(request):
    questions_answered = SurveyComplete.objects.count()
    total_questions = SurveyQuestion.objects.count()
    surveys_completed = 0
    if total_questions > 0:
        surveys_completed = questions_answered//total_questions

    results = SurveyComplete.objects.order_by('qid')
    return render(request,
        'dashboard.html',
        context={'questions_answered': questions_answered,
            'surveys_completed': surveys_completed,
            'total_questions': total_questions,
            'results': results
            }
        )
