from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Fact(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	totalLikes = models.IntegerField(default=0)
	totalDislikes = models.IntegerField(default=0)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class LikeDislike(models.Model):
	LIKE = 1
	DISLIKE = -1

	VOTES = (
		(DISLIKE, 'Dislike'),
		(LIKE, 'Like')
	)

	vote = models.SmallIntegerField(verbose_name="vote", choices=VOTES)
	user = models.ForeignKey('auth.User', on_delete=models.SET_NULL,null=True)
	fcId = models.ForeignKey('fc.Fact', on_delete=models.CASCADE)

class Comment(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,null=True)
	comment = models.ForeignKey('fc.Fact', on_delete=models.CASCADE, related_name='comments')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	totalTrues = models.IntegerField(default=0)
	totalSortOfs = models.IntegerField(default=0)
	totalFalses = models.IntegerField(default=0)

class ReviewComment(models.Model):
	isTrue = 1
	isSortOfTrue = 0
	isFalse = -1

	VOTES =(
		(isTrue, 'True'),
		(isSortOfTrue,'Sort Of True'),
		(isFalse,'False')
		)

	vote = models.SmallIntegerField(verbose_name="vote", choices=VOTES)
	user = models.ForeignKey('auth.User', on_delete=models.SET_NULL,null=True)
	comment = models.ForeignKey('fc.Comment', on_delete=models.CASCADE)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
	image= models.ImageField(upload_to='profile_image',default='profile_image/SSMILE.jpg')

class ReportFact(models.Model):
	fact = models.ForeignKey('fc.Fact', on_delete=models.CASCADE)
	reason = models.TextField(max_length=300)
	created_date = models.DateTimeField(
		default=timezone.now)
	investigated = models.BooleanField(default=False)
	resolution = models.TextField(max_length=300,null=True)

class ReportComment(models.Model):
	comment = models.ForeignKey('fc.Comment', on_delete=models.CASCADE)
	reason = models.TextField(max_length=300)
	created_date = models.DateTimeField(
		default=timezone.now)
	investigated = models.BooleanField(default=False)
	resolution = models.TextField(max_length=300,null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


