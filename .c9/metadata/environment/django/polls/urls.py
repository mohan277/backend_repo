{"filter":false,"title":"urls.py","tooltip":"/django/polls/urls.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["from django.urls import path","","from . import views","","urlpatterns = [","    path('', views.index, name='index'),","]"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["from django.urls import path","","from . import views","","urlpatterns = [","    path('', views.index, name='index'),","]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["from django.urls import path","","from . import views","","urlpatterns = [","    # ex: /polls/","    path('', views.index, name='index'),","    # ex: /polls/5/","    path('<int:question_id>/', views.detail, name='detail'),","    # ex: /polls/5/results/","    path('<int:question_id>/results/', views.results, name='results'),","    # ex: /polls/5/vote/","    path('<int:question_id>/vote/', views.vote, name='vote'),","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":17},"end":{"row":5,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1583418606796,"hash":"6c8a24b2e5014ef5680439e3a1b5a6aa9f2cb3fb"}