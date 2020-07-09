{"filter":false,"title":"get_reaction_metrics.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/utils/get_reaction_metrics.py","undoManager":{"mark":71,"position":71,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["# Task 8","def get_reaction_metrics(post_id):","","    if Post.objects.filter(id=post_id).exists() is False:","        raise InvalidPostException","","    reaction_obj = Reaction.objects.filter(","        post_id=post_id).values_list('reaction')","    return dict(reaction_obj.annotate(Count('reaction')))",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["from .models import *","from .exceptions import *","from django.db.models import *",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":4},{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"insert","lines":["# "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"remove","lines":["# "],"id":5},{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"remove","lines":["# "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"remove","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"remove","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"remove","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"remove","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"remove","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"remove","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"remove","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["f"],"id":6},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":7},"action":"remove","lines":["fb"],"id":7},{"start":{"row":0,"column":5},"end":{"row":0,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["*"],"id":8}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["R"],"id":9},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":29},"action":"remove","lines":["Re"],"id":10},{"start":{"row":0,"column":27},"end":{"row":0,"column":35},"action":"insert","lines":["Reaction"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":25},"action":"remove","lines":["from .exceptions import *"],"id":11}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"],"id":12},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":[" "],"id":14}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":[","],"id":15}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":[","],"id":16},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["o"]}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"],"id":17},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from fb_post.models import Reaction","from ","from django.db.models import *",""],"id":19},{"start":{"row":0,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["from fb_post.models import Comment","","from .check_for_exceptions import (","    is_valid_user_id,","    is_valid_post_id,","    is_valid_comment_content",")",""]}],[{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["t"],"id":20},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":["n"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["e"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"remove","lines":["m"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["m"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["o"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["C"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["R"],"id":21},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":29},"action":"remove","lines":["Re"],"id":22},{"start":{"row":0,"column":27},"end":{"row":0,"column":35},"action":"insert","lines":["Reaction"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":21},"action":"remove","lines":["is_valid_user_id,"],"id":23},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "]},{"start":{"row":2,"column":35},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":28},"action":"remove","lines":["is_valid_comment_content"],"id":24},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "]},{"start":{"row":3,"column":21},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":[","],"id":25}],[{"start":{"row":8,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["","    if Post.objects.filter(id=post_id).exists() is False:","        raise InvalidPostException",""],"id":26},{"start":{"row":7,"column":34},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":34},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["i"],"id":28},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":6},"action":"remove","lines":["is"],"id":29},{"start":{"row":9,"column":4},"end":{"row":9,"column":22},"action":"insert","lines":["is_valid_post_id()"]}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["p"],"id":30},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["o"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["s"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":25},"action":"remove","lines":["post"],"id":31},{"start":{"row":9,"column":21},"end":{"row":9,"column":28},"action":"insert","lines":["post_id"]}],[{"start":{"row":9,"column":29},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":34},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":35},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["d"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["j"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":7},"action":"remove","lines":["dj"],"id":36},{"start":{"row":2,"column":5},"end":{"row":2,"column":11},"action":"insert","lines":["django"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["."],"id":37},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["d"],"id":38},{"start":{"row":2,"column":12},"end":{"row":2,"column":14},"action":"insert","lines":["db"]}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["."],"id":39},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["m"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":17},"action":"remove","lines":["mo"],"id":40},{"start":{"row":2,"column":15},"end":{"row":2,"column":21},"action":"insert","lines":["models"]}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":[" "],"id":41},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["i"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["m"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["p"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":22},"end":{"row":2,"column":26},"action":"remove","lines":["impo"],"id":42},{"start":{"row":2,"column":22},"end":{"row":2,"column":28},"action":"insert","lines":["import"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["C"],"id":44}],[{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"remove","lines":["C"],"id":45},{"start":{"row":2,"column":29},"end":{"row":2,"column":34},"action":"insert","lines":["Count"]}],[{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":["r"],"id":46},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":["e"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"remove","lines":["t"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"remove","lines":["l"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"remove","lines":["i"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"remove","lines":["f"]}],[{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["g"],"id":47},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":["e"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["t"],"id":48},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["r"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["y"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":[":"]}],[{"start":{"row":12,"column":8},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":4},"end":{"row":14,"column":4},"action":"remove","lines":["try:","        ","    "],"id":50}],[{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":52},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":40},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":40},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":54},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":40},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":40},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":56},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["s"],"id":57}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["s"],"id":58}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"remove","lines":["s"],"id":59},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"remove","lines":["j"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"remove","lines":["b"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"remove","lines":["o"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["t"],"id":60},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["y"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":16},"action":"remove","lines":["reaction_typ"],"id":61},{"start":{"row":13,"column":4},"end":{"row":13,"column":17},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["_"],"id":62},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["c"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["o"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["u"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["n"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["r"],"id":63}],[{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["t"],"id":64}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["s"],"id":65}],[{"start":{"row":15,"column":29},"end":{"row":15,"column":57},"action":"remove","lines":[".annotate(Count('reaction'))"],"id":66}],[{"start":{"row":14,"column":48},"end":{"row":14,"column":76},"action":"insert","lines":[".annotate(Count('reaction'))"],"id":67}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["s"],"id":68},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["j"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["b"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["o"]}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["t"],"id":69},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["y"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["p"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["e"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":30},"action":"remove","lines":["reaction_types"],"id":70},{"start":{"row":15,"column":16},"end":{"row":15,"column":36},"action":"insert","lines":["reaction_types_count"]}],[{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"remove","lines":["t"],"id":71},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"remove","lines":["e"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"remove","lines":["g"]}],[{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":["f"],"id":72},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":["i"]},{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["l"]},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["t"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":["e"]},{"start":{"row":13,"column":49},"end":{"row":13,"column":50},"action":"insert","lines":["r"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":50},"end":{"row":13,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588046413688,"hash":"bf28be9d7caaea42ba7730b68b047b9fb53d68e8"}