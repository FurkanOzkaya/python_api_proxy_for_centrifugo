from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.conf import settings


def upload_to(instance, filename):
    return f'profile_image/{filename}'


class UserModel(AbstractUser):
    slug = CharField(
        max_length=200, help_text="Slug of User", blank=True)
    bio = CharField(
        max_length=500, help_text="Biography of User", blank=True)
    job = CharField(max_length=100, help_text="Job of User", blank=True)
    avatar = ImageField(upload_to="profile_image/",
                        help_text="Profile image of User", default=settings.DEFAULT_AVATAR)
