from django.shortcuts import render
from .models import SurveyComplete
from django.views.generic import TemplateView
from account.views import dashboard
from .functs import *
from random import shuffle


def home(request):
    if getQuestionCount() <= 0:
        return render(request, 'noquestion.html')
    if request.user.is_authenticated():
        return dashboard(request)
    return render(request, 'home.html', context={'count': getQuestionCount()})

def review(request):
    progress = int(getCompleteCount(request.session.session_key))
    count = getQuestionCount()
    if count < progress:
        count = progress
    if count == 0:
        return render(request, 'review.html',
            context={'progress': 0,
                'remain': 0,
                'count': 0
            }
        )
    perc_progress = (progress/count) * 100
    remain = count - progress
    perc_remain = (remain/count) * 100
    return render(request, 'review.html',
        context={'progress': int(perc_progress),
            'remain': int(perc_remain),
            'count': count
        }
    )

class QuestionView(TemplateView):
    template_name = 'question.html'

    def get(self, request):
        if getQuestionCount() <= 0:
            return render(request, 'noquestion.html')
        if request.session.get('progress', None) == None:
            request.session['progress'] = 0
            request.session['visited'] = 0
            request.session['last_question'] = ''
            question_indexes = [i for i in range(0, getQuestionCount())]
            shuffle(question_indexes)
            request.session['randomize'] = question_indexes
        random_list = request.session['randomize']
        progress = getCompleteCount(request.session.session_key)
        if progress >= len(random_list):
            return render(request, 'done.html')
        question = getQuestionByIndex(random_list[progress])
        request.session['last_question'] = question.question
        answers = getAnswers(question)
        return render(request,
            self.template_name,
            context={'progress': progress+1,
                'question': question,
                'answers': answers
            }
        )

    def post(self, request):
        progress = getCompleteCount(request.session.session_key)
        choice = request.POST.get('choice', '')
        random_list = request.session['randomize']
        if choice != '':
            sc = SurveyComplete(qid=random_list[progress]+1,
                question=request.session['last_question'],
                answer=choice, session=request.session.session_key
            )
            sc.save()
        progress += 1
        if progress >= len(random_list):
            return render(request, 'done.html')
        question = getQuestionByIndex(random_list[progress])
        request.session['last_question'] = question.question
        answers = getAnswers(question)
        return render(request,
            self.template_name,
            context={'progress': progress+1,
                'question': question,
                'answers': answers}
            )
