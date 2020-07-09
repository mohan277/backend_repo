{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/create_comment/api_wrapper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post.views.create_comment.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post.views.create_comment.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post.views.create_comment.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post\", test_case=test_case,","        operation_name=\"create_comment\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":52,"column":30},"action":"insert","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from fb_post.utils import create_comment","from rest_framework.response import Response","from raven.utils import json","from django.http import HttpResponse","from fb_post.constants import INVALID_COMMENT_CONTENT, INVALID_POST","from fb_post.exceptions import InvalidCommentContent, InvalidPostException","from django_swagger_utils.drf_server.exceptions import BadRequest","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    user = kwargs['user']","    post_id = kwargs['post_id']","    request_data = kwargs['request_data']","","    try:","        comment_id = create_comment(user_id=user.id, post_id=post_id, comment_content=request_data['content'])","    except InvalidCommentContent:","        raise BadRequest(*INVALID_COMMENT_CONTENT)","    except InvalidPostException:","        raise BadRequest(*INVALID_POST)","","    data = json.dumps({'comment_id': comment_id})","    response = HttpResponse(data, status=201)","    return response","","","    # ---------MOCK IMPLEMENTATION---------","","    # try:","    #     from fb_post.views.create_comment.tests.test_case_01 \\","    #         import TEST_CASE as test_case","    # except ImportError:","    #     from fb_post.views.create_comment.tests.test_case_01 \\","    #         import test_case","","    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","    #     import mock_response","    # try:","    #     from fb_post.views.create_comment.request_response_mocks \\","    #         import RESPONSE_200_JSON","    # except ImportError:","    #     RESPONSE_200_JSON = ''","    # response_tuple = mock_response(","    #     app_name=\"fb_post\", test_case=test_case,","    #     operation_name=\"create_comment\",","    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","    #     group_name=\"\")","    # return response_tuple[1]"]}]]},"ace":{"folds":[],"scrolltop":353,"scrollleft":0,"selection":{"start":{"row":29,"column":0},"end":{"row":29,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":18,"state":"start","mode":"ace/mode/python"}},"timestamp":1588950251976,"hash":"a57ba9b1a71a031a6153cfe8d558da9d85f4a105"}