{"filter":false,"title":"react_to_post.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/utils/react_to_post.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":0,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["from .models import *","from .exceptions import *","from django.db.models import *","",""],"id":24},{"start":{"row":0,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["from fb_post.models import Comment","","from .check_for_exceptions import (","    is_valid_user_id,","    is_valid_post_id,","    is_valid_comment_content",")"]}],[{"start":{"row":6,"column":1},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":27},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["o"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["r"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":28}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":[" "],"id":29},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["m"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["r"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":["o"]}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"],"id":30},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":31},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["f"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":7},"action":"remove","lines":["fb"],"id":32},{"start":{"row":2,"column":5},"end":{"row":2,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["."],"id":33}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["c"],"id":34},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["o"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["n"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["t"],"id":35}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["s"],"id":36},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":18},"action":"remove","lines":["const"],"id":37},{"start":{"row":2,"column":13},"end":{"row":2,"column":22},"action":"insert","lines":["constants"]}],[{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":[" "],"id":38},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["i"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["m"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["p"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["o"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["r"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":[" "],"id":39}],[{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["t"],"id":40},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":["n"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["e"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"remove","lines":["m"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["m"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["o"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["C"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["R"],"id":41},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["e"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["a"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":30},"action":"remove","lines":["Rea"],"id":42},{"start":{"row":0,"column":27},"end":{"row":0,"column":35},"action":"insert","lines":["Reaction"]}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["R"],"id":43}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"remove","lines":["R"],"id":44},{"start":{"row":2,"column":30},"end":{"row":2,"column":47},"action":"insert","lines":["ReactionChoices()"]}],[{"start":{"row":2,"column":45},"end":{"row":2,"column":47},"action":"remove","lines":["()"],"id":45}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":28},"action":"remove","lines":["comment_content"],"id":46},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["r"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["e"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["a"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["c"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["t"],"id":47},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["i"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["n"],"id":48},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["_"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["y"],"id":49},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["p"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["o"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["e"],"id":50},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"remove","lines":["o"]}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["e"],"id":51}],[{"start":{"row":14,"column":51},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":52}],[{"start":{"row":14,"column":51},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":18,"column":26},"action":"insert","lines":["is_valid_user_id,","    is_valid_post_id,","    is_valid_reaction_type"],"id":54}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":[","],"id":55}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":22},"action":"insert","lines":["()"],"id":56}],[{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"remove","lines":[","],"id":57}],[{"start":{"row":17,"column":20},"end":{"row":17,"column":22},"action":"insert","lines":["()"],"id":58}],[{"start":{"row":18,"column":26},"end":{"row":18,"column":28},"action":"insert","lines":["()"],"id":59}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["u"],"id":60},{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["s"]},{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"insert","lines":["e"]},{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":25},"action":"remove","lines":["user"],"id":61},{"start":{"row":16,"column":21},"end":{"row":16,"column":28},"action":"insert","lines":["user_id"]}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["p"],"id":62},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":23},"action":"remove","lines":["po"],"id":63},{"start":{"row":17,"column":21},"end":{"row":17,"column":28},"action":"insert","lines":["post_id"]}],[{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["r"],"id":64},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["e"]},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["a"]},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["c"]},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":27},"end":{"row":18,"column":32},"action":"remove","lines":["react"],"id":65},{"start":{"row":18,"column":27},"end":{"row":18,"column":40},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":22,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["","    if User.objects.filter(id=user_id).exists() is False:","        raise InvalidUserException","","    if Post.objects.filter(id=post_id).exists() is False:","        raise InvalidPostException","","    if reaction_type not in REACTIONS_LIST:","        raise InvalidReactionTypeException",""],"id":66}],[{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["t"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["r"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["y"]}],[{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":[":"],"id":68}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"insert","lines":["    "],"id":69}],[{"start":{"row":21,"column":47},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":70},{"start":{"row":22,"column":0},"end":{"row":22,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":23,"column":41},"end":{"row":23,"column":42},"action":"remove","lines":[" "],"id":71},{"start":{"row":23,"column":40},"end":{"row":23,"column":41},"action":"remove","lines":[" "]},{"start":{"row":23,"column":36},"end":{"row":23,"column":40},"action":"remove","lines":["    "]},{"start":{"row":23,"column":32},"end":{"row":23,"column":36},"action":"remove","lines":["    "]},{"start":{"row":23,"column":28},"end":{"row":23,"column":32},"action":"remove","lines":["    "]},{"start":{"row":23,"column":24},"end":{"row":23,"column":28},"action":"remove","lines":["    "]},{"start":{"row":23,"column":20},"end":{"row":23,"column":24},"action":"remove","lines":["    "]},{"start":{"row":23,"column":16},"end":{"row":23,"column":20},"action":"remove","lines":["    "]},{"start":{"row":23,"column":12},"end":{"row":23,"column":16},"action":"remove","lines":["    "]},{"start":{"row":23,"column":8},"end":{"row":23,"column":12},"action":"remove","lines":["    "]},{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":72},{"start":{"row":22,"column":34},"end":{"row":23,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":[" "],"id":73}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "],"id":74},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["e"],"id":75},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["s"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["l"]}],[{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["x"],"id":76},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["c"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"remove","lines":["exce"],"id":77},{"start":{"row":30,"column":4},"end":{"row":30,"column":10},"action":"insert","lines":["except"]}],[{"start":{"row":21,"column":45},"end":{"row":21,"column":46},"action":"remove","lines":["r"],"id":78},{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"remove","lines":["e"]},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"remove","lines":["t"]},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"remove","lines":["l"]},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"remove","lines":["i"]},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"remove","lines":["f"]}],[{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":["g"],"id":79},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"remove","lines":["r"],"id":80}],[{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":["e"],"id":81},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["y"]},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":["y"]}],[{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"remove","lines":["y"],"id":82},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"remove","lines":["y"]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["t"],"id":83}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":84},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"remove","lines":["0"],"id":85},{"start":{"row":25,"column":27},"end":{"row":25,"column":29},"action":"remove","lines":["[]"]}],[{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["0"],"id":86},{"start":{"row":26,"column":28},"end":{"row":26,"column":30},"action":"remove","lines":["[]"]}],[{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"remove","lines":["0"],"id":87},{"start":{"row":28,"column":28},"end":{"row":28,"column":30},"action":"remove","lines":["[]"]}],[{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"remove","lines":["0"],"id":88},{"start":{"row":29,"column":28},"end":{"row":29,"column":30},"action":"remove","lines":["[]"]}],[{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":89}],[{"start":{"row":34,"column":0},"end":{"row":35,"column":33},"action":"insert","lines":["def for_updating_or_deleting_reaction_if_reaction_exists(","    reaction_obj, reaction_type):"],"id":90}],[{"start":{"row":34,"column":50},"end":{"row":34,"column":51},"action":"insert","lines":["f"],"id":91},{"start":{"row":34,"column":51},"end":{"row":34,"column":52},"action":"insert","lines":["o"]},{"start":{"row":34,"column":52},"end":{"row":34,"column":53},"action":"insert","lines":["r"]},{"start":{"row":34,"column":53},"end":{"row":34,"column":54},"action":"insert","lines":["_"]}],[{"start":{"row":34,"column":54},"end":{"row":34,"column":55},"action":"insert","lines":["p"],"id":92},{"start":{"row":34,"column":55},"end":{"row":34,"column":56},"action":"insert","lines":["o"]}],[{"start":{"row":34,"column":56},"end":{"row":34,"column":57},"action":"insert","lines":["s"],"id":93},{"start":{"row":34,"column":57},"end":{"row":34,"column":58},"action":"insert","lines":["t"]},{"start":{"row":34,"column":58},"end":{"row":34,"column":59},"action":"insert","lines":["_"]}],[{"start":{"row":22,"column":51},"end":{"row":23,"column":0},"action":"remove","lines":["",""],"id":94}],[{"start":{"row":22,"column":51},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":95},{"start":{"row":23,"column":0},"end":{"row":23,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":12},"action":"remove","lines":["    "],"id":96}],[{"start":{"row":23,"column":8},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":97},{"start":{"row":24,"column":0},"end":{"row":24,"column":8},"action":"insert","lines":["        "]},{"start":{"row":24,"column":8},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":24,"column":8},"end":{"row":25,"column":33},"action":"insert","lines":["def for_updating_or_deleting_reaction_if_reaction_for_post_exists(","    reaction_obj, reaction_type):"],"id":98}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":[" "],"id":99},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"remove","lines":["f"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"remove","lines":["e"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"remove","lines":["d"]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":100},{"start":{"row":24,"column":70},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":70},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":101},{"start":{"row":25,"column":0},"end":{"row":25,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"remove","lines":[":"],"id":102}],[{"start":{"row":27,"column":8},"end":{"row":32,"column":35},"action":"remove","lines":["if reaction_obj:","            if reaction_obj.reaction == reaction_type:","                reaction_obj.delete()","            else:","                reaction_obj.reaction = reaction_type","                reaction_obj.save()"],"id":103}],[{"start":{"row":33,"column":33},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":104},{"start":{"row":34,"column":0},"end":{"row":34,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":34,"column":8},"end":{"row":39,"column":35},"action":"insert","lines":["if reaction_obj:","            if reaction_obj.reaction == reaction_type:","                reaction_obj.delete()","            else:","                reaction_obj.reaction = reaction_type","                reaction_obj.save()"],"id":105}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":106},{"start":{"row":32,"column":66},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":107},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"remove","lines":["    "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":108},{"start":{"row":32,"column":95},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":32,"column":95},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":109},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":20},"action":"remove","lines":["if reaction_obj:"],"id":110},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":32,"column":95},"end":{"row":33,"column":0},"action":"remove","lines":["",""],"id":111}],[{"start":{"row":32,"column":95},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":112},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":8},"action":"remove","lines":["    "],"id":113}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":8},"action":"remove","lines":["    "],"id":114}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"remove","lines":["    "],"id":115}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":8},"action":"remove","lines":["    "],"id":116}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"remove","lines":["    "],"id":117}],[{"start":{"row":28,"column":11},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":118},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"remove","lines":["        "],"id":119},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"remove","lines":["        "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"remove","lines":["        "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"remove","lines":["        "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":65},"action":"remove","lines":["REACTIONS_LIST = [reaction.value for reaction in ReactionChoices]"],"id":120},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]},{"start":{"row":8,"column":1},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":66},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":121},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":122},{"start":{"row":23,"column":40},"end":{"row":24,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":23,"column":40},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":123},{"start":{"row":24,"column":0},"end":{"row":24,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":12},"action":"remove","lines":["            "],"id":124}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":1},"end":{"row":8,"column":1},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588004789869,"hash":"7018f77113a53470f9c9b5f66c44752b33f4b687"}