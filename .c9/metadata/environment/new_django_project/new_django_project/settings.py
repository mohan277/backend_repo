{"filter":false,"title":"settings.py","tooltip":"/new_django_project/new_django_project/settings.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":27,"column":17},"end":{"row":27,"column":19},"action":"insert","lines":["\"\""],"id":2}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["*"],"id":3}],[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":40,"column":21},"action":"insert","lines":["'oauth2_provider',","    'rest_framework',"],"id":5}],[{"start":{"row":122,"column":0},"end":{"row":123,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":123,"column":0},"end":{"row":135,"column":1},"action":"insert","lines":["REST_FRAMEWORK = {","    'DEFAULT_AUTHENTICATION_CLASSES': (","        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',","    ),","    'DEFAULT_PERMISSION_CLASSES': (","        'rest_framework.permissions.IsAuthenticated',","    )","}","","OAUTH2_PROVIDER = {","    # this is the list of available scopes","    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}","}"],"id":7}],[{"start":{"row":122,"column":0},"end":{"row":123,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":133,"column":0},"end":{"row":136,"column":1},"action":"remove","lines":["OAUTH2_PROVIDER = {","    # this is the list of available scopes","    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}","}"],"id":10},{"start":{"row":133,"column":0},"end":{"row":141,"column":0},"action":"insert","lines":["OAUTH2_PROVIDER = {","    # this is the list of available scopes","    'SCOPES': {","        'read': 'Read scope',","        'write': 'Write scope',","        'superuser': 'SuperUser scope'","    }","}",""]}]]},"ace":{"folds":[],"scrolltop":2156.5,"scrollleft":0,"selection":{"start":{"row":141,"column":0},"end":{"row":141,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":118,"state":"start","mode":"ace/mode/python"}},"timestamp":1588416507480,"hash":"57425bff07852916f71ba6c99e8930cd57cd0c5d"}