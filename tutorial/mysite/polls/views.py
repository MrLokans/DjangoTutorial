from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        })
    # output = ', '.join([p.question_text + "</br>" for p in latest_question_list])
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("Looking at question {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("Yo're voting for {}".format(question_id))