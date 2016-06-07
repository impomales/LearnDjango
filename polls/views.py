from django.http import HttpResponse

# Create your views here.
# Displays latest questions.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
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