from flask_cors import CORS
from flask import Flask, make_response, jsonify
from flask_jwt_extended import JWTManager
from routes.app_route import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JWT_SECRET_KEY'] = 'sfohpdoiavnsiocjlJHAHGShgdgfliogfsbsyd'  # Change this!

jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """
    404 Error
        ---
        responses:
        404:
            description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
