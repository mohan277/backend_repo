{"filter":false,"title":"storage_interface.py","tooltip":"/ib_miniprojects_backend/formaster/interactors/storages/storage_interface.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":40,"column":23},"end":{"row":40,"column":40},"action":"remove","lines":["=self.question_id"],"id":213},{"start":{"row":40,"column":23},"end":{"row":40,"column":24},"action":"insert","lines":[":"]}],[{"start":{"row":40,"column":24},"end":{"row":40,"column":25},"action":"insert","lines":[" "],"id":214},{"start":{"row":40,"column":25},"end":{"row":40,"column":26},"action":"insert","lines":["i"]},{"start":{"row":40,"column":26},"end":{"row":40,"column":27},"action":"insert","lines":["n"]},{"start":{"row":40,"column":27},"end":{"row":40,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":37},"end":{"row":40,"column":50},"action":"remove","lines":["=self.form_id"],"id":215},{"start":{"row":40,"column":37},"end":{"row":40,"column":38},"action":"insert","lines":[":"]}],[{"start":{"row":40,"column":38},"end":{"row":40,"column":39},"action":"insert","lines":[" "],"id":216},{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"insert","lines":["i"]},{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":40,"column":41},"end":{"row":40,"column":42},"action":"insert","lines":["t"],"id":217}],[{"start":{"row":40,"column":43},"end":{"row":40,"column":44},"action":"insert","lines":[":"],"id":218}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":12},"action":"remove","lines":["    "],"id":219},{"start":{"row":40,"column":4},"end":{"row":40,"column":8},"action":"remove","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]},{"start":{"row":39,"column":39},"end":{"row":40,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":39,"column":39},"end":{"row":39,"column":40},"action":"insert","lines":["s"],"id":220},{"start":{"row":39,"column":40},"end":{"row":39,"column":41},"action":"insert","lines":["e"]},{"start":{"row":39,"column":41},"end":{"row":39,"column":42},"action":"insert","lines":["l"]},{"start":{"row":39,"column":42},"end":{"row":39,"column":43},"action":"insert","lines":["f"]}],[{"start":{"row":39,"column":43},"end":{"row":39,"column":44},"action":"insert","lines":[" "],"id":221}],[{"start":{"row":39,"column":43},"end":{"row":39,"column":44},"action":"remove","lines":[" "],"id":222}],[{"start":{"row":39,"column":43},"end":{"row":39,"column":44},"action":"insert","lines":[","],"id":223}],[{"start":{"row":39,"column":44},"end":{"row":39,"column":45},"action":"insert","lines":[" "],"id":224}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["p"],"id":225},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["a"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["s"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "],"id":226}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "],"id":227}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":21},"action":"remove","lines":["            )"],"id":228},{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["@"],"id":229},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["a"]},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":38,"column":5},"end":{"row":38,"column":7},"action":"remove","lines":["ab"],"id":230},{"start":{"row":38,"column":5},"end":{"row":38,"column":21},"action":"insert","lines":["abstractmethod()"]}],[{"start":{"row":38,"column":19},"end":{"row":38,"column":21},"action":"remove","lines":["()"],"id":231}],[{"start":{"row":35,"column":12},"end":{"row":37,"column":13},"action":"remove","lines":["return presenter.submit_form_response_details(","                user_response_id=user_response_id","            )"],"id":232}],[{"start":{"row":31,"column":0},"end":{"row":35,"column":12},"action":"remove","lines":["","    def submit_form_response_wrapper(self, presenter: PresenterInterface):","        try:","            user_response_id = self.submit_form_response()","            "],"id":233}],[{"start":{"row":8,"column":12},"end":{"row":31,"column":0},"action":"remove","lines":["","from abc import abstractmethod","from formaster.interactors.mixins.form_validation import FormValidationMixin","from formaster.interactors.storages.storage_interface import StorageInterface","from formaster.interactors.presenters.presenter_interface import \\","    PresenterInterface","from formaster.exceptions.exceptions import (","    FormClosedException,","    FormDoesNotExistException,","    QuestionDoesNotBelongToForm,","    InvalidUserResponseSubmitException",")","","","class BaseSubmitFormResponseInteractor(FormValidationMixin):","","    def __init__(self, storage: StorageInterface,","                 user_id: int, form_id: int, question_id: int):","","        self.user_id = user_id","        self.form_id = form_id","        self.question_id = question_id","        self.storage = storage",""],"id":234}],[{"start":{"row":8,"column":12},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":235},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]},{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":236}],[{"start":{"row":12,"column":12},"end":{"row":15,"column":12},"action":"insert","lines":["","    @abstractmethod","    def validate_question_id_with_form(self, question_id: int, form_id: int):","        pass"],"id":237}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":238},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":38},"action":"remove","lines":["validate_question_id_with_form"],"id":239},{"start":{"row":15,"column":8},"end":{"row":15,"column":56},"action":"insert","lines":["self.storage.validate_form(form_id=self.form_id)"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":21},"action":"remove","lines":["self.storage."],"id":240}],[{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["="],"id":241},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["d"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["i"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["_"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["m"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["r"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["o"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["f"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["."],"id":242}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":[","],"id":243}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":[" "],"id":244}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":[":"],"id":245},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["i"]},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"remove","lines":["n"],"id":246},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"remove","lines":["i"]}],[{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":[" "],"id":247},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["i"]},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":["n"]},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":41},"action":"remove","lines":["(self, form_id: int)"],"id":248}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":249}],[{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"remove","lines":[" "],"id":250},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"remove","lines":[","]},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"remove","lines":["t"]},{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"remove","lines":["n"]},{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"remove","lines":["i"]},{"start":{"row":15,"column":40},"end":{"row":15,"column":41},"action":"remove","lines":[" "]},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"remove","lines":[":"]},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"remove","lines":["d"]},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"remove","lines":["i"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"remove","lines":["_"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"remove","lines":["n"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"remove","lines":["o"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"remove","lines":["i"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["t"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["s"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["e"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["u"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["q"],"id":251}],[{"start":{"row":16,"column":12},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":252},{"start":{"row":17,"column":0},"end":{"row":17,"column":8},"action":"insert","lines":["        "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":253}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":254},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "],"id":255}],[{"start":{"row":19,"column":4},"end":{"row":46,"column":0},"action":"insert","lines":["from formaster.interactors.storages.storage_interface import StorageInterface","from formaster.interactors.base import BaseSubmitFormResponseInteractor","from formaster.exceptions.exceptions import InvalidUserResponseSubmitException","","","class MCQQuestionSubmitFormResponseInteractor(","    BaseSubmitFormResponseInteractor):","","    def __init__(self, storage: StorageInterface, question_id: int,","                 form_id: int, user_id: int, user_submitted_option_id: int):","        super().__init__(storage, question_id, form_id, user_id)","        self.user_submitted_option_id = user_submitted_option_id","","    def _validate_user_response(self):","        option_ids = self.storage.get_option_ids_for_question(","            question_id=self.question_id","        )","        is_valid_option_id = self.user_submitted_option_id not in option_ids","","        if is_valid_option_id:","            raise InvalidUserResponseSubmitException","","    def _create_user_response(self):","        response_id = self.storage.create_user_mcq_response(","            self.user_id, self.question_id, self.user_submitted_option_id","        )","        return response_id",""],"id":256}],[{"start":{"row":18,"column":0},"end":{"row":33,"column":0},"action":"remove","lines":["","    from formaster.interactors.storages.storage_interface import StorageInterface","from formaster.interactors.base import BaseSubmitFormResponseInteractor","from formaster.exceptions.exceptions import InvalidUserResponseSubmitException","","","class MCQQuestionSubmitFormResponseInteractor(","    BaseSubmitFormResponseInteractor):","","    def __init__(self, storage: StorageInterface, question_id: int,","                 form_id: int, user_id: int, user_submitted_option_id: int):","        super().__init__(storage, question_id, form_id, user_id)","        self.user_submitted_option_id = user_submitted_option_id","","    def _validate_user_response(self):",""],"id":257}],[{"start":{"row":21,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["        is_valid_option_id = self.user_submitted_option_id not in option_ids","","        if is_valid_option_id:","            raise InvalidUserResponseSubmitException","","    def _create_user_response(self):",""],"id":258}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["        return response_id",""],"id":259}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":34},"action":"remove","lines":["        option_ids = self.storage."],"id":260}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "],"id":261}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["d"],"id":262},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["e"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":[" "],"id":263}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":264}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "],"id":265}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["@"],"id":266},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["a"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":18,"column":5},"end":{"row":18,"column":7},"action":"remove","lines":["ab"],"id":267},{"start":{"row":18,"column":5},"end":{"row":18,"column":21},"action":"insert","lines":["abstractmethod()"]}],[{"start":{"row":18,"column":19},"end":{"row":18,"column":21},"action":"remove","lines":["()"],"id":268}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "],"id":269},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":40},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["."],"id":270}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":[","],"id":271}],[{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":[" "],"id":272}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":24},"action":"remove","lines":["            question_id="],"id":273},{"start":{"row":19,"column":36},"end":{"row":20,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":[":"],"id":274}],[{"start":{"row":19,"column":55},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":275},{"start":{"row":20,"column":0},"end":{"row":20,"column":8},"action":"insert","lines":["        "]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["p"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["a"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["s"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":12},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":276},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["@"],"id":277},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["a"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["b"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":5},"end":{"row":22,"column":8},"action":"remove","lines":["abs"],"id":278},{"start":{"row":22,"column":5},"end":{"row":22,"column":21},"action":"insert","lines":["abstractmethod()"]}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":21},"action":"remove","lines":["()"],"id":279}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":35},"action":"remove","lines":["response_id = self.storage."],"id":280},{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["d"],"id":281},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["e"]},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":[" "],"id":282}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":8},"action":"remove","lines":["    "],"id":283},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]},{"start":{"row":24,"column":73},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":12},"action":"remove","lines":["    "],"id":284},{"start":{"row":24,"column":4},"end":{"row":24,"column":8},"action":"remove","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":33},"end":{"row":24,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":23,"column":37},"end":{"row":23,"column":38},"action":"remove","lines":["."],"id":285}],[{"start":{"row":23,"column":37},"end":{"row":23,"column":38},"action":"insert","lines":[","],"id":286}],[{"start":{"row":23,"column":38},"end":{"row":23,"column":39},"action":"insert","lines":[" "],"id":287}],[{"start":{"row":23,"column":47},"end":{"row":23,"column":53},"action":"remove","lines":[" self."],"id":288}],[{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":[":"],"id":289}],[{"start":{"row":23,"column":47},"end":{"row":23,"column":48},"action":"insert","lines":[" "],"id":290},{"start":{"row":23,"column":48},"end":{"row":23,"column":49},"action":"insert","lines":["i"]},{"start":{"row":23,"column":49},"end":{"row":23,"column":50},"action":"insert","lines":["n"]},{"start":{"row":23,"column":50},"end":{"row":23,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":52},"end":{"row":23,"column":53},"action":"insert","lines":[" "],"id":291}],[{"start":{"row":23,"column":64},"end":{"row":23,"column":65},"action":"insert","lines":[":"],"id":292}],[{"start":{"row":23,"column":65},"end":{"row":23,"column":66},"action":"insert","lines":[" "],"id":293},{"start":{"row":23,"column":66},"end":{"row":23,"column":67},"action":"insert","lines":["i"]},{"start":{"row":23,"column":67},"end":{"row":23,"column":68},"action":"insert","lines":["n"]},{"start":{"row":23,"column":68},"end":{"row":23,"column":69},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":69},"end":{"row":23,"column":70},"action":"insert","lines":[" "],"id":294}],[{"start":{"row":23,"column":69},"end":{"row":23,"column":70},"action":"remove","lines":[" "],"id":295}],[{"start":{"row":23,"column":75},"end":{"row":23,"column":76},"action":"remove","lines":["."],"id":296},{"start":{"row":23,"column":74},"end":{"row":23,"column":75},"action":"remove","lines":["f"]},{"start":{"row":23,"column":73},"end":{"row":23,"column":74},"action":"remove","lines":["l"]},{"start":{"row":23,"column":72},"end":{"row":23,"column":73},"action":"remove","lines":["e"]},{"start":{"row":23,"column":71},"end":{"row":23,"column":72},"action":"remove","lines":["s"]}],[{"start":{"row":23,"column":95},"end":{"row":23,"column":96},"action":"insert","lines":[":"],"id":297}],[{"start":{"row":23,"column":96},"end":{"row":23,"column":97},"action":"insert","lines":[" "],"id":298},{"start":{"row":23,"column":97},"end":{"row":23,"column":98},"action":"insert","lines":["i"]},{"start":{"row":23,"column":98},"end":{"row":23,"column":99},"action":"insert","lines":["n"]},{"start":{"row":23,"column":99},"end":{"row":23,"column":100},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":70},"end":{"row":23,"column":71},"action":"remove","lines":[" "],"id":299},{"start":{"row":23,"column":70},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":8},"action":"insert","lines":["    "],"id":300}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":12},"action":"insert","lines":["    "],"id":301}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":16},"action":"insert","lines":["    "],"id":302}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":20},"action":"insert","lines":["    "],"id":303}],[{"start":{"row":24,"column":20},"end":{"row":24,"column":24},"action":"insert","lines":["    "],"id":304}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":28},"action":"insert","lines":["    "],"id":305}],[{"start":{"row":24,"column":28},"end":{"row":24,"column":32},"action":"insert","lines":["    "],"id":306}],[{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":[" "],"id":307}],[{"start":{"row":24,"column":63},"end":{"row":24,"column":64},"action":"insert","lines":[":"],"id":308}],[{"start":{"row":24,"column":64},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":309},{"start":{"row":25,"column":0},"end":{"row":25,"column":37},"action":"insert","lines":["                                     "]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":310},{"start":{"row":25,"column":0},"end":{"row":25,"column":37},"action":"remove","lines":["                                     "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "],"id":311}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":8},"action":"insert","lines":["    "],"id":312}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["p"],"id":313},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["a"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["s"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":0},"end":{"row":23,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":55,"mode":"ace/mode/python"}},"timestamp":1592548149105,"hash":"9e68505de0d6e0dfb90be9e0ea5345a89649776f"}