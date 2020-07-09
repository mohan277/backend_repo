# from is_weekend import is_weekend_using_calendar
# from my_calendar import MyCalendar


# def test_is_weekend_using_calendar_on_weekend():
#     calendar_obj = MyCalendar()

#     result = is_weekend_using_calendar(calendar_obj)

#     assert result is True


# def test_is_weekend_using_calendar_on_weekday():
#     calendar_obj = MyCalendar()

#     result = is_weekend_using_calendar(calendar_obj)

#     assert result is False

# from unittest.mock import Mock

# def test_weekend():
#     mock_calendar_obj = Mock()
#     mock_calendar_obj.get_current_day.return_value = 6

#     result = is_weekend_using_calendar(mock_calendar_obj)

#     assert result is True


from tasks import (
    get_count_field_from_object,
    ObjectDoesNotExists,
    get_epoch_time_stamp_as_str,
    get_stock_price
    )

from unittest.mock import Mock, patch
import pytest

def test_get_count_field_from_object_with_valid_details_returns_obj_count():

    # Arrange
    database_handler = Mock()
    data = Mock()
    data.count = 2
    database_handler.get.return_value = data

    # Act
    obj_count = get_count_field_from_object(database_handler, 1)

    # Assert
    assert obj_count == 2


def test_get_count_field_from_object_with_invalid_details_raise_exception():

    # Arrange
    database_handler = Mock()
    database_handler.get.side_effect = ObjectDoesNotExists

    # Act

    # Assert
    with pytest.raises(ObjectDoesNotExists):
        get_count_field_from_object(database_handler, 1)


from tasks import MyClass
import uuid

@patch.object(uuid, 'uuid4', return_value=1)
def test_is_valid_object(uuid):

    # Arrange
    expected_id = 1
    expected_name = "Hero"
    expected_age = 20

    # Act
    my_class_obj = MyClass(age=20, name="Hero")

    # Assert
    assert my_class_obj.id == expected_id
    assert my_class_obj.name == expected_name
    assert my_class_obj.age == expected_age



# Task 3
import time

@patch.object(time, 'time', return_value="1234567890")
def test_time(time):

    # Arrange
    expected_time = "1234567890"

    # Act
    result = get_epoch_time_stamp_as_str()

    # Assert
    assert result == expected_time

# Task 4
import requests

@patch.object(requests, 'get')
def test_stock_price(request):

    # Arrange
    price_obj = Mock()
    company_id = 1
    price_obj.content = '{"unit_price_in_inr": 123}'
    request.return_value = price_obj

    # Act

    result = get_stock_price(company_id)

    # Assert
    assert result == 123