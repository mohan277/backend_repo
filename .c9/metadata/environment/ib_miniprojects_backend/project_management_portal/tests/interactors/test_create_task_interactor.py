{"filter":false,"title":"test_create_task_interactor.py","tooltip":"/ib_miniprojects_backend/project_management_portal/tests/interactors/test_create_task_interactor.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":141,"column":15},"end":{"row":141,"column":16},"action":"insert","lines":["="],"id":321},{"start":{"row":141,"column":16},"end":{"row":141,"column":17},"action":"insert","lines":["u"]},{"start":{"row":141,"column":17},"end":{"row":141,"column":18},"action":"insert","lines":["s"]},{"start":{"row":141,"column":18},"end":{"row":141,"column":19},"action":"insert","lines":["e"]},{"start":{"row":141,"column":19},"end":{"row":141,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":141,"column":16},"end":{"row":141,"column":20},"action":"remove","lines":["user"],"id":322},{"start":{"row":141,"column":16},"end":{"row":141,"column":23},"action":"insert","lines":["user_id"]}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":4},"action":"remove","lines":["    "],"id":323},{"start":{"row":141,"column":23},"end":{"row":142,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":4},"end":{"row":141,"column":8},"action":"remove","lines":["    "],"id":324},{"start":{"row":141,"column":0},"end":{"row":141,"column":4},"action":"remove","lines":["    "]},{"start":{"row":140,"column":45},"end":{"row":141,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":28},"end":{"row":141,"column":36},"action":"remove","lines":["state_id"],"id":325},{"start":{"row":141,"column":28},"end":{"row":141,"column":29},"action":"insert","lines":["a"]},{"start":{"row":141,"column":29},"end":{"row":141,"column":30},"action":"insert","lines":["d"]},{"start":{"row":141,"column":30},"end":{"row":141,"column":31},"action":"insert","lines":["m"]},{"start":{"row":141,"column":31},"end":{"row":141,"column":32},"action":"insert","lines":["i"]},{"start":{"row":141,"column":32},"end":{"row":141,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":141,"column":14},"end":{"row":141,"column":43},"action":"remove","lines":["raise_invalid_admin_exception"],"id":326},{"start":{"row":141,"column":14},"end":{"row":141,"column":43},"action":"insert","lines":["raise_invalid_admin_exception"]}],[{"start":{"row":101,"column":0},"end":{"row":142,"column":0},"action":"remove","lines":["def test_create_task_by_invalid_admin_id_raises_exception():","","    # Arrange","    title = \"title_1\"","    description = \"description\"","    project = 1","    state = 10","    user_id = 1","    issue_type = \"Bug\"","","    storage = create_autospec(TaskStorageInterface)","    presenter = create_autospec(PresenterInterface)","","    interactor = CreateTaskInteractor(","        storage=storage,","        presenter=presenter","    )","","","    storage.is_admin.return_value = False","    presenter.raise_invalid_admin_exception.side_effect = NotFound","","    interactor = CreateTaskInteractor(","        storage=storage,","        presenter=presenter","    )","","    # Act","    with pytest.raises(NotFound):","        interactor.create_task(","            title=title,","            user_id=user_id,","            description=description,","            project=project,","            state=state,","            issue_type=issue_type","        )","","    # Assert","    storage.is_admin.assert_called_once_with(user_id=user_id)","    presenter.raise_invalid_admin_exception.assert_called_once()",""],"id":327}],[{"start":{"row":100,"column":0},"end":{"row":101,"column":0},"action":"remove","lines":["",""],"id":328},{"start":{"row":99,"column":0},"end":{"row":100,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":99,"column":0},"end":{"row":142,"column":0},"action":"insert","lines":["def test_create_task_with_invalid_state_id_raises_exception():","","    # Arrange","    title = \"title_1\"","    description = \"description\"","    project = 1","    state = 10","    user_id = 1","    issue_type = \"Bug\"","","    storage = create_autospec(TaskStorageInterface)","    presenter = create_autospec(PresenterInterface)","","    interactor = CreateTaskInteractor(","        storage=storage,","        presenter=presenter","    )","","","    storage.is_valid_state_id.return_value = False","    presenter.raise_invalid_state_id_exception.side_effect = NotFound","","    interactor = CreateTaskInteractor(","        storage=storage,","        presenter=presenter","    )","","    # Act","    with pytest.raises(NotFound):","        interactor.create_task(","            title=title,","            user_id=user_id,","            description=description,","            project=project,","            state=state,","            issue_type=issue_type","        )","","    # Assert","    storage.is_valid_state_id.assert_called_once_with(","        state=state","    )","    presenter.raise_invalid_state_id_exception.assert_called_once()",""],"id":329}],[{"start":{"row":99,"column":0},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":330},{"start":{"row":100,"column":0},"end":{"row":101,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":101,"column":38},"end":{"row":101,"column":39},"action":"remove","lines":["e"],"id":331},{"start":{"row":101,"column":37},"end":{"row":101,"column":38},"action":"remove","lines":["t"]},{"start":{"row":101,"column":36},"end":{"row":101,"column":37},"action":"remove","lines":["a"]},{"start":{"row":101,"column":35},"end":{"row":101,"column":36},"action":"remove","lines":["t"]},{"start":{"row":101,"column":34},"end":{"row":101,"column":35},"action":"remove","lines":["s"]}],[{"start":{"row":101,"column":34},"end":{"row":101,"column":35},"action":"insert","lines":["u"],"id":332},{"start":{"row":101,"column":35},"end":{"row":101,"column":36},"action":"insert","lines":["s"]},{"start":{"row":101,"column":36},"end":{"row":101,"column":37},"action":"insert","lines":["e"]},{"start":{"row":101,"column":37},"end":{"row":101,"column":38},"action":"insert","lines":["r"]}],[{"start":{"row":120,"column":28},"end":{"row":120,"column":29},"action":"remove","lines":["d"],"id":333},{"start":{"row":120,"column":27},"end":{"row":120,"column":28},"action":"remove","lines":["i"]},{"start":{"row":120,"column":26},"end":{"row":120,"column":27},"action":"remove","lines":["_"]},{"start":{"row":120,"column":25},"end":{"row":120,"column":26},"action":"remove","lines":["e"]},{"start":{"row":120,"column":24},"end":{"row":120,"column":25},"action":"remove","lines":["t"]},{"start":{"row":120,"column":23},"end":{"row":120,"column":24},"action":"remove","lines":["a"]},{"start":{"row":120,"column":22},"end":{"row":120,"column":23},"action":"remove","lines":["t"]},{"start":{"row":120,"column":21},"end":{"row":120,"column":22},"action":"remove","lines":["s"]}],[{"start":{"row":120,"column":21},"end":{"row":120,"column":22},"action":"insert","lines":["u"],"id":334},{"start":{"row":120,"column":22},"end":{"row":120,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":120,"column":12},"end":{"row":120,"column":23},"action":"remove","lines":["is_valid_us"],"id":335},{"start":{"row":120,"column":12},"end":{"row":120,"column":34},"action":"insert","lines":["is_valid_user_ids_list"]}],[{"start":{"row":120,"column":33},"end":{"row":120,"column":34},"action":"remove","lines":["t"],"id":336},{"start":{"row":120,"column":32},"end":{"row":120,"column":33},"action":"remove","lines":["s"]},{"start":{"row":120,"column":31},"end":{"row":120,"column":32},"action":"remove","lines":["i"]},{"start":{"row":120,"column":30},"end":{"row":120,"column":31},"action":"remove","lines":["l"]},{"start":{"row":120,"column":29},"end":{"row":120,"column":30},"action":"remove","lines":["_"]},{"start":{"row":120,"column":28},"end":{"row":120,"column":29},"action":"remove","lines":["s"]}],[{"start":{"row":121,"column":32},"end":{"row":121,"column":33},"action":"remove","lines":["e"],"id":337},{"start":{"row":121,"column":31},"end":{"row":121,"column":32},"action":"remove","lines":["t"]},{"start":{"row":121,"column":30},"end":{"row":121,"column":31},"action":"remove","lines":["a"]},{"start":{"row":121,"column":29},"end":{"row":121,"column":30},"action":"remove","lines":["t"]},{"start":{"row":121,"column":28},"end":{"row":121,"column":29},"action":"remove","lines":["s"]}],[{"start":{"row":121,"column":28},"end":{"row":121,"column":29},"action":"insert","lines":["u"],"id":338},{"start":{"row":121,"column":29},"end":{"row":121,"column":30},"action":"insert","lines":["s"]},{"start":{"row":121,"column":30},"end":{"row":121,"column":31},"action":"insert","lines":["e"]},{"start":{"row":121,"column":31},"end":{"row":121,"column":32},"action":"insert","lines":["r"]}],[{"start":{"row":140,"column":28},"end":{"row":140,"column":29},"action":"remove","lines":["d"],"id":339},{"start":{"row":140,"column":27},"end":{"row":140,"column":28},"action":"remove","lines":["i"]},{"start":{"row":140,"column":26},"end":{"row":140,"column":27},"action":"remove","lines":["_"]},{"start":{"row":140,"column":25},"end":{"row":140,"column":26},"action":"remove","lines":["e"]},{"start":{"row":140,"column":24},"end":{"row":140,"column":25},"action":"remove","lines":["t"]},{"start":{"row":140,"column":23},"end":{"row":140,"column":24},"action":"remove","lines":["a"]},{"start":{"row":140,"column":22},"end":{"row":140,"column":23},"action":"remove","lines":["t"]},{"start":{"row":140,"column":21},"end":{"row":140,"column":22},"action":"remove","lines":["s"]}],[{"start":{"row":140,"column":21},"end":{"row":140,"column":22},"action":"insert","lines":["u"],"id":340},{"start":{"row":140,"column":22},"end":{"row":140,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":140,"column":12},"end":{"row":140,"column":23},"action":"remove","lines":["is_valid_us"],"id":341},{"start":{"row":140,"column":12},"end":{"row":140,"column":28},"action":"insert","lines":["is_valid_user_id"]}],[{"start":{"row":143,"column":32},"end":{"row":143,"column":33},"action":"remove","lines":["e"],"id":342},{"start":{"row":143,"column":31},"end":{"row":143,"column":32},"action":"remove","lines":["t"]},{"start":{"row":143,"column":30},"end":{"row":143,"column":31},"action":"remove","lines":["a"]},{"start":{"row":143,"column":29},"end":{"row":143,"column":30},"action":"remove","lines":["t"]},{"start":{"row":143,"column":28},"end":{"row":143,"column":29},"action":"remove","lines":["s"]}],[{"start":{"row":143,"column":28},"end":{"row":143,"column":29},"action":"insert","lines":["u"],"id":343},{"start":{"row":143,"column":29},"end":{"row":143,"column":30},"action":"insert","lines":["s"]},{"start":{"row":143,"column":30},"end":{"row":143,"column":31},"action":"insert","lines":["e"]},{"start":{"row":143,"column":31},"end":{"row":143,"column":32},"action":"insert","lines":["r"]}],[{"start":{"row":143,"column":14},"end":{"row":143,"column":45},"action":"remove","lines":["raise_invalid_user_id_exception"],"id":344},{"start":{"row":143,"column":14},"end":{"row":143,"column":45},"action":"insert","lines":["raise_invalid_user_id_exception"]}],[{"start":{"row":141,"column":8},"end":{"row":141,"column":19},"action":"remove","lines":["state=state"],"id":345},{"start":{"row":141,"column":8},"end":{"row":141,"column":9},"action":"insert","lines":["u"]},{"start":{"row":141,"column":9},"end":{"row":141,"column":10},"action":"insert","lines":["s"]},{"start":{"row":141,"column":10},"end":{"row":141,"column":11},"action":"insert","lines":["e"]},{"start":{"row":141,"column":11},"end":{"row":141,"column":12},"action":"insert","lines":["r"]}],[{"start":{"row":141,"column":8},"end":{"row":141,"column":12},"action":"remove","lines":["user"],"id":346},{"start":{"row":141,"column":8},"end":{"row":141,"column":15},"action":"insert","lines":["user_id"]}],[{"start":{"row":141,"column":15},"end":{"row":141,"column":16},"action":"insert","lines":["="],"id":347},{"start":{"row":141,"column":16},"end":{"row":141,"column":17},"action":"insert","lines":["u"]},{"start":{"row":141,"column":17},"end":{"row":141,"column":18},"action":"insert","lines":["s"]},{"start":{"row":141,"column":18},"end":{"row":141,"column":19},"action":"insert","lines":["e"]},{"start":{"row":141,"column":19},"end":{"row":141,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":141,"column":20},"end":{"row":141,"column":21},"action":"insert","lines":["_"],"id":348}],[{"start":{"row":141,"column":16},"end":{"row":141,"column":21},"action":"remove","lines":["user_"],"id":349},{"start":{"row":141,"column":16},"end":{"row":141,"column":23},"action":"insert","lines":["user_id"]}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":4},"action":"remove","lines":["    "],"id":350},{"start":{"row":141,"column":23},"end":{"row":142,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":4},"end":{"row":141,"column":8},"action":"remove","lines":["    "],"id":351},{"start":{"row":141,"column":0},"end":{"row":141,"column":4},"action":"remove","lines":["    "]},{"start":{"row":140,"column":53},"end":{"row":141,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":152,"column":14},"end":{"row":152,"column":15},"action":"remove","lines":["1"],"id":352}],[{"start":{"row":152,"column":14},"end":{"row":152,"column":15},"action":"insert","lines":["1"],"id":353},{"start":{"row":152,"column":15},"end":{"row":152,"column":16},"action":"insert","lines":["0"]}],[{"start":{"row":152,"column":15},"end":{"row":152,"column":16},"action":"remove","lines":["0"],"id":354}],[{"start":{"row":145,"column":4},"end":{"row":145,"column":49},"action":"remove","lines":["task_details_dto, create_task_expected_output"],"id":355},{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"remove","lines":["    "]},{"start":{"row":144,"column":61},"end":{"row":145,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":144,"column":61},"end":{"row":145,"column":0},"action":"insert","lines":["",""],"id":356},{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":145,"column":4},"end":{"row":145,"column":20},"action":"insert","lines":["task_details_dto"],"id":357}],[{"start":{"row":145,"column":20},"end":{"row":145,"column":21},"action":"insert","lines":[","],"id":358}],[{"start":{"row":145,"column":21},"end":{"row":145,"column":22},"action":"insert","lines":[" "],"id":359}],[{"start":{"row":145,"column":22},"end":{"row":145,"column":49},"action":"insert","lines":["create_task_expected_output"],"id":360}],[{"start":{"row":165,"column":23},"end":{"row":165,"column":50},"action":"remove","lines":["create_task_expected_output"],"id":361},{"start":{"row":165,"column":23},"end":{"row":165,"column":50},"action":"insert","lines":["create_task_expected_output"]}],[{"start":{"row":190,"column":23},"end":{"row":190,"column":50},"action":"remove","lines":["create_task_expected_output"],"id":362},{"start":{"row":190,"column":23},"end":{"row":190,"column":50},"action":"insert","lines":["create_task_expected_output"]}],[{"start":{"row":163,"column":39},"end":{"row":163,"column":55},"action":"remove","lines":["task_details_dto"],"id":363},{"start":{"row":163,"column":39},"end":{"row":163,"column":55},"action":"insert","lines":["task_details_dto"]}],[{"start":{"row":187,"column":25},"end":{"row":187,"column":41},"action":"remove","lines":["task_details_dto"],"id":364},{"start":{"row":187,"column":25},"end":{"row":187,"column":41},"action":"insert","lines":["task_details_dto"]}],[{"start":{"row":187,"column":8},"end":{"row":187,"column":24},"action":"remove","lines":["task_details_dto"],"id":365},{"start":{"row":187,"column":8},"end":{"row":187,"column":24},"action":"insert","lines":["task_details_dto"]}],[{"start":{"row":153,"column":22},"end":{"row":154,"column":0},"action":"insert","lines":["",""],"id":366},{"start":{"row":154,"column":0},"end":{"row":154,"column":4},"action":"insert","lines":["    "]},{"start":{"row":154,"column":4},"end":{"row":154,"column":5},"action":"insert","lines":["e"]},{"start":{"row":154,"column":5},"end":{"row":154,"column":6},"action":"insert","lines":["x"]},{"start":{"row":154,"column":6},"end":{"row":154,"column":7},"action":"insert","lines":["p"]},{"start":{"row":154,"column":7},"end":{"row":154,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":154,"column":8},"end":{"row":154,"column":9},"action":"insert","lines":["c"],"id":367},{"start":{"row":154,"column":9},"end":{"row":154,"column":10},"action":"insert","lines":["t"]},{"start":{"row":154,"column":10},"end":{"row":154,"column":11},"action":"insert","lines":["e"]},{"start":{"row":154,"column":11},"end":{"row":154,"column":12},"action":"insert","lines":["d"]}],[{"start":{"row":154,"column":12},"end":{"row":154,"column":13},"action":"insert","lines":[" "],"id":368},{"start":{"row":154,"column":13},"end":{"row":154,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":154,"column":14},"end":{"row":154,"column":15},"action":"insert","lines":[" "],"id":369},{"start":{"row":154,"column":15},"end":{"row":154,"column":16},"action":"insert","lines":["{"]}],[{"start":{"row":154,"column":16},"end":{"row":154,"column":18},"action":"insert","lines":["\"\""],"id":370}],[{"start":{"row":154,"column":17},"end":{"row":154,"column":18},"action":"insert","lines":["m"],"id":371},{"start":{"row":154,"column":18},"end":{"row":154,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":154,"column":18},"end":{"row":154,"column":19},"action":"remove","lines":["o"],"id":372},{"start":{"row":154,"column":17},"end":{"row":154,"column":18},"action":"remove","lines":["m"]},{"start":{"row":154,"column":16},"end":{"row":154,"column":18},"action":"remove","lines":["\"\""]},{"start":{"row":154,"column":15},"end":{"row":154,"column":16},"action":"remove","lines":["{"]},{"start":{"row":154,"column":14},"end":{"row":154,"column":15},"action":"remove","lines":[" "]}],[{"start":{"row":154,"column":12},"end":{"row":154,"column":13},"action":"insert","lines":["_"],"id":373},{"start":{"row":154,"column":13},"end":{"row":154,"column":14},"action":"insert","lines":["o"]},{"start":{"row":154,"column":14},"end":{"row":154,"column":15},"action":"insert","lines":["u"]},{"start":{"row":154,"column":15},"end":{"row":154,"column":16},"action":"insert","lines":["t"]},{"start":{"row":154,"column":16},"end":{"row":154,"column":17},"action":"insert","lines":["p"]},{"start":{"row":154,"column":17},"end":{"row":154,"column":18},"action":"insert","lines":["u"]},{"start":{"row":154,"column":18},"end":{"row":154,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":154,"column":21},"end":{"row":164,"column":5},"action":"insert","lines":["response = {","        \"title\": \"title_1\",","        \"task_id\": 1,","        \"description\": \"description_1\",","        \"project\": \"project_1\",","        \"state\": \"state_1\",","        \"issue_type\": IssueType.BUG.value,","        \"created_at\": datetime.datetime(2020, 5, 20, 0, 0),","        \"created_by\": \"user_1\",","        \"user_id\": 1","    }"],"id":374}],[{"start":{"row":154,"column":30},"end":{"row":154,"column":31},"action":"remove","lines":["="],"id":375},{"start":{"row":154,"column":29},"end":{"row":154,"column":30},"action":"remove","lines":[" "]},{"start":{"row":154,"column":28},"end":{"row":154,"column":29},"action":"remove","lines":["e"]},{"start":{"row":154,"column":27},"end":{"row":154,"column":28},"action":"remove","lines":["s"]},{"start":{"row":154,"column":26},"end":{"row":154,"column":27},"action":"remove","lines":["n"]},{"start":{"row":154,"column":25},"end":{"row":154,"column":26},"action":"remove","lines":["o"]},{"start":{"row":154,"column":24},"end":{"row":154,"column":25},"action":"remove","lines":["p"]},{"start":{"row":154,"column":23},"end":{"row":154,"column":24},"action":"remove","lines":["s"]},{"start":{"row":154,"column":22},"end":{"row":154,"column":23},"action":"remove","lines":["e"]},{"start":{"row":154,"column":21},"end":{"row":154,"column":22},"action":"remove","lines":["r"]}],[{"start":{"row":155,"column":4},"end":{"row":155,"column":8},"action":"remove","lines":["    "],"id":376},{"start":{"row":155,"column":0},"end":{"row":155,"column":4},"action":"remove","lines":["    "]},{"start":{"row":154,"column":23},"end":{"row":155,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":154,"column":23},"end":{"row":155,"column":0},"action":"insert","lines":["",""],"id":377},{"start":{"row":155,"column":0},"end":{"row":155,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":201,"column":34},"end":{"row":201,"column":35},"action":"remove","lines":["_"],"id":378},{"start":{"row":201,"column":33},"end":{"row":201,"column":34},"action":"remove","lines":["k"]},{"start":{"row":201,"column":32},"end":{"row":201,"column":33},"action":"remove","lines":["s"]},{"start":{"row":201,"column":31},"end":{"row":201,"column":32},"action":"remove","lines":["a"]},{"start":{"row":201,"column":30},"end":{"row":201,"column":31},"action":"remove","lines":["t"]},{"start":{"row":201,"column":29},"end":{"row":201,"column":30},"action":"remove","lines":["_"]},{"start":{"row":201,"column":28},"end":{"row":201,"column":29},"action":"remove","lines":["e"]},{"start":{"row":201,"column":27},"end":{"row":201,"column":28},"action":"remove","lines":["t"]},{"start":{"row":201,"column":26},"end":{"row":201,"column":27},"action":"remove","lines":["a"]},{"start":{"row":201,"column":25},"end":{"row":201,"column":26},"action":"remove","lines":["e"]},{"start":{"row":201,"column":24},"end":{"row":201,"column":25},"action":"remove","lines":["r"]},{"start":{"row":201,"column":23},"end":{"row":201,"column":24},"action":"remove","lines":["c"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":379}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":380},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["r"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":[" "],"id":381}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"],"id":382}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["d"],"id":383},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["a"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["e"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":12},"action":"remove","lines":["datet"],"id":384},{"start":{"row":0,"column":7},"end":{"row":0,"column":15},"action":"insert","lines":["datetime"]}],[{"start":{"row":161,"column":41},"end":{"row":161,"column":42},"action":"remove","lines":[","],"id":385},{"start":{"row":161,"column":40},"end":{"row":161,"column":41},"action":"remove","lines":["e"]},{"start":{"row":161,"column":39},"end":{"row":161,"column":40},"action":"remove","lines":["u"]},{"start":{"row":161,"column":38},"end":{"row":161,"column":39},"action":"remove","lines":["l"]},{"start":{"row":161,"column":37},"end":{"row":161,"column":38},"action":"remove","lines":["a"]},{"start":{"row":161,"column":36},"end":{"row":161,"column":37},"action":"remove","lines":["v"]},{"start":{"row":161,"column":35},"end":{"row":161,"column":36},"action":"remove","lines":["."]},{"start":{"row":161,"column":34},"end":{"row":161,"column":35},"action":"remove","lines":["G"]},{"start":{"row":161,"column":33},"end":{"row":161,"column":34},"action":"remove","lines":["U"]},{"start":{"row":161,"column":32},"end":{"row":161,"column":33},"action":"remove","lines":["B"]},{"start":{"row":161,"column":31},"end":{"row":161,"column":32},"action":"remove","lines":["."]},{"start":{"row":161,"column":30},"end":{"row":161,"column":31},"action":"remove","lines":["e"]},{"start":{"row":161,"column":29},"end":{"row":161,"column":30},"action":"remove","lines":["p"]},{"start":{"row":161,"column":28},"end":{"row":161,"column":29},"action":"remove","lines":["y"]},{"start":{"row":161,"column":27},"end":{"row":161,"column":28},"action":"remove","lines":["T"]},{"start":{"row":161,"column":26},"end":{"row":161,"column":27},"action":"remove","lines":["e"]}],[{"start":{"row":161,"column":25},"end":{"row":161,"column":26},"action":"remove","lines":["u"],"id":386},{"start":{"row":161,"column":24},"end":{"row":161,"column":25},"action":"remove","lines":["s"]},{"start":{"row":161,"column":23},"end":{"row":161,"column":24},"action":"remove","lines":["s"]},{"start":{"row":161,"column":22},"end":{"row":161,"column":23},"action":"remove","lines":["I"]}],[{"start":{"row":161,"column":22},"end":{"row":161,"column":24},"action":"insert","lines":["\"\""],"id":387}],[{"start":{"row":161,"column":23},"end":{"row":161,"column":24},"action":"insert","lines":["B"],"id":388},{"start":{"row":161,"column":24},"end":{"row":161,"column":25},"action":"insert","lines":["u"]},{"start":{"row":161,"column":25},"end":{"row":161,"column":26},"action":"insert","lines":["g"]}],[{"start":{"row":161,"column":27},"end":{"row":161,"column":28},"action":"insert","lines":[","],"id":389}],[{"start":{"row":164,"column":8},"end":{"row":164,"column":20},"action":"remove","lines":["\"user_id\": 1"],"id":390},{"start":{"row":164,"column":4},"end":{"row":164,"column":8},"action":"remove","lines":["    "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":4},"action":"remove","lines":["    "]},{"start":{"row":163,"column":31},"end":{"row":164,"column":0},"action":"remove","lines":["",""]},{"start":{"row":163,"column":30},"end":{"row":163,"column":31},"action":"remove","lines":[","]}],[{"start":{"row":201,"column":23},"end":{"row":201,"column":24},"action":"insert","lines":["#"],"id":391}],[{"start":{"row":201,"column":23},"end":{"row":201,"column":25},"action":"insert","lines":["[]"],"id":392}],[{"start":{"row":201,"column":23},"end":{"row":201,"column":25},"action":"remove","lines":["[]"],"id":393}],[{"start":{"row":201,"column":23},"end":{"row":201,"column":24},"action":"remove","lines":["#"],"id":394}],[{"start":{"row":176,"column":23},"end":{"row":176,"column":24},"action":"insert","lines":["#"],"id":395}],[{"start":{"row":176,"column":23},"end":{"row":176,"column":25},"action":"insert","lines":["[]"],"id":396}],[{"start":{"row":176,"column":25},"end":{"row":176,"column":26},"action":"remove","lines":["#"],"id":397},{"start":{"row":176,"column":24},"end":{"row":176,"column":25},"action":"remove","lines":["]"]},{"start":{"row":176,"column":23},"end":{"row":176,"column":24},"action":"remove","lines":["["]}],[{"start":{"row":176,"column":34},"end":{"row":176,"column":35},"action":"remove","lines":["_"],"id":398},{"start":{"row":176,"column":33},"end":{"row":176,"column":34},"action":"remove","lines":["k"]},{"start":{"row":176,"column":32},"end":{"row":176,"column":33},"action":"remove","lines":["s"]},{"start":{"row":176,"column":31},"end":{"row":176,"column":32},"action":"remove","lines":["a"]},{"start":{"row":176,"column":30},"end":{"row":176,"column":31},"action":"remove","lines":["t"]},{"start":{"row":176,"column":29},"end":{"row":176,"column":30},"action":"remove","lines":["_"]},{"start":{"row":176,"column":28},"end":{"row":176,"column":29},"action":"remove","lines":["e"]},{"start":{"row":176,"column":27},"end":{"row":176,"column":28},"action":"remove","lines":["t"]},{"start":{"row":176,"column":26},"end":{"row":176,"column":27},"action":"remove","lines":["a"]},{"start":{"row":176,"column":25},"end":{"row":176,"column":26},"action":"remove","lines":["e"]},{"start":{"row":176,"column":24},"end":{"row":176,"column":25},"action":"remove","lines":["r"]},{"start":{"row":176,"column":23},"end":{"row":176,"column":24},"action":"remove","lines":["c"]},{"start":{"row":176,"column":22},"end":{"row":176,"column":23},"action":"remove","lines":[" "]}],[{"start":{"row":176,"column":22},"end":{"row":176,"column":23},"action":"insert","lines":[" "],"id":399}],[{"start":{"row":190,"column":20},"end":{"row":191,"column":0},"action":"insert","lines":["",""],"id":400},{"start":{"row":191,"column":0},"end":{"row":191,"column":8},"action":"insert","lines":["        "]},{"start":{"row":191,"column":8},"end":{"row":191,"column":9},"action":"insert","lines":["u"]},{"start":{"row":191,"column":9},"end":{"row":191,"column":10},"action":"insert","lines":["s"]},{"start":{"row":191,"column":10},"end":{"row":191,"column":11},"action":"insert","lines":["e"]},{"start":{"row":191,"column":11},"end":{"row":191,"column":12},"action":"insert","lines":["r"]},{"start":{"row":191,"column":12},"end":{"row":191,"column":13},"action":"insert","lines":["+"]},{"start":{"row":191,"column":13},"end":{"row":191,"column":14},"action":"insert","lines":["_"]}],[{"start":{"row":191,"column":13},"end":{"row":191,"column":14},"action":"remove","lines":["_"],"id":401},{"start":{"row":191,"column":12},"end":{"row":191,"column":13},"action":"remove","lines":["+"]}],[{"start":{"row":191,"column":12},"end":{"row":191,"column":13},"action":"insert","lines":["_"],"id":402},{"start":{"row":191,"column":13},"end":{"row":191,"column":14},"action":"insert","lines":["i"]},{"start":{"row":191,"column":14},"end":{"row":191,"column":15},"action":"insert","lines":["d"]},{"start":{"row":191,"column":15},"end":{"row":191,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":191,"column":16},"end":{"row":191,"column":17},"action":"insert","lines":["u"],"id":403},{"start":{"row":191,"column":17},"end":{"row":191,"column":18},"action":"insert","lines":["s"]},{"start":{"row":191,"column":18},"end":{"row":191,"column":19},"action":"insert","lines":["e"]},{"start":{"row":191,"column":19},"end":{"row":191,"column":20},"action":"insert","lines":["r"]},{"start":{"row":191,"column":20},"end":{"row":191,"column":21},"action":"insert","lines":["+"]}],[{"start":{"row":191,"column":20},"end":{"row":191,"column":21},"action":"remove","lines":["+"],"id":404}],[{"start":{"row":191,"column":20},"end":{"row":191,"column":21},"action":"insert","lines":["_"],"id":405},{"start":{"row":191,"column":21},"end":{"row":191,"column":22},"action":"insert","lines":["i"]},{"start":{"row":191,"column":22},"end":{"row":191,"column":23},"action":"insert","lines":["d"]},{"start":{"row":191,"column":23},"end":{"row":191,"column":24},"action":"insert","lines":[","]}],[{"start":{"row":155,"column":4},"end":{"row":164,"column":5},"action":"remove","lines":["expected_output = {","        \"title\": \"title_1\",","        \"task_id\": 1,","        \"description\": \"description_1\",","        \"project\": \"project_1\",","        \"state\": \"state_1\",","        \"issue_type\": \"Bug\",","        \"created_at\": datetime.datetime(2020, 5, 20, 0, 0),","        \"created_by\": \"user_1\"","    }"],"id":406},{"start":{"row":155,"column":0},"end":{"row":155,"column":4},"action":"remove","lines":["    "]},{"start":{"row":154,"column":22},"end":{"row":155,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":192,"column":23},"end":{"row":192,"column":24},"action":"insert","lines":["c"],"id":407},{"start":{"row":192,"column":24},"end":{"row":192,"column":25},"action":"insert","lines":["r"]},{"start":{"row":192,"column":25},"end":{"row":192,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":192,"column":23},"end":{"row":192,"column":26},"action":"remove","lines":["cre"],"id":408},{"start":{"row":192,"column":23},"end":{"row":192,"column":55},"action":"insert","lines":["create_project_expected_output()"]}],[{"start":{"row":192,"column":53},"end":{"row":192,"column":55},"action":"remove","lines":["()"],"id":409}],[{"start":{"row":192,"column":53},"end":{"row":192,"column":68},"action":"remove","lines":["expected_output"],"id":410}],[{"start":{"row":166,"column":23},"end":{"row":166,"column":24},"action":"insert","lines":["c"],"id":411},{"start":{"row":166,"column":24},"end":{"row":166,"column":25},"action":"insert","lines":["r"]},{"start":{"row":166,"column":25},"end":{"row":166,"column":26},"action":"insert","lines":["e"]},{"start":{"row":166,"column":26},"end":{"row":166,"column":27},"action":"insert","lines":["a"]}],[{"start":{"row":166,"column":23},"end":{"row":166,"column":27},"action":"remove","lines":["crea"],"id":412},{"start":{"row":166,"column":23},"end":{"row":166,"column":55},"action":"insert","lines":["create_project_expected_output()"]}],[{"start":{"row":166,"column":53},"end":{"row":166,"column":55},"action":"remove","lines":["()"],"id":413}],[{"start":{"row":166,"column":53},"end":{"row":166,"column":68},"action":"remove","lines":["expected_output"],"id":414}],[{"start":{"row":192,"column":36},"end":{"row":192,"column":37},"action":"remove","lines":["t"],"id":415},{"start":{"row":192,"column":35},"end":{"row":192,"column":36},"action":"remove","lines":["c"]},{"start":{"row":192,"column":34},"end":{"row":192,"column":35},"action":"remove","lines":["e"]},{"start":{"row":192,"column":33},"end":{"row":192,"column":34},"action":"remove","lines":["j"]},{"start":{"row":192,"column":32},"end":{"row":192,"column":33},"action":"remove","lines":["o"]},{"start":{"row":192,"column":31},"end":{"row":192,"column":32},"action":"remove","lines":["r"]},{"start":{"row":192,"column":30},"end":{"row":192,"column":31},"action":"remove","lines":["p"]}],[{"start":{"row":192,"column":30},"end":{"row":192,"column":31},"action":"insert","lines":["t"],"id":416},{"start":{"row":192,"column":31},"end":{"row":192,"column":32},"action":"insert","lines":["a"]},{"start":{"row":192,"column":32},"end":{"row":192,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":192,"column":23},"end":{"row":192,"column":33},"action":"remove","lines":["create_tas"],"id":417},{"start":{"row":192,"column":23},"end":{"row":192,"column":52},"action":"insert","lines":["create_task_expected_output()"]}],[{"start":{"row":192,"column":50},"end":{"row":192,"column":52},"action":"remove","lines":["()"],"id":418}],[{"start":{"row":192,"column":50},"end":{"row":192,"column":66},"action":"remove","lines":["_expected_output"],"id":419}],[{"start":{"row":166,"column":36},"end":{"row":166,"column":37},"action":"remove","lines":["t"],"id":420},{"start":{"row":166,"column":35},"end":{"row":166,"column":36},"action":"remove","lines":["c"]},{"start":{"row":166,"column":34},"end":{"row":166,"column":35},"action":"remove","lines":["e"]},{"start":{"row":166,"column":33},"end":{"row":166,"column":34},"action":"remove","lines":["j"]},{"start":{"row":166,"column":32},"end":{"row":166,"column":33},"action":"remove","lines":["o"]},{"start":{"row":166,"column":31},"end":{"row":166,"column":32},"action":"remove","lines":["r"]},{"start":{"row":166,"column":30},"end":{"row":166,"column":31},"action":"remove","lines":["p"]}],[{"start":{"row":166,"column":30},"end":{"row":166,"column":31},"action":"insert","lines":["t"],"id":421},{"start":{"row":166,"column":31},"end":{"row":166,"column":32},"action":"insert","lines":["a"]},{"start":{"row":166,"column":32},"end":{"row":166,"column":33},"action":"insert","lines":["s"]},{"start":{"row":166,"column":33},"end":{"row":166,"column":34},"action":"insert","lines":["k"]}]]},"ace":{"folds":[],"scrolltop":-50,"scrollleft":0,"selection":{"start":{"row":9,"column":29},"end":{"row":9,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591164741828,"hash":"b25f90deca5fbcc2ffa24d71b06d54e0f4f528e4"}