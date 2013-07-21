from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100, blank=False)
    done = models.BooleanField("Done",blank=True, default=False)
    def __unicode__(self):
    	return "%s" % self.todo

class UserTodo(models.Model):
    todo = models.CharField(max_length=100, blank=False)
    done = models.BooleanField("Done",blank=True, default=False)
    due = models.DateField(blank=True)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    def __unicode__(self):
    	return "%s" % self.todo
