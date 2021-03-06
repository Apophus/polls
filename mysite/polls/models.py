from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Poll(object):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

class Choice(object):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)