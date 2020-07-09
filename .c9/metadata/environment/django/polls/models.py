{"filter":false,"title":"models.py","tooltip":"/django/polls/models.py","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":3,"column":0},"end":{"row":14,"column":42},"action":"insert","lines":["from django.db import models","","","class Question(models.Model):","    question_text = models.CharField(max_length=200)","    pub_date = models.DateTimeField('date published')","","","class Choice(models.Model):","    question = models.ForeignKey(Question, on_delete=models.CASCADE)","    choice_text = models.CharField(max_length=200)","    votes = models.IntegerField(default=0)"],"id":2}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":3}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":33},"action":"insert","lines":["def __str__(self):","        return self.question_text"],"id":4}],[{"start":{"row":15,"column":42},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":17,"column":31},"action":"insert","lines":["def __str__(self):","        return self.choice_text"],"id":6}],[{"start":{"row":17,"column":31},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]},{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":8},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":22,"column":42},"action":"insert","lines":["class Rating(models.Model):","    question = models.ForeignKey(Question, on_delete=models.CASCADE)","    rating_value = models.IntegerField(default=0)","    count = models.IntegerField(default=0)"],"id":9}],[{"start":{"row":10,"column":33},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":11}],[{"start":{"row":11,"column":4},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":13,"column":75},"action":"insert","lines":["def was_published_recently(self):","        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"],"id":13}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":28},"action":"remove","lines":["from django.db import models"],"id":14}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":33},"action":"insert","lines":["import datetime","","from django.db import models","from django.utils import timezone"],"id":15}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":28},"action":"remove","lines":["from django.db import models"],"id":16},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":15},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":15},"end":{"row":3,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1583423277206,"hash":"447167ec36c0a625543e4d91419aab23c95302f2"}