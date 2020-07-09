{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/delete_post/api_wrapper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post.views.delete_post.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post.views.delete_post.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post.views.delete_post.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post\", test_case=test_case,","        operation_name=\"delete_post\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":47,"column":30},"action":"insert","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from fb_post.utils import delete_post","from rest_framework.response import Response","from raven.utils import json","from django.http import HttpResponse","from fb_post.constants import USER_CANNOT_DELETE_POST, INVALID_POST","from fb_post.exceptions import UserCannotDeletePostException, InvalidPostException","from django_swagger_utils.drf_server.exceptions import BadRequest","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    post_id = kwargs['post_id']","    user = kwargs['user']","","    try:","        delete_post(user_id=user.id, post_id=post_id)","    except InvalidPostException:","        raise BadRequest(*INVALID_POST)","    except UserCannotDeletePostException:","        raise BadRequest(*USER_CANNOT_DELETE_POST)","","","    # ---------MOCK IMPLEMENTATION---------","","    # try:","    #     from fb_post.views.delete_post.tests.test_case_01 \\","    #         import TEST_CASE as test_case","    # except ImportError:","    #     from fb_post.views.delete_post.tests.test_case_01 \\","    #         import test_case","","    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","    #     import mock_response","    # try:","    #     from fb_post.views.delete_post.request_response_mocks \\","    #         import RESPONSE_200_JSON","    # except ImportError:","    #     RESPONSE_200_JSON = ''","    # response_tuple = mock_response(","    #     app_name=\"fb_post\", test_case=test_case,","    #     operation_name=\"delete_post\",","    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","    #     group_name=\"\")","    # return response_tuple[1]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":25},"end":{"row":16,"column":25},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":6,"state":"start","mode":"ace/mode/python"}},"timestamp":1588950415285,"hash":"15549d1f53a2fc8e89ab6099ba1962eb58fcb2ea"}