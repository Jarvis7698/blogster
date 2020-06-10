from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):

	post_title = models.CharField(max_length=50)
	post_content = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	post_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.post_title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
