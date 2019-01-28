from flask_restful import Resource, reqparse
import werkzeug


class Upload(Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('info', type=dict, location='json')  #TODO
        args = parse.parse_args()
        audioFile = args['file']
        audioFile.save("your_file_name.jpg")

        return {'status' : 'sucess'}