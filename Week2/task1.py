import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        #result = json.loads(*args, **kwargs)
        result = json.dumps(func(*args, **kwargs))
        #result = func(*args, **kwargs)
        return result
    return wrapped
