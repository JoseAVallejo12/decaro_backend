from flask import request, make_response, jsonify, globals
from functools import wraps
from repository.implement.engine_mysql import DB_storage
storage = DB_storage()

def auth_basic(func):
    @wraps(func)
    def auth_middleware(*args, **kwargs):
        usuario = ''
        clave = ''
        keys = list(request.get_json().keys())
        if 'usuario' in keys and 'clave' in keys:
            usuario = request.get_json().get('usuario')
            clave = request.get_json().get('clave')

            if usuario == 'admin' and clave == 'admin':
                return func(*args, **kwargs)
            else:
                user_db = storage.find_one(usuario)
                for i in user_db:
                    if i.usuario == usuario and clave == i.clave:
                        return func(*args, **kwargs)

            return make_response(jsonify({'err': f'user {usuario} not be autorized'}), 400)

        return make_response(jsonify({'err': f'{keys}, keys must be [email, password]'}), 400)

    return auth_middleware