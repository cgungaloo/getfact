from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Fact(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	fcId = models.ForeignKey('fc.Fact', on_delete=models.CASCADE)

class Comment(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	comment = models.ForeignKey('fc.Fact', on_delete=models.CASCADE, related_name='comments')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image= models.ImageField(upload_to='profile_image',default='profile_image/SSMILE.jpg')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


