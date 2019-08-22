from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.utils import timezone
from django.urls import reverse
from stdimage import StdImageField

# Create your models here.


class Blog(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    post_body = models.TextField(blank=False)
    post_title = models.CharField(max_length=50, blank=False)
    pub_date = models.DateField(default=timezone.now, blank=True)
    article_pic = StdImageField(upload_to='articles/%Y/%m/%d/',
                                blank=False, variations={'thumbnail': {'width': 300, 'height': 300, "crop": True}})

    def get_absolute_url(self):
        return reverse('blog_home', kwargs={'pk': self.pk})
