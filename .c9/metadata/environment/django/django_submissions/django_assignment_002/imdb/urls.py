{"filter":false,"title":"urls.py","tooltip":"/django/django_submissions/django_assignment_002/imdb/urls.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["from django.urls import path","","from . import views","","urlpatterns = [","    path('', views.get_list_of_questions, name='get_list_of_questions'),","    path('create/', views.create_question, name='create_question'),","    path('<int:question_id>/get/', views.get_question, name='get_question'),","    path('<int:question_id>/update/', views.update_question, name='update_question'),","    path('<int:question_id>/delete/', views.delete_question, name='delete_question'),","","]","","","","",""],"id":1}],[{"start":{"row":6,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["path('create/', views.create_question, name='create_question'),","    path('<int:question_id>/get/', views.get_question, name='get_question'),","    path('<int:question_id>/update/', views.update_question, name='update_question'),","    path('<int:question_id>/delete/', views.delete_question, name='delete_question'),",""],"id":2},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "]},{"start":{"row":5,"column":72},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":68},"end":{"row":5,"column":69},"action":"remove","lines":["s"],"id":3},{"start":{"row":5,"column":67},"end":{"row":5,"column":68},"action":"remove","lines":["n"]},{"start":{"row":5,"column":66},"end":{"row":5,"column":67},"action":"remove","lines":["o"]},{"start":{"row":5,"column":65},"end":{"row":5,"column":66},"action":"remove","lines":["i"]},{"start":{"row":5,"column":64},"end":{"row":5,"column":65},"action":"remove","lines":["t"]},{"start":{"row":5,"column":63},"end":{"row":5,"column":64},"action":"remove","lines":["s"]},{"start":{"row":5,"column":62},"end":{"row":5,"column":63},"action":"remove","lines":["e"]},{"start":{"row":5,"column":61},"end":{"row":5,"column":62},"action":"remove","lines":["u"]},{"start":{"row":5,"column":60},"end":{"row":5,"column":61},"action":"remove","lines":["q"]},{"start":{"row":5,"column":59},"end":{"row":5,"column":60},"action":"remove","lines":["_"]},{"start":{"row":5,"column":58},"end":{"row":5,"column":59},"action":"remove","lines":["f"]},{"start":{"row":5,"column":57},"end":{"row":5,"column":58},"action":"remove","lines":["o"]},{"start":{"row":5,"column":56},"end":{"row":5,"column":57},"action":"remove","lines":["_"]},{"start":{"row":5,"column":55},"end":{"row":5,"column":56},"action":"remove","lines":["t"]},{"start":{"row":5,"column":54},"end":{"row":5,"column":55},"action":"remove","lines":["s"]},{"start":{"row":5,"column":53},"end":{"row":5,"column":54},"action":"remove","lines":["i"]},{"start":{"row":5,"column":52},"end":{"row":5,"column":53},"action":"remove","lines":["l"]}],[{"start":{"row":5,"column":51},"end":{"row":5,"column":52},"action":"remove","lines":["_"],"id":4},{"start":{"row":5,"column":50},"end":{"row":5,"column":51},"action":"remove","lines":["t"]},{"start":{"row":5,"column":49},"end":{"row":5,"column":50},"action":"remove","lines":["e"]},{"start":{"row":5,"column":48},"end":{"row":5,"column":49},"action":"remove","lines":["g"]}],[{"start":{"row":5,"column":48},"end":{"row":5,"column":49},"action":"insert","lines":["i"],"id":5},{"start":{"row":5,"column":49},"end":{"row":5,"column":50},"action":"insert","lines":["n"]},{"start":{"row":5,"column":50},"end":{"row":5,"column":51},"action":"insert","lines":["d"]},{"start":{"row":5,"column":51},"end":{"row":5,"column":52},"action":"insert","lines":["e"]},{"start":{"row":5,"column":52},"end":{"row":5,"column":53},"action":"insert","lines":["x"]}],[{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"remove","lines":["s"],"id":6},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"remove","lines":["n"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":["o"]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"remove","lines":["i"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["t"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"remove","lines":["s"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"remove","lines":["e"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":["u"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"remove","lines":["q"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"remove","lines":["_"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"remove","lines":["f"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["o"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["_"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["t"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["s"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["i"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["l"]}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["_"],"id":7},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["t"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["e"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["g"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["i"],"id":8},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["n"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["d"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["e"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["x"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":24},"end":{"row":5,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1583902948539,"hash":"2b732e88c3b5300c6aa6399045ac72aab0dfeee2"}