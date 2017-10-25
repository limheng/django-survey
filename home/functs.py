from .models import SurveyQuestion, SurveyAnswer, SurveyComplete
from random import choices

def getAnswers(question):
    """ Retrieves answers from a question queryset."""
    answers = question.surveyanswer_set.all()
    return [a.answer for i, a in enumerate(answers)]

def getQuestionCount():
    """ Retrieves the total number of questions in the database."""
    return SurveyQuestion.objects.count()

def getQuestionById(question_id):
    """ Retrieves the queryset of the specified index."""
    survey_question = SurveyQuestion.objects.get(pk=question_id)
    return survey_question

def getCompleteCount(key):
    """ Retrieves the completed count of a user with the specified (session) key."""
    return SurveyComplete.objects.filter(session=key).count()

def getQuestionIdNotComplete(key):
    """ Retrieves the questions not completed by (session) key user. """
    survey_complete = SurveyComplete.objects.filter(session=key).values('qid')
    survey_question = SurveyQuestion.objects.exclude(id__in=survey_complete).values('id')
    return [i['id'] for i in survey_question]

def checkComplete(progress):
    """ Checks if survey is complete based on progress. """
    if progress >= getQuestionCount():
        return True
    return False

def getQuestionAnswers(key):
    """ Selects random unanswered question and returns question and answers. """
    question_index = choices(getQuestionIdNotComplete(key))[0]
    question = getQuestionById(question_index)
    answers = getAnswers(question)
    return question, answers

# def getQuestionByIndex(index):
#     """ Retrieves the queryset of the specified index."""
#     survey_question = SurveyQuestion.objects.order_by('id')[index]
#     return survey_question
