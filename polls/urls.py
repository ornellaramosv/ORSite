from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.all_topics, name='topics'),
    path('topics/<int:topic_id>/', views.edit_topic, name='topic_detail'),
    path('topic/new', views.new_topic, name='new_topic'),
    path('question/<int:topic_id>/', views.all_questions, name='question'),
    path('options/<int:question_id>', views.all_options, name='options'),
    path('results/<int:question_id>/', views.results, name='results'),
    path('vote/<int:question_id>/', views.vote, name='vote'),

]

