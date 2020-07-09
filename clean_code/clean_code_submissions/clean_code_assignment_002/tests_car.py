from car import Car
import pytest


@pytest.fixture
def car():
    car_obj = Car(color="Red", max_speed=50, acceleration=10, tyre_friction=3)
    return car_obj


def test_car_object_creation_with_all_parameters_returns_car_object():

    # Arrange
    expected_max_speed = 50
    expected_acceleration = 10
    expected_tyre_friction = 3
    expected_current_speed = 0
    expected_is_engine_started = False

    # Act
    car_obj = Car(color="Red", max_speed=50, acceleration=10, tyre_friction=3)

    # Assert
    assert car_obj.max_speed == expected_max_speed
    assert car_obj.acceleration == expected_acceleration
    assert car_obj.tyre_friction == expected_tyre_friction
    assert car_obj.current_speed == expected_current_speed
    assert car_obj.is_engine_started is expected_is_engine_started
    assert isinstance(car_obj, Car)


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [(-250, 10, 3), (0, 10, 3)])
def test_car_object_creation_with_invalid_max_speed_returns_value_error(
        max_speed, acceleration, tyre_friction):

    with pytest.raises(ValueError) as Error:

        # Arrange
        expected_output = "Invalid value for max_speed"

        # Assert
        Car(color="Red", max_speed=max_speed, acceleration=acceleration,
            tyre_friction=tyre_friction)

        assert str(Error.value) == expected_output


@pytest.mark.parametrize(
    "max_speed,acceleration, tyre_friction", [(250, -10, 3), (250, 0, 3)])
def test_car_object_creation_with_invalid_acceleration_returns_value_error(
        max_speed, acceleration, tyre_friction):

    with pytest.raises(ValueError) as Error:

        # Arrange
        expected_output = "Invalid value for acceleration"

        # Act
        Car(color="Red", max_speed=max_speed, acceleration=acceleration,
            tyre_friction=tyre_friction)

        # Assert
        assert str(Error.value) == expected_output


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [(250, 10, -3), (250, 10, 0)])
def test_car_object_creation_with_invalid_tyre_friction_returns_value_error(
        max_speed, acceleration, tyre_friction):

    with pytest.raises(ValueError) as Error:

        # Arrange
        expected_output = "Invalid value for tyre_friction"

        # Act
        Car(color="Red", max_speed=max_speed, acceleration=acceleration,
            tyre_friction=tyre_friction)

        # Assert
        assert str(Error.value) == expected_output


def test_accelerate_car_should_increase_by_the_value_of_acceleration(car):

    # Arrange
    car.start_engine()
    expected_current_speed = 10

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == expected_current_speed


def test_accelerate_car_more_than_max_speed(car):

    # Arrange
    expected_current_speed = 50
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == expected_current_speed


def test_accelerate_when_car_engine_is_not_started(car, capsys):

    # Arrange
    expected_output = 'Start the engine to accelerate\n'
    output = capsys.readouterr()

    # Act
    car.accelerate()

    # Assert
    assert output.out == expected_output
    assert car.is_engine_started is False


def test_accelerate_when_car_engine_is_started(car):

    # Arrange
    car.start_engine()
    expected_current_speed = 10

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == expected_current_speed


def test_apply_break_when_car_current_speed_is_more_than_tyre_friction(car):

    # Arrange
    expected_current_speed = 7
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == expected_current_speed


def test_apply_break_when_car_current_speed_is_less_than_tyre_friction(car):

    # Arrange
    expected_current_speed = 0
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == expected_current_speed


def test_apply_break_when_car_current_speed_is_equal_to_tyre_friction():

    # Arrange
    car_obj = Car(color="Red", max_speed=50, acceleration=3, tyre_friction=3)
    expected_current_speed = 0
    car_obj.start_engine()
    car_obj.accelerate()

    # Act
    car_obj.apply_brakes()

    # Assert
    assert car_obj.current_speed == expected_current_speed


def test_sound_horn_when_car_engine_is_started_returns_beep_beep(car, capsys):

    # Arrange
    car.start_engine()
    expected_output = 'Beep Beep\n'
    expected_is_engine_started = True
    output = capsys.readouterr()

    # Act
    car.sound_horn()

    # Assert
    assert output.out == expected_output
    assert car.is_engine_started is expected_is_engine_started


def test_sound_horn_when_car_engine_not_started_returns_alert(car, capsys):

    # Arrange
    expected_output = 'Start the engine to sound_horn\n'
    expected_is_engine_started = False
    output = capsys.readouterr()

    # Act
    car.sound_horn()

    # Assert
    assert output.out == expected_output
    assert car.is_engine_started is expected_is_engine_started


def test_stop_engine_when_engine_is_started_returns_engine_state(car):

    # Arrange
    car.start_engine()
    expected_output = False

    # Act
    car.stop_engine()

    # Assert
    assert car.is_engine_started == expected_output


def test_stop_engine_when_engine_is_not_started_returns_engine_state(car):

    # Arrange
    expected_output = False

    # Act
    car.stop_engine()

    # Assert
    assert car.is_engine_started == expected_output


def test_encapsulation_of_protected_attribute_color_return_error(car):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        car.color = "Blue"

        # Assert
        assert str(Error.value) == expected_output


def test_encapsulation_of_protected_attribute_max_speed_return_error(car):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        car.max_speed = 100

        # Assert
        assert str(Error.value) == expected_output


def test_encapsulation_of_protected_attribute_acceleration_return_error(car):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        car.acceleration = 10

        # Assert
        assert str(Error.value) == expected_output


def test_encapsulation_of_protected_attribute_tyre_friction_return_error(car):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        car.tyre_friction = 3

        # Assert
        assert str(Error.value) == expected_output


def test_encapsulation_protected_attribute_is_engine_started_return_error(car):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        car.is_engine_started = False

        # Assert
        assert str(Error.value) == expected_output


def test_encapsulation_of_protected_attribute_current_speed_return_error(car):

    with pytest.raises(AttributeError) as Error:

        # Arrange
        expected_output = "can't set attribute"

        # Act
        car.current_speed = 10

        # Assert
        assert str(Error.value) == expected_output
