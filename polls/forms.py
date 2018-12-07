from django import forms
from django.forms import ModelForm
from .models import Topic
from bootstrap_datepicker_plus import DateTimePickerInput


class CreateTopic(ModelForm):

    class Meta:
        model = Topic
        fields = ['topic_text']
        labels = {
            'topic_text': 'Topic',
        }

    def __init__(self, *args, **kwargs):
        super(CreateTopic, self).__init__(*args, **kwargs)
        self.fields['topic_text'].widget.attrs['placeholder'] = ''
