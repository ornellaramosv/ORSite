from django.urls import path, include

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.act_topics, name='topics'),
    path('topics/', views.no_act_topics, name='no_act_topics'),
    path('topics/edit/<int:topic_id>/', views.topic_edit, name='topic_detail'),
    path('topic/new', views.topic_new, name='new_topic'),
    path('topic/remove/<int:topic_id>/', views.topic_remove, name='topic_remove'),
    path('question/<int:topic_id>/', views.all_questions, name='question'),
    path('options/<int:question_id>', views.all_options, name='options'),
    path('results/<int:question_id>/', views.results, name='results'),
    path('vote/<int:question_id>/', views.vote, name='vote'),

]

