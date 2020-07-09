{"filter":false,"title":"get_post.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/utils/get_post.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["# Task 13","def get_post(post_id):","","    try:","        post_objs = list(Post.objects.filter(id=post_id).select_related('posted_by').prefetch_related('comment_set','comment_set__commented_by','comment_set__reaction_set','reaction_set'))","        return post_details(post_objs[0])","    except:","        raise InvalidPostException","","def post_details(post_obj):","","    comment_objs = post_obj.comment_set.all()","    comments_list = []","    for comment_obj in comment_objs:","","        replies = []","        for reply in comment_objs:","            if reply.parent_comment_id == comment_obj.id:","                reply_dict = {","                    'comment_id': reply.id,","                    'commenter': {","                        'user_id': reply.commented_by.id,","                        'name': reply.commented_by.name,","                        'profile_pic': reply.commented_by.profile_pic","                    },","                    'commented_at': str(reply.commented_at)[:-6],","                    'comment_content': reply.content,","                    'reactions': {","                        'count': len(reply.reaction_set.all()),","                        'type': list(dict.fromkeys([reaction.reaction for reaction in reply.reaction_set.all()]))","                    },","                }","                replies.append(reply_dict)","","        if comment_obj.parent_comment_id is None:","            comment_dict = {","                'comment_id': comment_obj.id,","                'commenter': {","                    'user_id': comment_obj.commented_by.id,","                    'name': comment_obj.commented_by.name,","                    'profile_pic': comment_obj.commented_by.profile_pic","                },","            'commented_at': str(comment_obj.commented_at)[:-6],","            'comment_content':  comment_obj.content,","            'reactions': {","                'count': len(comment_obj.reaction_set.all()),","                'type': list(dict.fromkeys([reaction.reaction for reaction in comment_obj.reaction_set.all()]))","            },","            'replies_count': len(replies),","            'replies': replies","            }","            comments_list.append(comment_dict)","","    post_details_dict = {","        'post_id': post_obj.id,","        'posted_by': {","            'name': post_obj.posted_by.name,","            'user_id': post_obj.posted_by.id,","            'profile_pic': post_obj.posted_by.profile_pic","        },","        'posted_at': str(post_obj.posted_at)[:-6],","        'post_content': post_obj.content,","        'reactions': {","            'count': len(post_obj.reaction_set.all()),","            'type': list(dict.fromkeys([reaction.reaction for reaction in post_obj.reaction_set.all()]))","","        },","","        'comments':comments_list,","        \"comments_count\": len(comments_list)","    }","    return post_details_dict",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["from .models import *","from .exceptions import *","from django.db.models import *",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":4},{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"insert","lines":["# "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"insert","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["# "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["# "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["# "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["# "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["# "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"insert","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"remove","lines":["# "],"id":5},{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"remove","lines":["# "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"remove","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"remove","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"remove","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"remove","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"remove","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"remove","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"remove","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"remove","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"remove","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"remove","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"remove","lines":["# "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"remove","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"remove","lines":["# "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"remove","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"remove","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"remove","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"remove","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"remove","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"remove","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"remove","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"remove","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"remove","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"remove","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"remove","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"remove","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"remove","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"remove","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"remove","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"remove","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"remove","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"remove","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"remove","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"remove","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"remove","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"remove","lines":["# "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"remove","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"remove","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"remove","lines":["# "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"remove","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"remove","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"remove","lines":["# "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"remove","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"remove","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"remove","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"remove","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"remove","lines":["# "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":2},"action":"remove","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"remove","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"remove","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"remove","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"remove","lines":["# "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"remove","lines":["# "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"remove","lines":["# "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"remove","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"remove","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"remove","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"remove","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"remove","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"remove","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"remove","lines":["# "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"remove","lines":["# "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"remove","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"remove","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":0,"column":0},"end":{"row":2,"column":30},"action":"remove","lines":["from .models import *","from .exceptions import *","from django.db.models import *"],"id":6},{"start":{"row":0,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["from fb_post.models import Comment","","from .check_for_exceptions import (","    is_valid_user_id,","    is_valid_post_id,","    is_valid_comment_content",")"]}],[{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["t"],"id":7},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":["n"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["e"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"remove","lines":["m"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["m"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["o"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["C"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["P"],"id":8},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["o"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["s"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":21},"action":"remove","lines":["is_valid_user_id,"],"id":9}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":10},{"start":{"row":3,"column":4},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":28},"action":"remove","lines":["is_valid_comment_content"],"id":11},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "]},{"start":{"row":3,"column":21},"end":{"row":4,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":[","]}],[{"start":{"row":7,"column":22},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":7,"column":22},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["i"]},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":6},"action":"remove","lines":["is"],"id":14},{"start":{"row":9,"column":4},"end":{"row":9,"column":20},"action":"insert","lines":["is_valid_post_id"]}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":22},"action":"insert","lines":["()"],"id":15}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["p"],"id":16},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["o"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["s"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":25},"action":"remove","lines":["post"],"id":17},{"start":{"row":9,"column":21},"end":{"row":9,"column":28},"action":"insert","lines":["post_id"]}],[{"start":{"row":10,"column":4},"end":{"row":11,"column":4},"action":"remove","lines":["try:","    "],"id":18}],[{"start":{"row":12,"column":4},"end":{"row":14,"column":0},"action":"remove","lines":["except:","        raise InvalidPostException",""],"id":19}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":21}],[{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"remove","lines":["r"],"id":22},{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"remove","lines":["e"]},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"remove","lines":["t"]},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"remove","lines":["l"]},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"remove","lines":["i"]},{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"remove","lines":["f"]}],[{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["g"],"id":23},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["e"]},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":65},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":10,"column":38},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "],"id":26},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":35},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":65},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":12,"column":0},"end":{"row":12,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":12,"column":54},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":13,"column":0},"end":{"row":13,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":[" "],"id":30}],[{"start":{"row":13,"column":57},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":14,"column":0},"end":{"row":14,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"remove","lines":["]"],"id":32},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"remove","lines":["0"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"remove","lines":["["]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["s"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["s"],"id":33}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":34},{"start":{"row":14,"column":0},"end":{"row":14,"column":12},"action":"remove","lines":["            "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":29,"column":26},"end":{"row":29,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588053452413,"hash":"574d4651cea0838bc4f3dd99659daca248c02b52"}