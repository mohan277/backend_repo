{"filter":false,"title":"test_user_admin_login.py","tooltip":"/ib_miniprojects_backend/project_management_portal/tests/interactors/test_user_admin_login.py","undoManager":{"mark":38,"position":38,"stack":[[{"start":{"row":0,"column":0},"end":{"row":44,"column":0},"action":"insert","lines":["from unittest .mock import create_autospec","from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor","from fb_post_v2.interactors.storages.storage_interface import \\","    StorageInterface","from fb_post_v2.interactors.presenters.presenter_interface import \\","    PresenterInterface","","def test_create_post():","","    # Arrange","    user_id = 1","    post_content = \"New_Post\"","    new_post_id = 1","    mock_presenter_response = {\"post_id\": new_post_id}","","    storage = create_autospec(StorageInterface)","    presenter = create_autospec(PresenterInterface)","","    interactor = CreatePostInteractor(","        storage=storage,","        presenter=presenter","    )","","    storage.create_post.return_value = new_post_id","    presenter.get_create_post_response.return_value = mock_presenter_response","","    # Act","    response = interactor.create_post(","        user_id=user_id,","        post_content=post_content","    )","","    # Assert","","    storage.create_post.assert_called_once_with(","        user_id=user_id,","        post_content=post_content","    )","","    presenter.get_create_post_response.assert_called_once_with(","        post_id=new_post_id","    )","","    assert response == mock_presenter_response",""],"id":1}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":20},"action":"remove","lines":["create_post"],"id":2},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["u"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["s"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["e"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["r"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["_"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["a"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["m"],"id":3},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["i"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["n"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["_"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["l"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["o"]}],[{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["g"],"id":4},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["i"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["n"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["w"],"id":5},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["i"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["t"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["h"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["_"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["v"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["a"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["k"]}],[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"remove","lines":["k"],"id":6}],[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["l"],"id":7},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["i"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["d"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["_"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["e"],"id":8},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["t"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["a"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["i"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["l"]},{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":15},"action":"remove","lines":["fb_post_v2"],"id":9},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["p"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":7},"action":"remove","lines":["pr"],"id":10},{"start":{"row":1,"column":5},"end":{"row":1,"column":30},"action":"insert","lines":["project_management_portal"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":15},"action":"remove","lines":["fb_post_v2"],"id":11},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["p"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["r"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["o"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["j"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["e"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["c"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":12},"action":"remove","lines":["project"],"id":12},{"start":{"row":2,"column":5},"end":{"row":2,"column":30},"action":"insert","lines":["project_management_portal"]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":15},"action":"remove","lines":["fb_post_v2"],"id":13},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["p"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["r"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":8},"action":"remove","lines":["pro"],"id":14},{"start":{"row":4,"column":5},"end":{"row":4,"column":30},"action":"insert","lines":["project_management_portal"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":65},"action":"remove","lines":["create_post_interactor"],"id":15},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["u"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["s"]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["e"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":47},"action":"remove","lines":["user"],"id":16},{"start":{"row":1,"column":43},"end":{"row":1,"column":77},"action":"insert","lines":["user_admin_login_storage_interface"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["s"],"id":17},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":45},"action":"remove","lines":["st"],"id":18},{"start":{"row":1,"column":43},"end":{"row":1,"column":51},"action":"insert","lines":["storages"]}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":["."],"id":19}],[{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":[" "],"id":20},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["\\"]}],[{"start":{"row":1,"column":54},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "],"id":22}],[{"start":{"row":2,"column":46},"end":{"row":2,"column":66},"action":"remove","lines":["CreatePostInteractor"],"id":23}],[{"start":{"row":2,"column":46},"end":{"row":2,"column":47},"action":"insert","lines":["L"],"id":24}],[{"start":{"row":2,"column":46},"end":{"row":2,"column":47},"action":"remove","lines":["L"],"id":25},{"start":{"row":2,"column":46},"end":{"row":2,"column":67},"action":"insert","lines":["LoginStorageInterface"]}],[{"start":{"row":3,"column":43},"end":{"row":3,"column":69},"action":"remove","lines":["storages.storage_interface"],"id":26},{"start":{"row":3,"column":43},"end":{"row":3,"column":70},"action":"insert","lines":["user_admin_login_interactor"]}],[{"start":{"row":3,"column":71},"end":{"row":3,"column":72},"action":"insert","lines":["\\"],"id":27}],[{"start":{"row":3,"column":72},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":28}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "],"id":29}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "],"id":30},{"start":{"row":4,"column":12},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["\\"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["L"],"id":31},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":29},"action":"remove","lines":["LoStorageInterface"],"id":32},{"start":{"row":4,"column":11},"end":{"row":4,"column":32},"action":"insert","lines":["LoginStorageInterface"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":32},"action":"remove","lines":["LoginStorageInterface"],"id":33}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["L"],"id":34},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":13},"action":"remove","lines":["Lo"],"id":35},{"start":{"row":4,"column":11},"end":{"row":4,"column":26},"action":"insert","lines":["LoginInteractor"]}],[{"start":{"row":5,"column":74},"end":{"row":5,"column":75},"action":"insert","lines":["\\"],"id":36}],[{"start":{"row":5,"column":75},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "],"id":38}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":39},{"start":{"row":6,"column":12},"end":{"row":7,"column":0},"action":"remove","lines":["",""]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["\\"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":11},"end":{"row":13,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590553546821,"hash":"a66ae9c998b4ab000b2cc5606dd479a70d08486a"}