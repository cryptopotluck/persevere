from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import StringIO
from PIL import Image
from stdimage import StdImageField, JPEGField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    about = models.TextField(blank=True)
    profile_image = StdImageField(upload_to='profile/%Y/%m/%d/', default='profile/default/default_img.png',
                                  blank=True, variations={'thumbnail': {'width': 300, 'height': 300, "crop": True}})
    email = models.EmailField(blank=True)
    first_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=40)
    postal_code = models.CharField(blank=True, max_length=5)


    def __str__(self):
        return f'{self.user.username}'

    # def save(self, force_insert=False, force_update=True, using=None,
    #          update_fields=profile_image):
    #     super().save()
    #
    #     img = Image.open(self.profile_image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

