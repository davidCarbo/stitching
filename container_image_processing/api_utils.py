from flask import abort, jsonify, current_app
from jsonschema import ValidationError
import jsonschema
import json
from functools import wraps

def validate_schema(args, schema):
    try:
        jsonschema.validate(args, schema)
    except json.decoder.JSONDecodeError as e:
        return handle_error(e, schema)
    except ValidationError as e:
        return handle_error(e, schema)
    except Exception as e:
        return handle_error(e, schema)
    return True

# def validate_schema(args, schema):
#     def decorator(f):
#         def wrapper(*args, **kwargs):
#             try:
#                 jsonschema.validate(args, schema)
#             except json.decoder.JSONDecodeError as e:
#                 return handle_error(e, schema)
#             except ValidationError as e:
#                 return handle_error(e, schema)
#             except Exception as e:
#                 print(e)
#                 return handle_error(e, schema)
#             return f(*args, **kwargs)
#         return wrapper
#     return decorator

def handle_error(e, schema=None):
    if isinstance(e, ValidationError):
        subschema = schema
        for path_point in e.schema_path:
            subschema = subschema.get(path_point, None)
            if not subschema:
                return f"{e.validator}-mismatch on path {list(e.path)}", 400
        message = f"""
            {e.validator}-mismatch on path {list(e.path)}.
            Expected {e.validator}: {subschema}
            Full Message: {e.message}
        """
        return jsonify(error= message), 403
    code = e.code
    return jsonify(error=str(e)), code

def debug_only(f):
    @wraps(f)
    def wrapped(**kwargs):
        if not current_app.debug:
            abort(404)
        return f(**kwargs)
    return wrapped