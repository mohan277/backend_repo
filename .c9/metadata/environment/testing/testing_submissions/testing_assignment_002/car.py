{"filter":false,"title":"car.py","tooltip":"/testing/testing_submissions/testing_assignment_002/car.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":75,"column":0},"end":{"row":155,"column":51},"action":"remove","lines":["        ","    ","class Truck(Car):","    ","    HORN_SOUND = 'Honk Honk'","    def __init__(self,color=None, max_speed=None, acceleration=None, tyre_friction=None, max_cargo_weight=None):","        super().__init__(color, max_speed, acceleration,tyre_friction)","        self._max_cargo_weight = max_cargo_weight","        self._my_cargo = 0","    ","    @property","    def max_cargo_weight(self):","        return self._max_cargo_weight","        ","    @property","    def may_cargo(self):","        return self._my_cargo","        ","    @property","    def cargo_weight(self):","        return self._cargo_weight","    ","    def load(self, cargo_weight):","        if self._current_speed <= 0:","            self._cargo_weight = cargo_weight","            if self._cargo_weight <= 0:","                raise ValueError(f'Invalid value for cargo_weight')","            else:","                if self._my_cargo + self._cargo_weight <= self._max_cargo_weight:","                    self._my_cargo += self._cargo_weight","                else:","                    print(f'Cannot load cargo more than max limit: {self._max_cargo_weight}')","        else:","            print('Cannot load cargo during motion')","            ","            ","    def unload(self, cargo_weight):","        if self._current_speed <= 0:","            self._cargo_weight = cargo_weight","            if self._cargo_weight <= 0:","                raise ValueError(f'Invalid value for cargo_weight')","            else:","                if self._my_cargo - self._cargo_weight >= 0:","                    self._my_cargo -= self._cargo_weight","        else:","            print('Cannot unload cargo during motion')","        ","    ","class RaceCar(Car):","    HORN_SOUND = 'Peep Peep\\nBeep Beep'","    ","    def __init__(self,color=None, max_speed=None, acceleration=None, tyre_friction=None):","        super().__init__(color, max_speed, acceleration,tyre_friction)","        self._nitro = 0","        ","    @property","    def nitro(self):","        return self._nitro","    ","    def apply_brakes(self):","        if self._current_speed >= self._tyre_friction:","            if self._current_speed > self._max_speed/2:","                self._nitro += 10","            self._current_speed -= self._tyre_friction","        else:","            self._current_speed = 0","            ","            ","    def accelerate(self):","        import math","        if self._is_engine_started:","            if self._nitro > 0:","                self._nitro -= 10","                if self._current_speed + self._acceleration + (math.ceil(self._acceleration * 30/100)) <= self._max_speed:","                    self._current_speed += self._acceleration + (math.ceil(self._acceleration * 30/100))","                else:","                    self._current_speed = self._max_speed","            else:","                super().accelerate()","        else:","            print('Start the engine to accelerate')"],"id":2},{"start":{"row":74,"column":43},"end":{"row":75,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":1040.5,"scrollleft":0,"selection":{"start":{"row":74,"column":43},"end":{"row":74,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":56,"state":"start","mode":"ace/mode/python"}},"timestamp":1587631935304,"hash":"decf4f8664934359e959a67f60fafcc5ed6a916d"}