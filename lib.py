def get_direction(key):
    keys = {
        "w": "UP",
        "a": "LEFT",
        "s": "DOWN",
        "d": "RIGHT",
    }
    if key in keys:
        return keys[key]
    return None
