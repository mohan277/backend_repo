{"changed":true,"filter":false,"title":"views.py","tooltip":"/django_assignment_001/django_assignment_001/questions/views.py","value":"","undoManager":{"mark":30,"position":31,"stack":[[{"start":{"row":3,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["def index(request):","    latest_question_list = Question.objects.order_by('-pub_date')[:5]","    context = {'latest_question_list': latest_question_list}","    return render(request, 'polls/index.html', context)","    ",""],"id":2}],[{"start":{"row":8,"column":0},"end":{"row":10,"column":71},"action":"insert","lines":["def detail(request, question_id):","    question = get_object_or_404(Question, pk=question_id)","    return render(request, 'polls/detail.html', {'question': question})"],"id":3}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["l"],"id":4},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["i"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["a"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["t"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["e"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":19},"action":"insert","lines":["create_question"],"id":5}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":71},"action":"remove","lines":["question = get_object_or_404(Question, pk=question_id)","    return render(request, 'polls/detail.html', {'question': question})"],"id":6}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["p"],"id":7},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["a"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["s"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":8},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["def create_question(request, question_id):","    pass"],"id":9}],[{"start":{"row":12,"column":8},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["def create_question(request, question_id):","    pass"],"id":11}],[{"start":{"row":15,"column":8},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["def create_question(request, question_id):","    pass"],"id":13}],[{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["",""],"id":15}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":16}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["def create_question(request, question_id):","    pass"],"id":17}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":19},"action":"remove","lines":["create_question"],"id":18},{"start":{"row":11,"column":4},"end":{"row":11,"column":16},"action":"insert","lines":["get_question"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":19},"action":"remove","lines":["create_question"],"id":19},{"start":{"row":14,"column":4},"end":{"row":14,"column":19},"action":"insert","lines":["update_question"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":19},"action":"remove","lines":["create_question"],"id":20},{"start":{"row":17,"column":4},"end":{"row":17,"column":19},"action":"insert","lines":["delete_question"]}],[{"start":{"row":1,"column":35},"end":{"row":6,"column":55},"action":"remove","lines":["","","def index(request):","    latest_question_list = Question.objects.order_by('-pub_date')[:5]","    context = {'latest_question_list': latest_question_list}","    return render(request, 'polls/index.html', context)"],"id":21}],[{"start":{"row":14,"column":0},"end":{"row":16,"column":8},"action":"remove","lines":["","def create_question(request, question_id):","    pass"],"id":22}],[{"start":{"row":2,"column":4},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "],"id":24}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":21},"action":"insert","lines":["get_list_of_questions"],"id":25}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":26}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":4,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["def create_question(request, question_id):","    pass",""],"id":28}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":21},"action":"remove","lines":["get_list_of_questions"],"id":29}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":19},"action":"remove","lines":["create_question"],"id":30},{"start":{"row":4,"column":4},"end":{"row":4,"column":25},"action":"insert","lines":["get_list_of_questions"]}],[{"start":{"row":5,"column":8},"end":{"row":6,"column":0},"action":"remove","lines":["",""],"id":31}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":25},"action":"remove","lines":["# Create your views here."],"id":32},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["from django.shortcuts import render","    ","","def get_list_of_questions(request, question_id):","    pass","","def create_question(request, question_id):","    pass","","def get_question(request, question_id):","    pass","","def update_question(request, question_id):","    pass","","def delete_question(request, question_id):","    pass",""],"id":33}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1583487667587}