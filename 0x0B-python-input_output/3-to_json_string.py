import json

def to_json_string(my_obj):
    """Returns the JSON representation of python object"""
    try:
        return json.dumps(my_obj)
    except Exception as e:
        print("Error dumping object to JSON: {}".format(e))
        return None
