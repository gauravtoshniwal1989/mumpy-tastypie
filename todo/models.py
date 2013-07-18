from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100, blank=False)
    done = models.BooleanField("Done",blank=True, default=False)

    def __unicode__(self):
    	return "%s" % self.todo