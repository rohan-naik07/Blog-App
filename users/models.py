from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)# delete profile after deleting user but not vice-e-eversa
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'
'''
	def save(self): #method that runs after model is saved
		super().save()
		img=Image.open(self.image.path)

		if img.height > 300 or img.width >300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
'''
