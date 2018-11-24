from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import PollQuestionPostForm
from .models import Choice, Question
from rest_framework import viewsets

from django.contrib.auth.models import User, Group
from polls.serializers import QuestionSerializer, GroupSerializer, UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """RETURN THE LAST FIVE QUESTIONS """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class CreatePollView(generic.CreateView):
    model = Question
    fields = [
        'question_text',
        'pub_date',
    ]
    template_name = 'polls/create.html'
    success_url = '/polls'
    
# class CreateChoicesView(generic.CreateView):
#     model = Choice 

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': 'You did not select a choice.'
        })
    else:
        selected_choice.votes += 1 
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer