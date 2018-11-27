from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question, Choice, Topic
from django.urls import reverse
from django.db.models import F
from .forms import CreateTopic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def index(request):
    return render(request, 'polls/index.html')


def all_topics(request):
    try:
        topic = Topic.objects.all()
    except Topic.DoesNotExist:
        return render(request, 'polls/topics.html', {
            'error_message': "There no topics."
        })
    return render(request, 'polls/topics.html', {
        'topics': topic
    })


def all_questions(request, topic_id):
    try:
        question = Question.objects.filter(topic=topic_id).all()
    except Question.DoesNotExist:
        return render(request, 'polls/questions.html', {
            'error_message': "The topic don't have questions."
        })
    else:
        return render(request, 'polls/questions.html', {
            'questions': question
        })


def all_options(request, question_id):
    try:
        choice = Choice.objects.filter(question_id=question_id).all()
        q_choice = Choice.objects.filter(question_id=question_id).values('question').distinct()
        q = q_choice[0]['question']
        question_t = Question.objects.filter(id=q).values('question_text')
        question_text = question_t[0]['question_text']

        idtopic = Question.objects.filter(id=q).values('topic_id').distinct()
        id_topic = idtopic[0]['topic_id']

    except Choice.DoesNotExist:
        return render(request, 'polls/vote.html', {
            'error_message': "The question don't have options.",
            'question_id': question_id,
        })
    except IndexError:
        return render(request, 'polls/vote.html', {
            'error_message': "The question don't have options.",
            'question_id': question_id,
        })
    else:
        return render(request, 'polls/vote.html', {
            'choices': choice,
            'u_question': question_text,
            'question_id': question_id,
            'topic_id': id_topic,
        })


def results(request, question_id):
    try:
        choice = Choice.objects.filter(question_id=question_id).all()
        q_choice = Choice.objects.filter(question_id=question_id).values('question').distinct()
        q = q_choice[0]['question']
        question_t = Question.objects.filter(id=q).values('question_text')
        question_text = question_t[0]['question_text']
    except Choice.DoesNotExist:
        return render(request, 'polls/vote.html', {
            'error_message': "The question don't have options.",
            'question_id': question_id,
        })
    except IndexError:
        return render(request, 'polls/results.html', {
            'error_message': "The question don't have options.",
            'question_id': question_id,
        })
    else:
        return render(request, 'polls/results.html', {
            'choices': choice,
            'u_question': question_text,
            'question_id': question_id,
        })


def vote(request, question_id):
    try:
        question = Question.objects.filter(id=question_id).values('id')
        choice = request.POST.get('choice')
        selected_option = Choice.objects.get(id=choice)
    except Choice.DoesNotExist:
        return render(request, 'polls/results.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    except IndexError:
        return render(request, 'polls/results.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_option.votes = F('votes') + 1
        selected_option.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def new_topic(request):
    if request.method == "POST":
        form = CreateTopic(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.cre_date = timezone.now()
            topic.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = CreateTopic()
        return render(request, 'polls/new_topic.html', {'form': form})


def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == "POST":
        form = CreateTopic(request.POST, instance=topic)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.cre_date = timezone.now()
            topic.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = CreateTopic(instance=topic)
        return render(request, 'polls/new_topic.html', {'form': form})
