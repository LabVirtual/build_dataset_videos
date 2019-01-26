from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from register import Register
#from upload import Upload
from sigin import Sigin


app = Flask(__name__)
api = Api(app)

api.add_resource(Register, '/register')
api.add_resource(Sigin, '/sigin')
#api.add_resource(Upload, '/upload')


if __name__ == '__main__':
    app.run(debug=True)