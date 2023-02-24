def get_action(key):
    keys = {
        "w": "UP",
        "a": "LEFT",
        "s": "DOWN",
        "d": "RIGHT",
        " ": "SPACE",
    }
    if key in keys:
        return keys[key]
    return "ANY"
