from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		instance.profile=Profile(user=instance)
		instance.profile.save()

# kwargs allows additional arguments
# Dhoni11  Mahifan56
