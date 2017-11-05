from .models import SurveyQuestion, SurveyAnswer, SurveyComplete
from random import choices


def get_answers(question):
    """ Retrieves answers from a question queryset."""
    answers = question.surveyanswer_set.all()
    return [a.answer for i, a in enumerate(answers)]


def get_question_count():
    """ Retrieves the total number of questions in the database."""
    return SurveyQuestion.objects.count()


def get_question_by_id(question_id):
    """ Retrieves the queryset of the specified index."""
    survey_question = SurveyQuestion.objects.get(pk=question_id)
    return survey_question


def get_complete_count(key):
    """ Retrieves the completed count of a user with the specified (session) key."""
    return SurveyComplete.objects.filter(session=key).count()


def get_question_id_not_complete(key):
    """ Retrieves the questions not completed by (session) key user. """
    survey_complete = SurveyComplete.objects.filter(session=key).values('qid')
    survey_question = SurveyQuestion.objects.exclude(id__in=survey_complete).values('id')
    return [i['id'] for i in survey_question]


def check_complete(progress):
    """ Checks if survey is complete based on progress. """
    if progress >= get_question_count():
        return True
    return False


def get_question_answers(key):
    """ Selects random unanswered question and returns question and answers. """
    question_index = choices(get_question_id_not_complete(key))[0]
    question = get_question_by_id(question_index)
    answers = get_answers(question)
    return question, answers

# def get_question_by_index(index):
#     """ Retrieves the queryset of the specified index."""
#     survey_question = SurveyQuestion.objects.order_by('id')[index]
#     return survey_question
