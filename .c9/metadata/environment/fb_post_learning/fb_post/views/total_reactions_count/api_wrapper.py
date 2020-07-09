{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/total_reactions_count/api_wrapper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post.views.total_reactions_count.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post.views.total_reactions_count.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post.views.total_reactions_count.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post\", test_case=test_case,","        operation_name=\"total_reactions_count\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":40,"column":30},"action":"insert","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from fb_post.utils import get_total_reaction_count","from rest_framework.response import Response","from raven.utils import json","from django.http import HttpResponse","from django_swagger_utils.drf_server.exceptions import BadRequest","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    reactions_count = get_total_reaction_count()","","    data = json.dumps(reactions_count)","    response = HttpResponse(data, status=201)","    return response","","    # ---------MOCK IMPLEMENTATION---------","","    # try:","    #     from fb_post.views.get_total_reactions_count.tests.test_case_01 \\","    #         import TEST_CASE as test_case","    # except ImportError:","    #     from fb_post.views.get_total_reactions_count.tests.test_case_01 \\","    #         import test_case","","    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","    #     import mock_response","    # try:","    #     from fb_post.views.get_total_reactions_count.request_response_mocks \\","    #         import RESPONSE_200_JSON","    # except ImportError:","    #     RESPONSE_200_JSON = ''","    # response_tuple = mock_response(","    #     app_name=\"fb_post\", test_case=test_case,","    #     operation_name=\"get_total_reactions_count\",","    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","    #     group_name=\"\")","    # return response_tuple[1]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":40,"column":30},"end":{"row":40,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588950731060,"hash":"ec191d2467dfecae8b3924cc17a58d2e6d3aad8a"}