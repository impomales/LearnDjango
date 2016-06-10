from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
# Displays latest questions.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        # return last five published questions.
        return Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
    
# displays question text
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

# displays results of a question
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# handles voting for a choice in a question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # F() used to prevent race conditions.
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # redirect after POST to prevent double post if users hits back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)