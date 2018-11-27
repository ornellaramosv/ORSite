from django import forms
from django.forms import ModelForm
from .models import Topic
from bootstrap_datepicker_plus import DateTimePickerInput


class CreateTopic(ModelForm):

    class Meta:
        model = Topic
        fields = ['topic_text', 'pub_date']
        widgets = {
            'pub_date': DateTimePickerInput(
                format='YYYY-MM-DD hh:mm:ss',
            )
        }
        labels = {
            'topic_text': 'Topic',
            'pub_date': 'Date Published',
        }

    def __init__(self, *args, **kwargs):
        super(CreateTopic, self).__init__(*args, **kwargs)
        self.fields['topic_text'].widget.attrs['placeholder'] = ''
        self.fields['pub_date'].widget.attrs['placeholder'] = ''
