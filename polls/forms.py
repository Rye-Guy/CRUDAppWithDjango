from django import forms

from .models import Question

class PollQuestionPostForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date'
        ]