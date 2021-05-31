from flask import make_response, jsonify, request
from datetime import timedelta
from flask import Blueprint
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)

from middleware.app_auth import auth_basic
from middleware.json_validate import json_validate
from controller.app_controller import ControllerApp


controller = ControllerApp()
app_views = Blueprint('app_views', __name__, url_prefix='/api')

@app_views.route('/login', methods=['POST'], strict_slashes=False)
@auth_basic
def login_user():
    user_data = {}
    username = get_jwt_identity()
    expires = timedelta(hours=2)
    token = create_access_token(username, expires_delta=expires)
    user_data.update({
        'user_name': request.get_json().get('usuario'),
        'logged': True,
        'access_token': token,
        'token_type': 'bearer',
        'user_inf': controller.get_user()
    })

    return make_response(jsonify(user_data), 200)

@app_views.route('/user/new', methods=['POST'], strict_slashes=False)
@jwt_required
def update_user():
    current_user = get_jwt_identity()
    res = controller.create_user()
    return make_response(jsonify(res), 200)

@app_views.route('/user/update', methods=['POST'], strict_slashes=False)
@jwt_required
def new_user():
    res = controller.update_user()
    return make_response(jsonify(res), 200)


@app_views.route('/user/delete', methods=['POST'], strict_slashes=False)
@jwt_required
def delete_user():
    print('entrando en delete route')
    res = controller.delete_uer()
    return make_response(jsonify(res), 200)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@jwt_required
def get_all_users():
    return make_response(jsonify(controller.get_users()), 200)