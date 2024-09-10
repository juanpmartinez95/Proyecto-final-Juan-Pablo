from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set_permissions')
