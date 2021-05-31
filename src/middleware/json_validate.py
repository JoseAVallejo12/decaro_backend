from flask import request, make_response, jsonify
from functools import wraps
from .json_schema import schema


def json_validate(func):
    @wraps(func)
    def json_input(*args, **kwargs):
        try:
            validation_result = schema.validate(request.get_json())
            if validation_result.get('success'):
                func(*args, **kwargs)
        except Exception as err:
            return make_response(jsonify({'err': 'err'}), 400)


    return json_input
