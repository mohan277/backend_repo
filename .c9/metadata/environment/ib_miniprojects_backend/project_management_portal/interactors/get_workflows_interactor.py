{"filter":false,"title":"get_workflows_interactor.py","tooltip":"/ib_miniprojects_backend/project_management_portal/interactors/get_workflows_interactor.py","undoManager":{"mark":44,"position":44,"stack":[[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":2}],[{"start":{"row":14,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["@abstractmethod","    def get_list_of_workflows(self) -> ListOfWorkflowsDto:","        pass",""],"id":3}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["        pass",""],"id":4}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":19},"action":"remove","lines":["    @abstractmethod"],"id":5}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":57},"action":"remove","lines":[" -> ListOfWorkflowsDto"],"id":6}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":74},"action":"remove","lines":["def get_list_of_projects(self, limit: int, offset: int, user_id: int):"],"id":7},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["",""]},{"start":{"row":15,"column":36},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":8},"end":{"row":19,"column":8},"action":"remove","lines":["is_admin = self.storage.is_admin(user_id=user_id)","","        "],"id":20}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":20},"action":"remove","lines":["if is_admin:"],"id":21}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":22},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":23},"action":"remove","lines":["project"],"id":26}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["w"],"id":27},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["o"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["r"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["k"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["f"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["l"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["w"],"id":28}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":29},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":69},"end":{"row":17,"column":70},"action":"remove","lines":["t"],"id":30},{"start":{"row":17,"column":68},"end":{"row":17,"column":69},"action":"remove","lines":["c"]},{"start":{"row":17,"column":67},"end":{"row":17,"column":68},"action":"remove","lines":["e"]},{"start":{"row":17,"column":66},"end":{"row":17,"column":67},"action":"remove","lines":["j"]},{"start":{"row":17,"column":65},"end":{"row":17,"column":66},"action":"remove","lines":["o"]},{"start":{"row":17,"column":64},"end":{"row":17,"column":65},"action":"remove","lines":["r"]},{"start":{"row":17,"column":63},"end":{"row":17,"column":64},"action":"remove","lines":["p"]},{"start":{"row":17,"column":62},"end":{"row":17,"column":63},"action":"remove","lines":["_"]},{"start":{"row":17,"column":61},"end":{"row":17,"column":62},"action":"remove","lines":["n"]},{"start":{"row":17,"column":60},"end":{"row":17,"column":61},"action":"remove","lines":["i"]},{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"remove","lines":["m"]},{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"remove","lines":["d"]},{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"remove","lines":["a"]}],[{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"insert","lines":["w"],"id":31},{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"insert","lines":["o"]},{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"insert","lines":["r"]},{"start":{"row":17,"column":60},"end":{"row":17,"column":61},"action":"insert","lines":["k"]}],[{"start":{"row":17,"column":45},"end":{"row":17,"column":62},"action":"remove","lines":["get_list_of_works"],"id":32},{"start":{"row":17,"column":45},"end":{"row":17,"column":66},"action":"insert","lines":["get_list_of_workflows"]}],[{"start":{"row":18,"column":8},"end":{"row":21,"column":8},"action":"remove","lines":["    limit=limit,","            offset=offset,","            user_id=user_id","        "],"id":33},{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"remove","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":67},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":19,"column":4},"end":{"row":26,"column":4},"action":"remove","lines":["    else:","            list_of_projects_dto = self.storage.get_list_of_member_projects(","                limit=limit,","                offset=offset,","                user_id=user_id","            )","","    "],"id":34}],[{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"remove","lines":["t"],"id":35},{"start":{"row":19,"column":51},"end":{"row":19,"column":52},"action":"remove","lines":["c"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"remove","lines":["e"]},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"remove","lines":["j"]},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"remove","lines":["o"]},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"remove","lines":["r"]},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"remove","lines":["p"]}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["w"],"id":36},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["o"]},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["r"]},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["k"]}],[{"start":{"row":19,"column":34},"end":{"row":19,"column":50},"action":"remove","lines":["get_list_of_work"],"id":37},{"start":{"row":19,"column":34},"end":{"row":19,"column":55},"action":"insert","lines":["get_list_of_workflows"]}],[{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"remove","lines":["s"],"id":38}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"remove","lines":["t"],"id":39},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["c"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["e"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["j"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"remove","lines":["o"]},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"remove","lines":["r"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["w"],"id":40},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":["o"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["r"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["k"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["f"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["l"]},{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":["o"]},{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"insert","lines":["w"]}],[{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"remove","lines":["w"],"id":41}],[{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"insert","lines":["w"],"id":42}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":33},"action":"remove","lines":["list_of_workflows_dto"],"id":43},{"start":{"row":20,"column":12},"end":{"row":20,"column":33},"action":"insert","lines":["list_of_workflows_dto"]}],[{"start":{"row":20,"column":42},"end":{"row":20,"column":54},"action":"remove","lines":["projects_dto"],"id":44},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":["w"]},{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"insert","lines":["o"]},{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"insert","lines":["r"]}],[{"start":{"row":20,"column":34},"end":{"row":20,"column":45},"action":"remove","lines":["list_of_wor"],"id":45},{"start":{"row":20,"column":34},"end":{"row":20,"column":55},"action":"insert","lines":["list_of_workflows_dto"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"remove","lines":["t"],"id":46},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":["c"]},{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"remove","lines":["e"]},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"remove","lines":["j"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["o"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["r"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["P"]}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["W"],"id":47}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":54},"action":"remove","lines":["WStorageInterface"],"id":48},{"start":{"row":1,"column":37},"end":{"row":1,"column":61},"action":"insert","lines":["WorkflowStorageInterface"]}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["t"],"id":49},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["c"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["e"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"remove","lines":["j"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["o"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["r"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["P"]}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["W"],"id":50}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":43},"action":"remove","lines":["WStorageInterface"],"id":51},{"start":{"row":8,"column":26},"end":{"row":8,"column":50},"action":"insert","lines":["WorkflowStorageInterface"]}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["t"],"id":52},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["c"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["e"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["j"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["o"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["r"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["w"],"id":53},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["o"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["r"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["k"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["f"]}],[{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["l"],"id":54},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["o"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["w"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["t"],"id":55},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["c"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["e"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["j"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["o"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["r"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["P"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["W"],"id":56},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["o"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["r"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["k"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["f"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["l"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["o"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["w"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["s"],"id":57}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["s"],"id":58}],[{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["s"],"id":59}],[{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"remove","lines":["s"],"id":60}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["s"],"id":61}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":51},"end":{"row":20,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591088789902,"hash":"af73d8337ce933b979111cacaa66605e7cbebcb3"}