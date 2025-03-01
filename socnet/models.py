from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(
        "self",
        related_name="friend_of",
        symmetrical=False,
        blank=True
    )
    bio = models.TextField(default="My bio", max_length=300)
    avatar = models.ImageField(upload_to='', default='default.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Create your models here.
