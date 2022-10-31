from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse

# Create your views here.

# 목록화면 함수
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'survey/index.html', context)

# 상세화면 함수
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/detail.html', {'question': question})

# 결과화면 함수
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/results.html', {'question': question})

# post 처리 함수
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # global selected_choice
        # for sc in request.POST.getlist('choice'):  # 체크박스 값을 리스트로 불러오기 (리스트 크기만큼 반복) 이때 str로 불러와짐
        #     scnum = int(sc)  # str 타입을 int로 변환
        #     selected_choice = Question.choice_set.get(pk=scnum)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'survey/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))