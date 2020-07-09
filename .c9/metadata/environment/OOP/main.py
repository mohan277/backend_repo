{"filter":false,"title":"main.py","tooltip":"/OOP/main.py","ace":{"folds":[],"scrolltop":694.5,"scrollleft":0,"selection":{"start":{"row":53,"column":4},"end":{"row":53,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":69,"mode":"ace/mode/python"}},"hash":"004ba972b567a1cf2bc767d8122f48b29a6e1082","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":49,"column":11},"end":{"row":49,"column":12},"action":"insert","lines":["a"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":49,"column":12},"action":"remove","lines":["class C(object):","    def __init__(self):","        self._x = 0","","    @property","    def x(self):","        print('getting')","        return self._x","","    @x.setter","    def set_x(self, value):","        print('setting')","        self._x = value","","if __name__ == '__main__':","    c = C()","    print(c.x)","    c.x = 10","    print(c.x)","","","","","","","","","","","","","# class Pet:","#     _class_info = \"pet animals\"","","#     def about(self):","#         print(\"This class is about \" + self._class_info + \"!\")   ","    ","","# class Dog(Pet):","#     _class_info = \"man's best friends\"","","# class Cat(Pet):","#     _class_info = \"all kinds of cats\"","","# p = Pet()","# p.about()","# d = Dog()","# d.about()","# c = Cat()","# c.about()a"],"id":3},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["c"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["l"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["a"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["s"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["D"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["e"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["e"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[":"],"id":5}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["d"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["e"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["f"],"id":7},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["e"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":1,"column":4},"end":{"row":40,"column":35},"action":"insert","lines":["deers_count = 0","    sound = 'Buck Buck'","    breathing = 'Breathe in air'","    ","    def __init__(self,age_in_months, breed, required_food_in_kgs):","        self._age_in_months =age_in_months","        self._breed= breed","        self._required_food_in_kgs = required_food_in_kgs","        type(self).deers_count += 1","        ","        if self._age_in_months != 1:","            raise ValueError(f'Invalid value for field age_in_months: {self.age_in_months}')","            ","        if self._required_food_in_kgs <= 0:","            raise ValueError(f'Invalid value for field required_food_in_kgs: {self._required_food_in_kgs}')","            ","            ","    @property","    def age_in_months(self):","        return self._age_in_months","        ","    @property","    def breed(self):","        return self._breed","    ","    @property","    def required_food_in_kgs(self):","        return self._required_food_in_kgs","    ","    ","    def grow(self):","        self._age_in_months += 1","        self._required_food_in_kgs += 2","    ","    ","    def make_sound(self):","        print(type(self).sound)","    ","    def breathe(self):","        print(type(self).breathing)"],"id":8}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["="],"id":10},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["N"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["o"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["e"],"id":11}],[{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":["="],"id":12},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"insert","lines":["N"]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"insert","lines":["o"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"insert","lines":["n"]},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":74},"end":{"row":6,"column":75},"action":"insert","lines":["="],"id":13},{"start":{"row":6,"column":75},"end":{"row":6,"column":76},"action":"insert","lines":["N"]},{"start":{"row":6,"column":76},"end":{"row":6,"column":77},"action":"insert","lines":["o"]},{"start":{"row":6,"column":77},"end":{"row":6,"column":78},"action":"insert","lines":["n"]},{"start":{"row":6,"column":78},"end":{"row":6,"column":79},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":76},"end":{"row":13,"column":77},"action":"insert","lines":["_"],"id":14}],[{"start":{"row":41,"column":35},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]},{"start":{"row":42,"column":8},"end":{"row":43,"column":0},"action":"insert","lines":["",""]},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":8},"action":"remove","lines":["    "],"id":16},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":43,"column":0},"end":{"row":64,"column":0},"action":"insert","lines":["class Lion(Deer):","    ","    sound = 'Roar Roar'","    breathing = 'Breathe in air'","    ","    def __init__(self,age_in_months, breed, required_food_in_kgs):","        super().__init__(age_in_months, breed, required_food_in_kgs)","        ","        ","    def grow(self):","        self._age_in_months += 1","        self._required_food_in_kgs += 4","    ","    def hunt(self,park_name):","        self.park_name = park_name","        if type(self).deers_count > 0:","            type(self).deers_count -= 1","            print(type(self).deers_count)","            # type(self).animals_count -= 1","        else:","            print('No deers to hunt')",""],"id":17}],[{"start":{"row":61,"column":12},"end":{"row":61,"column":43},"action":"remove","lines":["# type(self).animals_count -= 1"],"id":18},{"start":{"row":61,"column":8},"end":{"row":61,"column":12},"action":"remove","lines":["    "]},{"start":{"row":61,"column":4},"end":{"row":61,"column":8},"action":"remove","lines":["    "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"remove","lines":["    "]},{"start":{"row":60,"column":41},"end":{"row":61,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":48,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["def __init__(self,age_in_months, breed, required_food_in_kgs):","        super().__init__(age_in_months, breed, required_food_in_kgs)","        ","        "],"id":19},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"remove","lines":["    "]},{"start":{"row":47,"column":4},"end":{"row":48,"column":0},"action":"remove","lines":["",""]}]]},"timestamp":1582258164985}