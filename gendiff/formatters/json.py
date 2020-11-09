import json


def render_json(diff_dict):
    return json.dumps(diff_dict, indent='    ', sort_keys=True)
