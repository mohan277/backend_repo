import time
from django.db import connection

def no_of_database_hits(func_call1):
    def wrapper(*args, **kwargs):
        print('args: {}'.format(args))
        print('kwargs: {}'.format(kwargs))
        hits_before_exection = len(connection.queries)
        result = func_call1(*args, **kwargs)
        hits_after_exection = len(connection.queries)
        total_hits = hits_after_exection - hits_before_exection
        print("no_of_database_hits: {}".format(total_hits))
        return result
    return wrapper

def run_time(func_call2):
    def wrapper(*args, **kwargs):
        print('args: {}'.format(args))
        print('kwargs: {}'.format(kwargs))
        start_time = time.time()
        result = func_call2(*args, **kwargs)
        end_time = time.time()
        total_run_time = end_time - start_time
        print("total_run_time  : {}".format(total_run_time))
        return result
    return wrapper
