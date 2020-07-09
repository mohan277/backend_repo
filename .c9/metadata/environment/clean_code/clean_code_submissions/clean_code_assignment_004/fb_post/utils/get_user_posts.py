{"filter":false,"title":"get_user_posts.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/utils/get_user_posts.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["# Task 14","def get_user_posts(user_id):","    user_obj = User.objects.filter(id=user_id)","","    if user_obj:","        post_objs = list(Post.objects.filter(posted_by_id=user_id).select_related('posted_by').prefetch_related('comment_set','comment_set__commented_by','comment_set__reaction_set','reaction_set'))","","        # user_posts_list = []","        # for post_obj in post_objs:","        #     user_posts_list.append(post_details(post_obj))","        # return user_posts_list","        return [post_details(post_obj) for post_obj in post_objs]","","    else:","        raise InvalidUserException",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["from .models import *","from .exceptions import *","from django.db.models import *",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":4},{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"insert","lines":["# "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"insert","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"remove","lines":["# "],"id":5}],[{"start":{"row":9,"column":45},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":10,"column":0},"end":{"row":10,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":10,"column":79},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":11,"column":0},"end":{"row":11,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":10,"column":49},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":11,"column":0},"end":{"row":11,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":12,"column":12},"end":{"row":12,"column":16},"action":"remove","lines":["    "],"id":9},{"start":{"row":12,"column":8},"end":{"row":12,"column":12},"action":"remove","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":46},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":60},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":12,"column":0},"end":{"row":12,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":20},"action":"insert","lines":["    "],"id":11}],[{"start":{"row":11,"column":46},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":12,"column":0},"end":{"row":12,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":20},"action":"remove","lines":["    "],"id":13},{"start":{"row":13,"column":12},"end":{"row":13,"column":16},"action":"remove","lines":["    "]},{"start":{"row":13,"column":8},"end":{"row":13,"column":12},"action":"remove","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":34},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":62},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":13,"column":0},"end":{"row":13,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":10},"action":"insert","lines":["# "],"id":17},{"start":{"row":10,"column":8},"end":{"row":10,"column":10},"action":"insert","lines":["# "]},{"start":{"row":11,"column":8},"end":{"row":11,"column":10},"action":"insert","lines":["# "]},{"start":{"row":12,"column":8},"end":{"row":12,"column":10},"action":"insert","lines":["# "]},{"start":{"row":13,"column":8},"end":{"row":13,"column":10},"action":"insert","lines":["# "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":22,"column":36},"end":{"row":22,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588062982371,"hash":"20221a2a80a610241afdb5460602f5c9916cad10"}