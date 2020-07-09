{"filter":false,"title":"service_adapter.py","tooltip":"/ib_miniprojects_backend/project_management_portal/adapters/service_adapter.py","ace":{"folds":[],"scrolltop":223,"scrollleft":0,"selection":{"start":{"row":34,"column":0},"end":{"row":34,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/python"}},"hash":"52efae23265a244396278005279224fa9968ae55","undoManager":{"mark":26,"position":26,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":18},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["class ServiceAdapter:","","    @property","    def auth_service(self):","        from .auth_service import AuthService","        return AuthService()","","","    @property","    def reactions_service(self):","        from .reactions_service import ReactionsService","        return ReactionsService()","","def get_service_adapter():","    return ServiceAdapter()","","",""],"id":20}],[{"start":{"row":24,"column":28},"end":{"row":31,"column":0},"action":"remove","lines":["","","","    @property","    def reactions_service(self):","        from .reactions_service import ReactionsService","        return ReactionsService()",""],"id":21}],[{"start":{"row":24,"column":28},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]},{"start":{"row":25,"column":8},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"remove","lines":["        "],"id":23},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"remove","lines":["        "]}],[{"start":{"row":25,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["    @property","    def auth_service(self):","        from .auth_service import AuthService","        return AuthService()",""],"id":24}],[{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":20},"action":"remove","lines":["auth_service"],"id":26},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["v"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["a"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["l"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":11},"action":"remove","lines":["val"],"id":27},{"start":{"row":27,"column":8},"end":{"row":27,"column":26},"action":"insert","lines":["validate_admin_dto"]}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"remove","lines":["o"],"id":28},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"remove","lines":["t"]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":["d"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"remove","lines":["_"]}],[{"start":{"row":28,"column":14},"end":{"row":28,"column":26},"action":"remove","lines":["auth_service"],"id":29},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["v"]},{"start":{"row":28,"column":15},"end":{"row":28,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":28,"column":14},"end":{"row":28,"column":16},"action":"remove","lines":["va"],"id":30},{"start":{"row":28,"column":14},"end":{"row":28,"column":28},"action":"insert","lines":["validate_admin"]}],[{"start":{"row":28,"column":36},"end":{"row":28,"column":47},"action":"remove","lines":["AuthService"],"id":31},{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":["V"]}],[{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"remove","lines":["V"],"id":32},{"start":{"row":28,"column":36},"end":{"row":28,"column":49},"action":"insert","lines":["ValidateAdmin"]}],[{"start":{"row":29,"column":15},"end":{"row":29,"column":26},"action":"remove","lines":["AuthService"],"id":33},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["V"]},{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["a"]}],[{"start":{"row":29,"column":15},"end":{"row":29,"column":17},"action":"remove","lines":["Va"],"id":34},{"start":{"row":29,"column":15},"end":{"row":29,"column":28},"action":"insert","lines":["ValidateAdmin"]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":35}],[{"start":{"row":34,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["def get_service_adapter():","    return ServiceAdapter()",""],"id":36}],[{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":23},"action":"remove","lines":["service_adapter"],"id":38},{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["i"]},{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["s"]},{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["_"]},{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["v"]},{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["a"]},{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["l"]},{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["i"]}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["d"],"id":39},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["_"]},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["a"]},{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["d"]},{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["m"]}],[{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["i"],"id":40},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""],"id":41},{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":35,"column":0},"end":{"row":37,"column":0},"action":"remove","lines":["def get_is_valid_admin():","    return ServiceAdapter()",""],"id":42},{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["v"],"id":43},{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"insert","lines":["v"]}],[{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"remove","lines":["v"],"id":44},{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["v"]}]]},"timestamp":1593617644020}