
route = {}

def get_route(name):
    def func(func):
        route[name] = func
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return func