import asyncio


def new_event_loop_decorator(func):
    def wrapper(*args, **kwargs):
        if asyncio.get_event_loop().is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())
        return func(*args, **kwargs)

    return wrapper
