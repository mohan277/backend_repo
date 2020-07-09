from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.shortcuts import get_object_or_404

def get_list_of_questions(request):
    questions_list = Question.objects.all()
    sort = request.GET.get('sort_by')
    if sort == 'desc':
        questions_list = Question.objects.all().order_by('-text')
    if sort == 'asc':
        questions_list = Question.objects.all().order_by('text')
    return render(request,'get_list_of_questions.html',{'question':questions_list})

def create_question(request):
    if request.method == 'GET':
        return render(request,'create_question_form.html')
    if request.method == 'POST':
        if request.POST.get('question') and request.POST.get('answer'):
            question_obj = Question()
            question_obj.text = request.POST.get('question')
            question_obj.answer = request.POST.get('answer')
            question_obj.save()
            return render(request,'create_question_success.html')
        else:
            return render(request,'create_question_failure.html')
    
    


def get_question(request, question_id):
    question_obj = get_object_or_404(Question,pk=question_id)
    return render(request,'each_question_form.html',{'question':question_obj})


def update_question(request, question_id):
    if request.method == 'GET':
        question_obj = get_object_or_404(Question,pk=question_id)
        return render(request,'each_question_form.html',{'question':question_obj})
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if question and answer:
            question_obj = Question.objects.get(pk=question_id)
            question_obj.text = question
            question_obj.answer = answer
            question_obj.save()
            return render(request,'update_question_success.html')
        else:
            return render(request,'update_question_failure.html')
    

def delete_question(request, question_id):
    question_obj = Question.objects.get(pk=question_id)
    try:
        if question_obj:
            question_obj.delete()
            return render(request,'delete_question_success.html')
    except:
        return render(request,'delete_question_failure.html')