from race_car import RaceCar

import pytest

@pytest.fixture
def race_car():
    race_car = RaceCar(color="Red",
                  max_speed=50, 
                  acceleration=10, 
                  tyre_friction=3)
    return race_car
    
def test_truck_object_creation_when_parameters_passed_returns_truck_object():
    
    # Arrange
    expected_max_speed = 250
    expected_acceleration = 10
    expected_tyre_friction = 3
    expected_max_cargo_weight = 100
    expected_is_engine_started = False
    # Act
    race_car = RaceCar(color="Red",
                  max_speed=250,
                  acceleration=10,
                  tyre_friction=3)
    
    # Assert
    assert race_car.max_speed == expected_max_speed 
    assert race_car.acceleration == expected_acceleration
    assert race_car.tyre_friction == expected_tyre_friction
    assert race_car.is_engine_started is expected_is_engine_started
    assert isinstance(race_car,RaceCar)


def test_sound_horn_when_engine_started_returns_sound(race_car, capsys):
    
    # Arrange
    race_car.start_engine()
    expected_output = 'Peep Peep\nBeep Beep\n'
    expected_is_engine_started = True
    
    # Act
    race_car.sound_horn()
    output = capsys.readouterr()
    
    # Assert
    assert output.out == expected_output
    assert race_car.is_engine_started is expected_is_engine_started

def test_sound_horn_when_engine_not_started_returns_alert(race_car, capsys):
    
    # Arrange
    expected_output = 'Start the engine to sound_horn\n'
    expected_is_engine_started = False
    # Act
    race_car.sound_horn()
    output = capsys.readouterr()
    
    # Assert
    assert output.out == expected_output
    assert race_car.is_engine_started is expected_is_engine_started


def test_accelerate_when_nitro_is_available_returns_extra_increased_current_speed(race_car):
    
    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    expected_is_engine_started = True
    expected_current_speed = 40
    expected_nitro = 0
    
    # Act
    race_car.accelerate()
    
    # Assert
    assert race_car.current_speed == expected_current_speed
    assert race_car.is_engine_started is expected_is_engine_started
    assert race_car.nitro == expected_nitro

def test_accelerate_when_current_speed_more_than_max_speed(race_car):
    
    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    expected_is_engine_started = True
    expected_current_speed = 50
    
    # Act
    race_car.accelerate()
    
    # Assert
    assert race_car.current_speed == expected_current_speed
    assert race_car.is_engine_started is expected_is_engine_started

# def test_apply_break_when_current_speed_is_equal_to_tyre_friction()
def test_encapsulation_of_protected_attribute_nitro_returns_error(race_car):
    
    with pytest.raises(AttributeError) as Error:
        
        # Arrange
        expected_output = "can't set attribute"
        
        # Act
        race_car.nitro = 10
        
        # Assert
        assert str(Error.value) == expected_output