{"filter":false,"title":"middleware.py","tooltip":"/rest/rest_submissions/rest_assignment_002/fb_post/middleware.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":41},"end":{"row":14,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"d639f25e21a5bfafe7768834a55750f405aebeb9","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":41},"action":"insert","lines":["import pytz","","from django.utils import timezone","","class TimezoneMiddleware:","    def __init__(self, get_response):","        self.get_response = get_response","","    def __call__(self, request):","        tzname = request.session.get('django_timezone')","        if tzname:","            timezone.activate(pytz.timezone(tzname))","        else:","            timezone.deactivate()","        return self.get_response(request)"],"id":1}]]},"timestamp":1589468527136}