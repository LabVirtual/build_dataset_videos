from flask import Flask, Blueprint
from flask_restful import Api
from restfull_config import output_json
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import sys, logging, time
from flask_jwt import JWT


app = Flask(__name__)
api_bp  Blueprint('api',__name__)


# app.secret_key = 'Dese.Decent.Pups.BOOYO0OST'
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
api.representations = {'application/json': output_json}

# jwt = JWT(app, authenticate, identity)  # Auto Creates /auth endpoint
api.add_resource(Sigin,'/sigin/<>')  #TODO

app.register_blueprint(api_bp)

socketio = SocketIO(app)
socketio.on_namespace(ChatChannel('/upload'))


def config_log():
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    level = logging.DEBUG
    if len(sys.argv) > 1:
        sys.argv
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)

    logging.basicConfig(filename='app.log', level=level)
    if level.__eq__(logging.DEBUG):
        logging.getLogger().addHandler(logging.StreamHandler())


if __name__ == '__main__':
    from db import mongo  # Avoid circular import
    config_log()
    mongo.configDb(app)
    socketio.run(app)
    app.run(debug=True)  # important to mention debug=True



