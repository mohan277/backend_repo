# Task 1
class ObjectDoesNotExists(Exception):
    pass

def get_count_field_from_object(database_handler, object_id):

    try:
        obj = database_handler.get(id=object_id)
    except Exception:
        raise ObjectDoesNotExists

    return obj.count

# Task 2
class MyClass:
    def __init__(self, name, age):
        import uuid
        self.id = uuid.uuid4()
        self.name = name
        self.age = age

# Task 3
import time

def get_epoch_time_stamp_as_str():
    return str(time.time())

# Task 4
class Timeout(Exception):
    pass

def get_stock_price(company_id):
    import requests
    import json
    from requests.exceptions import Timeout
    try:
        response = requests.get(" http://www.mocky.io/v2/5eb664e831000057006999f3")
    except Timeout:
        raise Exception('Request timedout')
    result = json.loads(response.content)

    return result['unit_price_in_inr']