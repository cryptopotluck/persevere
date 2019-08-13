from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Question, Reply
from tinymce.widgets import TinyMCE
from question_board.forms import PostForm
from users.models import Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views import View
from .forms import ReplyForm

# Create your views here.


def questionboard(requests):
    return render(requests, 'question_board/question_board.html')


def all(requests):
    post = Question.objects.values()
    post_owner = Profile.objects.all().values()
    user_username = User.objects.all().values()
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts,
        'post_owner': post_owner,
        'username': user_username
    }
    return render(requests, 'question_board/all_question_categories.html', context)


class PostCreateView(CreateView):
    model = Question
    fields = ['language', 'post_title', 'post_body', 'post_owner_id']

    def get_form(self, form_class=PostForm):
        form = super(PostCreateView, self).get_form(PostForm)
        form.fields['post_body'].widget = TinyMCE()
        return form

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.post_owner_id = self.request.user.id
        instance.save()
        response = super().form_valid(form)
        self.object.save()
        return response


""" Replies """


class ReplyCreateView(View):
    template_name = 'question_board/reply_form.html'

    def get(self, request, post_id):
        post = Question.objects.get(pk=post_id)
        form = ReplyForm()
        context = {
            'post': post,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, post_id):
        post = Question.objects.get(pk=post_id)
        form = ReplyForm(request.POST)

        if form.is_valid():
            reply = Reply()
            reply.post = post
            reply.author = request.user
            reply.reply_body = form.data['reply_body']
            reply.save()
            return redirect('question_detail', pk=post.pk)
        else:
            pass


class ReplyPaginatorView(View):
    template_name='question_board/reply-list.html'
    def get(self, request, post_id):

        if request.is_ajax():
            post = Question.objects.get(pk=post_id)
            replies = post.replies()
            paginator = Paginator(replies,5)

            page = request.GET.get('page')

            replies_response = paginator.get_page(page)

            replies_response.number = int(page)

            context = {
                'post':post,
                'replies_response': replies_response
            }

            return render(request, self.template_name, context)
        else:
            print('not ajax')
            pass


def css(requests):
    post = Question.objects.filter(language='css')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/css_questions.html', context)


def datascience(requests):
    post = Question.objects.filter(language='Data Science')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/datascience_questions.html', context)


class PostDetailView(DetailView):
    model = Question
    # template_name = 'question_board/question_detail.html'
    # def get(self, request, post_id):
    #     post = Question.objects.get(pk=post_id)
    #     replies = Reply.objects.filter(post=self)
    #     paginator = Paginator(replies, 10)
    #     page = request.GET.get('page')
    #     my_posts = paginator.get_page(page)
    #     context = {
    #         'posts': my_posts
    #     }
    #     return render(request, self.template_name, context)


def html(requests):
    post = Question.objects.filter(language='HTML')
    paginator = Paginator(post, 10)
    page=requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts':my_posts
    }

    return render(requests, 'question_board/html_questions.html', context)


def java(requests):
    post = Question.objects.filter(language='Java')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/java_questions.html', context)


def javascript(requests):
    post = Question.objects.filter(language='Javascript')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }

    return render(requests, 'question_board/javascript_questions.html', context)


def jquery(requests):
    post = Question.objects.filter(language='JQuery')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/jquery_questions.html', context)


def node(requests):
    post = Question.objects.filter(language='Node.js')
    paginator = Paginator(post, 1)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/node_questions.html', context)


def python(requests):
    post = Question.objects.filter(language='Python')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }

    return render(requests, 'question_board/python_questions.html', context)


def rank(requests):
    return render(requests, 'question_board/rank_by_new.html')


def react(requests):
    post = Question.objects.filter(language='React')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/react_questions.html', context)


def sass(requests):
    post = Question.objects.filter(language='Sass')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/sass_questions.html', context)


def sql(requests):
    post = Question.objects.filter(language='SQL')
    paginator = Paginator(post, 10)
    page = requests.GET.get('page')
    my_posts = paginator.get_page(page)
    context = {
        'posts': my_posts
    }
    return render(requests, 'question_board/sql_questions.html', context)

