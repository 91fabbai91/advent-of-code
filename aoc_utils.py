import logging
import functools
from time import process_time

def logging_func(*args, **kwargs):
    def decorator(func):
        logging.basicConfig(*args,**kwargs)
        def wrap_func(*args, **kwargs):
            logging.debug(f'Function {func.__name__!r} called with {args} and {kwargs}')
            return func(*args, **kwargs)
        return wrap_func
    return decorator


def timer_func(func):
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        t1 = process_time()
        result = func(*args, **kwargs)
        t2 = process_time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func