from flask import Flask, jsonify
from config import config


def create_app(config_name='default'):
    '''creates app module for flask'''
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    
    @app.route("/")
    def index():
        return "Hello World"
    
    @app.route('/users/ping', methods=['GET'])
    def ping_pong():
        return jsonify({
            'status': 'success',
            'message': 'pong!'
            })
    
    return app
