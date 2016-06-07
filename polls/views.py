from django.http import HttpResponse

from .models import Question

# Create your views here.
# Displays latest questions.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    
# displays question text
def detail(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)

# displays results of a question
def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

# handles voting for a choice in a question
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)