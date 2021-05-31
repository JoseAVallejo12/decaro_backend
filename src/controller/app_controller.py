from flask import request
import random
from repository.implement.engine_mysql import DB_storage
from repository.empleados import Empleados

class ControllerApp(object):

    __storage = None

    def __init__(self) -> None:
        self.__storage = DB_storage()

    def get_user(self):
        user = request.get_json().get('usuario')
        user_schema = self.__storage.find_one(user)
        return self.__query_to_dict(user_schema)

    def get_users(self):
        response = []
        res = self.__storage.find()
        if(res):
            for items in res:
                obj = {}
                for key, value in items.__dict__.items():
                    obj.update({key: value})
                if (obj.get('_sa_instance_state')):
                    obj.pop('_sa_instance_state')
                response.append(obj)
        return response

    def create_user(self):
        user_data = request.get_json()
        new = Empleados(**user_data)
        new.usuario = f'{new.primer_nombre[:3]}{new.primer_apellido[:3]}'
        new.clave = random.randint(10000, 99000)
        response = self.__storage.new(new)
        return self.__query_to_dict(response)

    def update_user(self):
        response = self.__storage.update(request.get_json())
        return self.__query_to_dict(response)

    def delete_uer(self):
        user_list = request.get_json()
        list_deleted_users = []
        if (isinstance(user_list.get('usuario'), list)):
            for id in user_list.get('usuario'):
                if self.__storage.delete_by_id(id):
                    list_deleted_users.append(id)
        return {
            'userDeleted': f'Id de usuarios borrados {list_deleted_users}'
        }

    def __query_to_dict(self, schema):
            res = {}
            if (schema):
                for items in schema:
                    for key, value in items.__dict__.items():
                        res.update({key: value})
                if (res.get('_sa_instance_state')):
                    res.pop('_sa_instance_state')
            return res