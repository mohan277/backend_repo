{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/posts_reacted_by_user/api_wrapper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post.views.posts_reacted_by_user.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post.views.posts_reacted_by_user.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post.views.posts_reacted_by_user.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post\", test_case=test_case,","        operation_name=\"posts_reacted_by_user\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":41,"column":30},"action":"insert","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from fb_post.utils import get_posts_reacted_by_user","from rest_framework.response import Response","from raven.utils import json","from django.http import HttpResponse","from django_swagger_utils.drf_server.exceptions import BadRequest","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    user = kwargs['user']","    list_of_post_ids = get_posts_reacted_by_user(user_id=user.id)","","    data = json.dumps(list_of_post_ids)","    response = HttpResponse(data, status=201)","    return response","","    # ---------MOCK IMPLEMENTATION---------","","    # try:","    #     from fb_post.views.get_post_reacted_by_user.tests.test_case_01 \\","    #         import TEST_CASE as test_case","    # except ImportError:","    #     from fb_post.views.get_post_reacted_by_user.tests.test_case_01 \\","    #         import test_case","","    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","    #     import mock_response","    # try:","    #     from fb_post.views.get_post_reacted_by_user.request_response_mocks \\","    #         import RESPONSE_200_JSON","    # except ImportError:","    #     RESPONSE_200_JSON = ''","    # response_tuple = mock_response(","    #     app_name=\"fb_post\", test_case=test_case,","    #     operation_name=\"get_post_reacted_by_user\",","    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","    #     group_name=\"\")","    # return response_tuple[1]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":41,"column":30},"end":{"row":41,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588950485035,"hash":"c7b6e1bc40df7edfa9b9e00dd43746f5001e5805"}