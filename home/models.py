from django.db import models

class SurveyQuestion(models.Model):
    question = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.question


class SurveyAnswer(models.Model):
    question_id = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer


class SurveyComplete(models.Model):
    qid = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    session = models.CharField(max_length=100)

    def __str__(self):
        return str(self.qid)
