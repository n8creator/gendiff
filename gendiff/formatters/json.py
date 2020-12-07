import json


def render_json(diff):
    return (json.dumps(diff, sort_keys=True))
