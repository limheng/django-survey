from django.shortcuts import render
from .models import SurveyComplete
from django.views.generic import TemplateView
from account.views import dashboard
from .functs import *


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
            request.session['last_choice'] = ()
        progress = getCompleteCount(request.session.session_key)
        if checkComplete(progress):
            return render(request, 'done.html')
        question, answers = getQuestionAnswers(request.session.session_key)
        request.session['last_choice'] = (question.id, question.question)
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
        if choice != '':
            last_id, last_question = request.session['last_choice']
            sc = SurveyComplete(qid=last_id,
                question=last_question,
                answer=choice, session=request.session.session_key
            )
            sc.save()
        progress += 1
        if checkComplete(progress):
            return render(request, 'done.html')
        question, answers = getQuestionAnswers(request.session.session_key)
        request.session['last_choice'] = (question.id, question.question)
        return render(request,
            self.template_name,
            context={'progress': progress+1,
                'question': question,
                'answers': answers}
            )
