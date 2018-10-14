from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Fact(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	comment = models.ForeignKey('fc.Fact', on_delete=models.CASCADE, related_name='comments')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)



