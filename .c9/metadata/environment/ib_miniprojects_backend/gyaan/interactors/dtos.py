{"filter":false,"title":"dtos.py","tooltip":"/ib_miniprojects_backend/gyaan/interactors/dtos.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["\"\"\"","Created on 11/06/20","","@author: revanth","\"\"\"","from dataclasses import dataclass","from typing import List","","from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \\","    UserDetailsDTO, DomainJoinRequestDTO, CompletePostDetails","","","@dataclass","class DomainDetailsDTO:","    domain: DomainDTO","    domain_stats: DomainStatsDTO","    domain_experts: List[UserDetailsDTO]","    join_requests: List[DomainJoinRequestDTO]","    requested_users: List[UserDetailsDTO]","    user_id: int","    is_user_domain_expert: bool","","","@dataclass","class DomainDetailsWithPosts:","    post_details: CompletePostDetails","    domain_details: DomainDetailsDTO",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["\"\"\"","Created on 11/06/20","","@author: revanth","\"\"\"",""],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["","from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \\","    UserDetailsDTO, DomainJoinRequestDTO, CompletePostDetails","",""],"id":3}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":105,"column":0},"action":"insert","lines":["import datetime","from dataclasses import dataclass","from typing import List","","","@dataclass","class DomainDTO:","    domain_id: int","    name: str","    description: str","","","@dataclass","class DomainStatsDTO:","    domain_id: int","    followers_count: int","    posts_count: int","    bookmarked_count: int","","","@dataclass","class UserDetailsDTO:","    user_id: int","    name: str","    profile_pic_url: str","","","@dataclass","class DomainJoinRequestDTO:","    request_id: int","    user_id: int","","","@dataclass","class PostDTO:","    post_id: int","    posted_at: datetime.datetime","    posted_by_id: int","    title: str","    content: str","","","@dataclass","class CommentDTO:","    comment_id: int","    commented_at: datetime.datetime","    commented_by_id: int","    content: str","","","@dataclass","class Tag:","    tag_id: int","    name: str","","","@dataclass","class PostTag:","    post_id: int","    tag_id: int","","","@dataclass","class PostTagDetails:","    tags: List[Tag]","    post_tag_ids: List[PostTag]","","","@dataclass","class PostReactionsCount:","    post_id: int","    reactions_count: int","","","@dataclass","class CommentReactionsCount:","    comment_id: int","    reactions_count: int","","","@dataclass","class PostCommentsCount:","    post_id: int","    comments_count: int","","","@dataclass","class CommentRepliesCount:","    comment_id: int","    replies_count: int","","","@dataclass()","class CompletePostDetails:","    post_dtos: List[PostDTO]","    post_reaction_counts: List[PostReactionsCount]","    comment_reaction_counts: List[CommentReactionsCount]","    comment_counts: List[PostCommentsCount]","    reply_counts: List[CommentRepliesCount]","    comment_dtos: List[CommentDTO]","    post_tag_ids: List[PostTag]","    tags: List[Tag]","    users_dtos: List[UserDetailsDTO]",""],"id":5}],[{"start":{"row":3,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["from dataclasses import dataclass","from typing import List",""],"id":7}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["import datetime",""],"id":8},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["import datetime",""]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["import datetime",""],"id":9},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["import datetime",""]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from typing import List",""],"id":10},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["from typing import List",""]}]]},"ace":{"folds":[],"scrolltop":1748,"scrollleft":0,"selection":{"start":{"row":114,"column":0},"end":{"row":114,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":101,"state":"start","mode":"ace/mode/python"}},"timestamp":1592389926777,"hash":"d16c032f36a74b9913fca0f956c301e472dc0141"}