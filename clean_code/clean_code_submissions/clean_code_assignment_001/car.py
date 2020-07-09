class Car:

    HORN_SOUND = 'Beep Beep'

    def __init__(
        self, color=None, max_speed=None,
            acceleration=None, tyre_friction=None):

        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._current_speed = 0
        self.raiseError(self._max_speed, 'max_speed')
        self.raiseError(self._acceleration, 'acceleration')
        self.raiseError(self._tyre_friction, 'tyre_friction')

    @property
    def color(self):
        return self._color

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def acceleration(self):
        return self._acceleration

    @property
    def tyre_friction(self):
        return self._tyre_friction

    @property
    def is_engine_started(self):
        return self._is_engine_started

    @property
    def current_speed(self):
        return self._current_speed

    @staticmethod
    def raiseError(value, name):
        if value <= 0:
            raise ValueError(f'Invalid value for {name}')

    def start_engine(self):
        if not self._is_engine_started:
            self._is_engine_started = True

    def sound_horn(self):
        if self._is_engine_started:
            print(type(self).HORN_SOUND)
        else:
            print('Start the engine to sound_horn')

    def accelerate(self):
        if self._is_engine_started:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                self._current_speed = self._max_speed
        else:
            print('Start the engine to accelerate')

    def apply_brakes(self):
        if self._current_speed >= self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0

    def stop_engine(self):
        if self._is_engine_started:
            self._is_engine_started = False
