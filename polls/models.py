import datetime

from django.db import models
from django.utils import timezone


class Topic(models.Model):
    topic_text = models.CharField(max_length=100)
    cre_date = models.DateTimeField('date created', default=timezone.now)
    upd_date = models.DateTimeField(default=timezone.now)
    topic_act = models.BooleanField('active', default=False)


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
