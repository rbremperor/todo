from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import ForeignKey

User = get_user_model()

class Todo(models.Model):
    NEW = 'NEW'
    FINISHED = 'FINISHED'

    STATUS= [
        (NEW, 'New'),
        (FINISHED, 'Finished'),
    ]

    user = ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=512)
    status = models.CharField(choices= STATUS,max_length=10, default=NEW)

    def mark_as_finished(self):
        self.status = self.FINISHED
        self.save()

    def mark_as_unfinished(self):
        self.status = self.NEW
        self.save()