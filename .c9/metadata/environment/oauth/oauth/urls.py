{"filter":false,"title":"urls.py","tooltip":"/oauth/oauth/urls.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":15,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["from django.contrib import admin","from django.urls import path","","urlpatterns = [","    path('admin/', admin.site.urls),","]",""],"id":2},{"start":{"row":15,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["from django.contrib import admin","from django.urls import path, include","","urlpatterns = [","    path('admin/', admin.site.urls),","    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),","    path('', include('<app_name>.urls')),","]"]}],[{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"remove","lines":["e"],"id":3},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["m"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["a"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":["n"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["_"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["p"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["p"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["a"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":["<"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":[">"],"id":4}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["n"],"id":5},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["e"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["w"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["a"],"id":6},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["p"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["p"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":37},"end":{"row":21,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588586435125,"hash":"be35f4ad359959ba646111feaf0bd665f871a8a2"}