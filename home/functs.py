from .models import SurveyQuestion, SurveyAnswer, SurveyComplete

def getAnswers(question):
    """ Retrieves answers from a question queryset."""
    answers = question.surveyanswer_set.all()
    return [a.answer for i, a in enumerate(answers)]

def getQuestionCount():
    """ Retrieves the total number of questions in the database."""
    return SurveyQuestion.objects.count()

def getProgress(key):
    """ Retrieves the current progress by counting the completed survey questions."""
    if SurveyComplete.objects.count() == 0:
        return -1
    question_id = SurveyComplete.objects.order_by('-qid').filter(session=key).values('qid').first()['qid']
    return question_id

def getQuestionByIndex(index):
    """ Retrieves the queryset of the specified index."""
    question_id = SurveyQuestion.objects.order_by('id')[index]
    return question_id

def getCompleteCount(key):
    """ Retrieves the  completed count of a user with the specified (session) key."""
    return SurveyComplete.objects.filter(session=key).count()
