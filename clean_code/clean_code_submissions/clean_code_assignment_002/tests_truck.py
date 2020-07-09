from truck import Truck

import pytest


@pytest.fixture
def truck():
    truck = Truck(color="Red", max_speed=250, acceleration=10,
                  tyre_friction=3, max_cargo_weight=100)
    return truck


def test_truck_object_creation_when_parameters_passed_returns_truck_object():

    # Arrange
    expected_max_speed = 250
    expected_acceleration = 10
    expected_tyre_friction = 3
    expected_max_cargo_weight = 100
    expected_is_engine_started = False
    # Act
    truck = Truck(color="Red", max_speed=250, acceleration=10,
                  tyre_friction=3, max_cargo_weight=100)

    # Assert
    assert truck.max_speed == expected_max_speed
    assert truck.acceleration == expected_acceleration
    assert truck.tyre_friction == expected_tyre_friction
    assert truck.max_cargo_weight == expected_max_cargo_weight
    assert truck.is_engine_started is expected_is_engine_started
    assert isinstance(truck, Truck)


def test_sound_horn_when_truck_engine_started_returns_honk_honk(truck, capsys):

    # Arrange
    truck.start_engine()
    expected_output = 'Honk Honk\n'
    expected_is_engine_started = True
    output = capsys.readouterr()

    # Act
    truck.sound_horn()

    # Assert
    assert output.out == expected_output
    assert truck.is_engine_started is expected_is_engine_started


def test_sound_horn_when_truck_engine_not_started_returns_alert(truck, capsys):

    # Arrange
    expected_output = 'Start the engine to sound_horn\n'
    expected_is_engine_started = False
    output = capsys.readouterr()

    # Act
    truck.sound_horn()

    # Assert
    assert output.out == expected_output
    assert truck.is_engine_started is expected_is_engine_started


@pytest.mark.parametrize(
        "max_speed, acceleration, tyre_friction, max_cargo_weight",
        [(250, 10, 3, -50), (250, 10, 3, 0)])
def test_load_when_invalid_data_of_load_is_given_returns_value_error(
        max_speed, acceleration, tyre_friction, max_cargo_weight):

    with pytest.raises(ValueError) as Error:

        # Arrange
        truck = Truck(color="Red", max_speed=max_speed,
                      acceleration=acceleration, tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight)
        expected_output = "Invalid value for cargo_weight"

        # Act
        truck.load(max_cargo_weight)

        # Assert
        assert str(Error.value) == expected_output


def test_load_when_truck_engine_on_and_at_rest_returns_loaded_weight(truck):

    # Arrange
    truck.start_engine()
    expected_current_speed = 0
    expected_is_engine_started = True

    # Act
    truck.load(50)

    # Assert
    assert truck.current_speed == expected_current_speed
    assert truck.is_engine_started is expected_is_engine_started


def test_load_when_truck_engine_off_returns_loaded_weight(truck):

    # Arrange
    expected_current_speed = 0
    expected_is_engine_started = False

    # Act
    truck.load(50)

    # Assert
    assert truck.current_speed == expected_current_speed
    assert truck.is_engine_started is expected_is_engine_started


def test_load_when_truck_is_in_motion_returns_alert(truck, capsys):

    # Arrange
    truck.start_engine()
    truck.accelerate()
    expected_output = 'Cannot load cargo during motion\n'
    expected_is_engine_started = True
    output = capsys.readouterr()

    # Act
    truck.load(50)

    # Assert
    assert output.out == expected_output
    assert truck.is_engine_started is expected_is_engine_started


def test_load_when_load_more_than_max_cargo_weight_return_alert(truck, capsys):

    # Arrange
    expected_output = 'Cannot load cargo more than max limit: 100\n'
    output = capsys.readouterr()

    # Act
    truck.load(110)

    # Assert
    assert output.out == expected_output


def test_load_when_truck_engine_on_and_at_rest_load_more_than_max_cargo_weight_returns_alert(truck, capsys):

    # Arrange
    truck.start_engine()
    expected_output = 'Cannot load cargo more than max limit: 100\n'
    expected_current_speed = 0
    expected_is_engine_started = True
    output = capsys.readouterr()

    # Act
    truck.load(110)

    # Assert
    assert output.out == expected_output
    assert truck.current_speed == expected_current_speed
    assert truck.is_engine_started == expected_is_engine_started


def test_unload_when_truck_engine_on_and_at_rest_return_unloaded_weight(truck):

    # Arrange
    truck.start_engine()
    expected_current_speed = 0
    expected_is_engine_started = True

    # Act
    truck.unload(50)

    # Assert
    assert truck.current_speed == expected_current_speed
    assert truck.is_engine_started is expected_is_engine_started


def test_unload_when_truck_engine_off_returns_unloaded_weight(truck):

    # Arrange
    expected_current_speed = 0
    expected_is_engine_started = False

    # Act
    truck.unload(50)

    # Assert
    assert truck.current_speed == expected_current_speed
    assert truck.is_engine_started is expected_is_engine_started


def test_unload_when_truck_is_in_motion_returns_alert(truck, capsys):

    # Arrange
    truck.start_engine()
    truck.accelerate()
    expected_output = 'Cannot unload cargo during motion\n'
    expected_is_engine_started = True
    output = capsys.readouterr()

    # Act
    truck.unload(50)

    # Assert
    assert output.out == expected_output
    assert truck.is_engine_started is expected_is_engine_started


def test_encapsulation_of_protected_attribute_max_cargo_weight_returns_error(truck):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        truck.max_cargo_weight = 100

        # Assert
        assert str(Error.value) == expected_output
