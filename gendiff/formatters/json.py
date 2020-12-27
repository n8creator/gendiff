import json


def render(diff):
    return (json.dumps(diff, sort_keys=True))
