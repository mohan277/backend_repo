from .models import *

def profile():
    def decorator(func):
        def handler(*args, **kwargs):
            import line_profiler
            profiler = line_profiler.LineProfiler()
            profiler.enable_by_count()
            
            profiler.add_function(func)
            from django.db import connection
            initial_count = len(connection.queries)
            result = func()
            later_count = len(connection.queries)
            print("Total Number of Hits:",later_count-initial_count)
            # result = func(*args, **kwargs)
            profiler.print_stats()
            return result
        handler.__doc__ = func.__doc__
        return handler
    return decorator

@profile()
def my_function():
    import time
    time.sleep(2)
    print("Exiting my function")

@profile()
def get_books_by_library_id(book_ids):
    from db_optimization.models import Book
    from collections import defaultdict
    result = defaultdict(list)
   
    for book_id in book_ids:
        book = Book.objects.get(id=book_id)
        result[book.library_id].append(book)
    # return result

@profile()
def get_books_by_library_id_one_query(book_ids):
    from db_optimization.models import Book
    from collections import defaultdict
    books = Book.objects.filter(id__in=book_ids)
    result = defaultdict(list)
    
    for book in books:
        result[book.library_id].append(book)
    # return result