from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
	user = models.ForeignKey(User)
	text = models.CharField(max_length=140)

	created = models.DateTimeField(auto_now_add=True, blank = True)
	updated = models.DateTimeField(auto_now=True, blank = True)

	class Meta:
		ordering = ['created']


	def __str__(self):
		return self.text

	def __unicode__(self):
		return self.text + ' - ' + self.user.username