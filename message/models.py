from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class post:
    post_title = models.CharField(max_length = 50)
    post_author = models.CharField(max_length = 20)
    post_text = models.TextField
    post_date = models.DateTimeField('date published')
    post_creation = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.post_title

    def published_date(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days = 1)


    #remeber modelform

