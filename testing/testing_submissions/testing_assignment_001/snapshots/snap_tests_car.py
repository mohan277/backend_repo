# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_car_object_creation_with_all_parameters_returns_car_object_snapshot max_speed'] = 50

snapshots['test_car_object_creation_with_all_parameters_returns_car_object_snapshot acceleration'] = 10

snapshots['test_car_object_creation_with_all_parameters_returns_car_object_snapshot tyre_friction'] = 3

snapshots['test_car_object_creation_with_all_parameters_returns_car_object_snapshot current_speed'] = 0

snapshots['test_car_object_creation_with_all_parameters_returns_car_object_snapshot is_engine_started'] = False

snapshots['test_car_object_creation_with_all_parameters_returns_car_object_snapshot is_car_instance'] = True

snapshots['test_car_object_creation_with_invalid_max_speed_returns_value_error_snapshot[-250-10-3] invalid_max_speed'] = GenericRepr("<ExceptionInfo ValueError('Invalid value for max_speed') tblen=3>")

snapshots['test_car_object_creation_with_invalid_max_speed_returns_value_error_snapshot[0-10-3] invalid_max_speed'] = GenericRepr("<ExceptionInfo ValueError('Invalid value for max_speed') tblen=3>")

snapshots['test_car_object_creation_with_invalid_acceleration_returns_value_error_snapshot[250--10-3] invalid_acceleration'] = GenericRepr("<ExceptionInfo ValueError('Invalid value for acceleration') tblen=3>")

snapshots['test_car_object_creation_with_invalid_acceleration_returns_value_error_snapshot[250-0-3] invalid_acceleration'] = GenericRepr("<ExceptionInfo ValueError('Invalid value for acceleration') tblen=3>")

snapshots['test_car_object_creation_with_invalid_tyre_friction_returns_value_error_snapshot[250-10--3] invalid_tyre_friction'] = GenericRepr("<ExceptionInfo ValueError('Invalid value for tyre_friction') tblen=3>")

snapshots['test_car_object_creation_with_invalid_tyre_friction_returns_value_error_snapshot[250-10-0] invalid_tyre_friction'] = GenericRepr("<ExceptionInfo ValueError('Invalid value for tyre_friction') tblen=3>")

snapshots['test_accelerate_car_should_increase_by_the_value_of_acceleration_snapshot current_speed'] = 10

snapshots['test_accelerate_car_more_than_max_speed_snapshot accelerate more than maxspeed'] = 50

snapshots['test_accelerate_when_car_engine_is_not_started_snapshot Start the engine to accelerate'] = '''Start the engine to accelerate
'''

snapshots['test_accelerate_when_car_engine_is_not_started_snapshot is engine started'] = False

snapshots['test_accelerate_when_car_engine_is_started_snapshot when car engine is started'] = 10

snapshots['test_apply_break_when_car_current_speed_is_more_than_tyre_friction_snapshot applying brakes'] = 7

snapshots['test_apply_break_when_car_current_speed_is_less_than_tyre_friction_snapshot applying brakes when current_speed is lessthan tyre_friction'] = 0

snapshots['test_apply_break_when_car_current_speed_is_equal_to_tyre_friction_snapshot applying brakes when current_speed is equal to tyre_friction'] = 0

snapshots['test_sound_horn_when_car_engine_is_started_returns_beep_beep_snapshot sound_horn'] = '''Start the engine to sound_horn
'''

snapshots['test_sound_horn_when_car_engine_is_started_returns_beep_beep_snapshot is_engine_started'] = False

snapshots['test_sound_horn_when_car_engine_not_started_returns_alert_snapshot sound_horn when car is not started'] = '''Start the engine to sound_horn
'''

snapshots['test_sound_horn_when_car_engine_not_started_returns_alert_snapshot is_engine_started'] = False

snapshots['test_stop_engine_when_engine_is_started_returns_engine_state_snapshot is_engine_started'] = False

snapshots['test_stop_engine_when_engine_is_not_started_returns_engine_state_snapshot is_engine_started'] = False

snapshots['test_encapsulation_of_protected_attribute_color_return_error_snapshot encapsulation of color'] = GenericRepr('<ExceptionInfo AttributeError("can\'t set attribute") tblen=1>')

snapshots['test_encapsulation_of_protected_attribute_max_speed_return_error_snapshot encapsulation of max_speed'] = GenericRepr('<ExceptionInfo AttributeError("can\'t set attribute") tblen=1>')

snapshots['test_encapsulation_of_protected_attribute_acceleration_return_error_snapshot encapsulation of acceleration'] = GenericRepr('<ExceptionInfo AttributeError("can\'t set attribute") tblen=1>')

snapshots['test_encapsulation_of_protected_attribute_tyre_friction_return_error_snapshot encapsulation of tyre_friction'] = GenericRepr('<ExceptionInfo AttributeError("can\'t set attribute") tblen=1>')

snapshots['test_encapsulation_of_protected_attribute_is_engine_started_return_error_snapshot encapsulation of is_engine_started'] = GenericRepr('<ExceptionInfo AttributeError("can\'t set attribute") tblen=1>')

snapshots['test_encapsulation_of_protected_attribute_current_speed_return_error_snapshot encapsulation of current_speed'] = GenericRepr('<ExceptionInfo AttributeError("can\'t set attribute") tblen=1>')
