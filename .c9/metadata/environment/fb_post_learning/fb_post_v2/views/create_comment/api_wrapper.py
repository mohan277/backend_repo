{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post_v2/views/create_comment/api_wrapper.py","undoManager":{"mark":77,"position":77,"stack":[[{"start":{"row":6,"column":33},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":8,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    request_data = kwargs['request_data']","    post_id = request_data['post_id']","    comment_text = request_data['comment_text']","    user = kwargs['user']","    user_id = user.id","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = CreateCommentInteractor(storage=storage)","","    comment_id_dict = interactor.create_comment(","        post_id=post_id,","        comment_text=comment_text,","        user_id=user_id,","        presenter=presenter)","","    response_data = json.dumps(comment_id_dict)","    return HttpResponse(response_data, status=201)",""],"id":5}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":6},"action":"insert","lines":["# "],"id":6},{"start":{"row":31,"column":4},"end":{"row":31,"column":6},"action":"insert","lines":["# "]},{"start":{"row":32,"column":4},"end":{"row":32,"column":6},"action":"insert","lines":["# "]},{"start":{"row":33,"column":4},"end":{"row":33,"column":6},"action":"insert","lines":["# "]},{"start":{"row":34,"column":4},"end":{"row":34,"column":6},"action":"insert","lines":["# "]},{"start":{"row":35,"column":4},"end":{"row":35,"column":6},"action":"insert","lines":["# "]},{"start":{"row":37,"column":4},"end":{"row":37,"column":6},"action":"insert","lines":["# "]},{"start":{"row":38,"column":4},"end":{"row":38,"column":6},"action":"insert","lines":["# "]},{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["# "]},{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["# "]},{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["# "]},{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["# "]},{"start":{"row":43,"column":4},"end":{"row":43,"column":6},"action":"insert","lines":["# "]},{"start":{"row":44,"column":4},"end":{"row":44,"column":6},"action":"insert","lines":["# "]},{"start":{"row":45,"column":4},"end":{"row":45,"column":6},"action":"insert","lines":["# "]},{"start":{"row":46,"column":4},"end":{"row":46,"column":6},"action":"insert","lines":["# "]},{"start":{"row":47,"column":4},"end":{"row":47,"column":6},"action":"insert","lines":["# "]},{"start":{"row":48,"column":4},"end":{"row":48,"column":6},"action":"insert","lines":["# "]},{"start":{"row":49,"column":4},"end":{"row":49,"column":6},"action":"insert","lines":["# "]}],[{"start":{"row":4,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):",""],"id":7}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["P"],"id":8},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["s"],"id":9},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":4,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","","from fb_post_clean_arch.interactors.create_comment_interactor import \\","    CreateCommentInteractor","from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation","from fb_post_clean_arch.storages.storage_implementation import StorageImplementation","from .validator_class import ValidatorClass",""],"id":11}],[{"start":{"row":2,"column":43},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":43},"action":"remove","lines":["from .validator_class import ValidatorClass"],"id":13},{"start":{"row":12,"column":84},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator",""],"id":14}],[{"start":{"row":5,"column":36},"end":{"row":6,"column":0},"action":"remove","lines":["",""],"id":15}],[{"start":{"row":3,"column":11},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":16}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["import json",""],"id":17},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import json",""]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["import json",""],"id":18},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["import json",""]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["import json",""],"id":19},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["import json",""]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["p"],"id":20},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["o"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["s"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["t"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":68},"end":{"row":8,"column":69},"action":"insert","lines":["P"],"id":21},{"start":{"row":8,"column":69},"end":{"row":8,"column":70},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":68},"end":{"row":8,"column":91},"action":"remove","lines":["PoStorageImplementation"],"id":22},{"start":{"row":8,"column":68},"end":{"row":8,"column":93},"action":"insert","lines":["PostStorageImplementation"]}],[{"start":{"row":17,"column":21},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":56},"end":{"row":22,"column":57},"action":"insert","lines":[","],"id":25}],[{"start":{"row":22,"column":57},"end":{"row":22,"column":58},"action":"insert","lines":[" "],"id":26},{"start":{"row":22,"column":58},"end":{"row":22,"column":59},"action":"insert","lines":["p"]},{"start":{"row":22,"column":59},"end":{"row":22,"column":60},"action":"insert","lines":["r"]},{"start":{"row":22,"column":60},"end":{"row":22,"column":61},"action":"insert","lines":["e"]},{"start":{"row":22,"column":61},"end":{"row":22,"column":62},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":58},"end":{"row":22,"column":62},"action":"remove","lines":["pres"],"id":27},{"start":{"row":22,"column":58},"end":{"row":22,"column":67},"action":"insert","lines":["presenter"]}],[{"start":{"row":22,"column":67},"end":{"row":22,"column":68},"action":"insert","lines":["="],"id":28},{"start":{"row":22,"column":68},"end":{"row":22,"column":69},"action":"insert","lines":["p"]},{"start":{"row":22,"column":69},"end":{"row":22,"column":70},"action":"insert","lines":["r"]},{"start":{"row":22,"column":70},"end":{"row":22,"column":71},"action":"insert","lines":["e"]},{"start":{"row":22,"column":71},"end":{"row":22,"column":72},"action":"insert","lines":["s"]},{"start":{"row":22,"column":72},"end":{"row":22,"column":73},"action":"insert","lines":["e"]}],[{"start":{"row":22,"column":68},"end":{"row":22,"column":73},"action":"remove","lines":["prese"],"id":29},{"start":{"row":22,"column":68},"end":{"row":22,"column":77},"action":"insert","lines":["presenter"]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":57},"action":"insert","lines":["self, user_id : int, post_id: int, comment_content: str):"],"id":30}],[{"start":{"row":29,"column":56},"end":{"row":29,"column":57},"action":"remove","lines":[":"],"id":31},{"start":{"row":29,"column":55},"end":{"row":29,"column":56},"action":"remove","lines":[")"]},{"start":{"row":29,"column":54},"end":{"row":29,"column":55},"action":"remove","lines":["r"]},{"start":{"row":29,"column":53},"end":{"row":29,"column":54},"action":"remove","lines":["t"]},{"start":{"row":29,"column":52},"end":{"row":29,"column":53},"action":"remove","lines":["s"]},{"start":{"row":29,"column":51},"end":{"row":29,"column":52},"action":"remove","lines":[" "]},{"start":{"row":29,"column":50},"end":{"row":29,"column":51},"action":"remove","lines":[":"]}],[{"start":{"row":29,"column":35},"end":{"row":29,"column":50},"action":"remove","lines":["comment_content"],"id":32}],[{"start":{"row":26,"column":8},"end":{"row":26,"column":20},"action":"remove","lines":["comment_text"],"id":33},{"start":{"row":26,"column":8},"end":{"row":26,"column":23},"action":"insert","lines":["comment_content"]}],[{"start":{"row":28,"column":8},"end":{"row":28,"column":27},"action":"remove","lines":["presenter=presenter"],"id":34},{"start":{"row":28,"column":4},"end":{"row":28,"column":8},"action":"remove","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":24},"end":{"row":28,"column":0},"action":"remove","lines":["",""]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":[","]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":35},"action":"remove","lines":["self, user_id : int, post_id: int, "],"id":35}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":36},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"remove","lines":["t"],"id":37},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"remove","lines":["x"]},{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"remove","lines":["e"]},{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":["c"],"id":38},{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":["o"]},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["m"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["m"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["e"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["n"]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"remove","lines":["t"],"id":39},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"remove","lines":["n"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"remove","lines":["e"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"remove","lines":["m"]},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"remove","lines":["m"]}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["n"],"id":40},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["t"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["e"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["n"]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["t"],"id":41},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["x"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["e"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["c"],"id":42},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["o"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":15},"action":"remove","lines":["comment_con"],"id":43},{"start":{"row":15,"column":4},"end":{"row":15,"column":19},"action":"insert","lines":["comment_content"]}],[{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"remove","lines":["t"],"id":44},{"start":{"row":26,"column":34},"end":{"row":26,"column":35},"action":"remove","lines":["x"]},{"start":{"row":26,"column":33},"end":{"row":26,"column":34},"action":"remove","lines":["e"]},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"remove","lines":["t"]}],[{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"insert","lines":["c"],"id":45},{"start":{"row":26,"column":33},"end":{"row":26,"column":34},"action":"insert","lines":["o"]},{"start":{"row":26,"column":34},"end":{"row":26,"column":35},"action":"insert","lines":["n"]},{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"insert","lines":["t"]},{"start":{"row":26,"column":36},"end":{"row":26,"column":37},"action":"insert","lines":["e"]},{"start":{"row":26,"column":37},"end":{"row":26,"column":38},"action":"insert","lines":["n"]},{"start":{"row":26,"column":38},"end":{"row":26,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":23},"action":"remove","lines":["fb_post_clean_arch"],"id":46},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["f"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":7},"action":"remove","lines":["fb"],"id":47},{"start":{"row":7,"column":5},"end":{"row":7,"column":15},"action":"insert","lines":["fb_post_v2"]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":23},"action":"remove","lines":["fb_post_clean_arch"],"id":48},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["f"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["b"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":8},"action":"remove","lines":["fb_"],"id":49},{"start":{"row":8,"column":5},"end":{"row":8,"column":15},"action":"insert","lines":["fb_post_v2"]}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":23},"action":"remove","lines":["fb_post_clean_arch"],"id":50},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["f"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":7},"action":"remove","lines":["fb"],"id":51},{"start":{"row":5,"column":5},"end":{"row":5,"column":15},"action":"insert","lines":["fb_post_v2"]}],[{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["a"],"id":52},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["t"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["a"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["d"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["_"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["t"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["s"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["e"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":["u"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["q"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["e"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["k"],"id":53},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["w"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["a"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["r"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["f"]}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["f"],"id":54}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":18},"action":"remove","lines":["kwar"],"id":55},{"start":{"row":14,"column":14},"end":{"row":14,"column":20},"action":"insert","lines":["kwargs"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":11},"action":"remove","lines":["import json"],"id":56},{"start":{"row":0,"column":0},"end":{"row":0,"column":28},"action":"insert","lines":["from raven.utils import json"]}],[{"start":{"row":12,"column":33},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["p"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["i"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"],"id":58}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":11},"action":"insert","lines":["()"],"id":59}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["\"\""],"id":60}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["&"],"id":61}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["*"],"id":62},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["1"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["0"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["0"]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["    print(\"&\"*100)",""],"id":63}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["    print(\"&\"*100)",""],"id":64}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["0"],"id":65},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["0"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["1"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["*"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["\""]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["&"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["\""]}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["k"],"id":66},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["w"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["a"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["g"],"id":67}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":13},"action":"remove","lines":["kwa"],"id":68},{"start":{"row":14,"column":10},"end":{"row":14,"column":16},"action":"insert","lines":["kwargs"]}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":18},"action":"insert","lines":["[]"],"id":69}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["p"],"id":70},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["o"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":20},"action":"remove","lines":["pos"],"id":71},{"start":{"row":14,"column":17},"end":{"row":14,"column":24},"action":"insert","lines":["post_id"]}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["'"],"id":72}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["'"],"id":73}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":6},"action":"insert","lines":["# "],"id":74},{"start":{"row":14,"column":4},"end":{"row":14,"column":6},"action":"insert","lines":["# "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":6},"action":"insert","lines":["# "]}],[{"start":{"row":8,"column":60},"end":{"row":8,"column":64},"action":"remove","lines":["Post"],"id":75},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["C"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["o"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["m"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["m"]},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["e"]},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["n"]},{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":18},"action":"remove","lines":["Post"],"id":76},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["C"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["o"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["m"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["m"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["e"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["n"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["t"],"id":77},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["s"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["o"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["c"],"id":78},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["o"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["m"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["m"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["e"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["n"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":6},"action":"remove","lines":["# "],"id":79},{"start":{"row":14,"column":4},"end":{"row":14,"column":6},"action":"remove","lines":["# "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":6},"action":"remove","lines":["# "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":18},"end":{"row":15,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1592931377048,"hash":"fc2d439e54ba0940100da91637e646d2c0e72671"}