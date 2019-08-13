from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your models here.


class Question(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    language_type =(('HTML', 'HTML'),
                    ('Javascript', 'Javascript'),
                    ('Node.js', 'Node.js'),
                    ('React', 'React'),
                    ('Python', 'Python'),
                    ('Data Science', 'Data Science'),
                    ('SQL', 'SQL'),
                    ('Java', 'Java'),
                    ('JQuery', 'JQuery'),
                    ('css', 'css'),
                    ('Sass', 'Sass'))
    language = models.CharField(max_length=50, choices=language_type, default='HTML')
    post_body = models.TextField(blank=False)
    post_title = models.CharField(max_length=50, blank=False)
    pub_date = models.DateField(default=timezone.now, blank=True)

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

    def get_first_page(self):
        replies = self.replies()
        paginator = Paginator(replies, 20)
        replies_response = paginator.get_page('1')
        replies_response.number = 1
        return replies_response

    def get_first_page_uncensored(self):
        replies = self.replies_uncensored()
        paginator = Paginator(replies, 20)
        replies_response = paginator.get_page('1')
        replies_response.number = 1
        return replies_response

    def replies(self):
        return Reply.objects.filter(post=self, block=False).order_by('-pub_date')

    def replies_uncensored(self):
        return Reply.objects.filter(post=self).order_by('-pub_date')


class Reply(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE)
    reply_body = models.TextField(blank=False)
    pub_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    block = models.BooleanField(default=False)

    def __str__(self):
        return self.reply_body

    def get_account_data(self):
        us = User.objects.get(user=self.author)
        return us
