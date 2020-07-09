from car import Car


class RaceCar(Car):
    HORN_SOUND = 'Peep Peep\nBeep Beep'

    def __init__(
        self, color=None, max_speed=None,
            acceleration=None, tyre_friction=None):

        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._nitro = 0

    @property
    def nitro(self):
        return self._nitro

    def apply_brakes(self):
        if self._current_speed >= self._tyre_friction:
            if self._current_speed > self._max_speed/2:
                self._nitro += 10
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0

    def accelerate(self):
        import math
        if self._is_engine_started:
            if self._nitro > 0:
                self._nitro -= 10
                if self._current_speed + self._acceleration + (
                    math.ceil(
                        self._acceleration * 30/100)) <= self._max_speed:

                    self._current_speed += self._acceleration + (
                        math.ceil(self._acceleration * 30/100))
                else:
                    self._current_speed = self._max_speed
            else:
                super().accelerate()
        else:
            print('Start the engine to accelerate')
