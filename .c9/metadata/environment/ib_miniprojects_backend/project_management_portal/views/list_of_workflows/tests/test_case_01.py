{"filter":false,"title":"test_case_01.py","tooltip":"/ib_miniprojects_backend/project_management_portal/views/list_of_workflows/tests/test_case_01.py","undoManager":{"mark":26,"position":26,"stack":[[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":2}],[{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":37,"column":0},"action":"insert","lines":["def setupUser(self, username, password):","        super(TestCase01ListOfProjectsAPITestCase, self).setupUser(","            username=username, password=password","        )","        user = self.foo_user","        user.is_admin = True","        user.save()","        ProjectFactory.create_batch(10, created_by=user)",""],"id":4}],[{"start":{"row":33,"column":0},"end":{"row":37,"column":0},"action":"remove","lines":["        user = self.foo_user","        user.is_admin = True","        user.save()","        ProjectFactory.create_batch(10, created_by=user)",""],"id":5}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "],"id":6}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"insert","lines":["    "],"id":7}],[{"start":{"row":33,"column":8},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":34,"column":0},"end":{"row":34,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":8},"action":"remove","lines":["    "],"id":9},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]},{"start":{"row":33,"column":8},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["W"],"id":10},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["o"]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":10},"action":"remove","lines":["Wo"],"id":11},{"start":{"row":33,"column":8},"end":{"row":33,"column":16},"action":"insert","lines":["Workflow"]}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":["F"],"id":12},{"start":{"row":33,"column":17},"end":{"row":33,"column":18},"action":"insert","lines":["a"]},{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"insert","lines":["c"]},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"insert","lines":["o"],"id":13},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"insert","lines":["r"]},{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"insert","lines":["y"]}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":25},"action":"insert","lines":["()"],"id":14}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"insert","lines":["."],"id":15},{"start":{"row":33,"column":24},"end":{"row":33,"column":25},"action":"insert","lines":["c"]},{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"insert","lines":["r"]},{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"insert","lines":["e"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":["a"]},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"insert","lines":["t"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":30},"end":{"row":33,"column":31},"action":"insert","lines":["_"],"id":16}],[{"start":{"row":33,"column":24},"end":{"row":33,"column":31},"action":"remove","lines":["create_"],"id":17},{"start":{"row":33,"column":24},"end":{"row":33,"column":36},"action":"insert","lines":["create_batch"]}],[{"start":{"row":33,"column":37},"end":{"row":33,"column":38},"action":"insert","lines":["1"],"id":18},{"start":{"row":33,"column":38},"end":{"row":33,"column":39},"action":"insert","lines":["0"]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":4,"column":0},"end":{"row":8,"column":66},"action":"insert","lines":["","from project_management_portal.models import Project","from project_management_portal.models.factories import ProjectFactory","from project_management_portal.utils.custom_tests_utils import CustomTestUtils","from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX"],"id":20}],[{"start":{"row":7,"column":78},"end":{"row":9,"column":61},"action":"remove","lines":["","from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX","from django_swagger_utils.utils.test import CustomAPITestCase"],"id":21}],[{"start":{"row":6,"column":55},"end":{"row":6,"column":69},"action":"remove","lines":["ProjectFactory"],"id":22},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"insert","lines":["W"]}],[{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"remove","lines":["W"],"id":23},{"start":{"row":6,"column":55},"end":{"row":6,"column":70},"action":"insert","lines":["WorkflowFactory"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":52},"action":"remove","lines":["from project_management_portal.models import Project"],"id":24},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "],"id":25},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":23,"column":43},"end":{"row":23,"column":60},"action":"remove","lines":["CustomAPITestCase"],"id":26},{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["C"]}],[{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"remove","lines":["C"],"id":27},{"start":{"row":23,"column":43},"end":{"row":23,"column":58},"action":"insert","lines":["CustomTestUtils"]}],[{"start":{"row":31,"column":14},"end":{"row":31,"column":49},"action":"remove","lines":["TestCase01ListOfProjectsAPITestCase"],"id":28},{"start":{"row":31,"column":14},"end":{"row":31,"column":50},"action":"insert","lines":["TestCase01ListOfWorkflowsAPITestCase"]}]]},"ace":{"folds":[],"scrolltop":144,"scrollleft":0,"selection":{"start":{"row":39,"column":41},"end":{"row":39,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1593185548712,"hash":"023df85b248732ecad516e782e5785a471d40b6e"}