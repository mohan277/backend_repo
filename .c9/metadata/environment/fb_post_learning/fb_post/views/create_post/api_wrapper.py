{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/create_post/api_wrapper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post.views.create_post.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post.views.create_post.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post.views.create_post.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post\", test_case=test_case,","        operation_name=\"create_post\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":48,"column":30},"action":"insert","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from fb_post.utils import create_post","from rest_framework.response import Response","from raven.utils import json","from django.http import HttpResponse","from fb_post.constants import INVALID_POST_CONTENT","from fb_post.exceptions import InvalidPostContent","from django_swagger_utils.drf_server.exceptions import BadRequest","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    user = kwargs['user']","    request_data = kwargs['request_data']","","    try:","        post_id = create_post(user_id=user.id,post_content=request_data['content'])","    except InvalidPostContent:","        raise BadRequest(*INVALID_POST_CONTENT)","","    data = json.dumps({'post_id': post_id})","    response = HttpResponse(data, status=201)","    return response","","    # ---------MOCK IMPLEMENTATION---------","","    # try:","    #     from fb_post.views.create_post.tests.test_case_01 \\","    #         import TEST_CASE as test_case","    # except ImportError:","    #     from fb_post.views.create_post.tests.test_case_01 \\","    #         import test_case","","    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","    #     import mock_response","    # try:","    #     from fb_post.views.create_post.request_response_mocks \\","    #         import RESPONSE_200_JSON","    # except ImportError:","    #     RESPONSE_200_JSON = ''","    # response_tuple = mock_response(","    #     app_name=\"fb_post\", test_case=test_case,","    #     operation_name=\"create_post\",","    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","    #     group_name=\"\")","    # return response_tuple[1]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":50},"end":{"row":7,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588950367266,"hash":"5e7c789d27193ceab4fff0e74a60707d42474c0e"}