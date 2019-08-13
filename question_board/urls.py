from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionboard, name='question-board'),
    path('ask/', views.PostCreateView.as_view(), name='ask'),
    path('css/', views.css, name='css'),
    path('datascience/', views.datascience, name='datascience'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='question_detail'),
    path('html/', views.html, name='html'),
    path('java/', views.java, name='java'),
    path('javascript/', views.javascript, name='javascript'),
    path('node/', views.node, name='node'),
    path('python/', views.python, name='python'),
    path('rank/', views.rank, name='rank'),
    path('react/', views.react, name='react'),
    path('sass/', views.sass, name='sass'),
    path('sql/', views.sql, name='sql'),
    path('jquery/', views.jquery, name='jquery'),
    path('all/', views.all, name='all'),

    ## Replies
    path('reply/<int:post_id>/', views.ReplyCreateView.as_view(), name='reply'),
    path('reply-list/<int:post_id>/', views.ReplyPaginatorView.as_view(), name="reply-list"),

]