from flask_restful import Resource, reqparse
from flask import request
import werkzeug


class Upload(Resource):

    def get(self):
        pass
        #data = request.get_json

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        audioFile = args['file']
        audioFile.save("your_file_name.jpg")
        return {'status' : 'sucess'}



class UploadWavAPI(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('audio', type=werkzeug.FileStorage, location='files')

        args = parse.parse_args()

        stream = args['audio'].stream
        wav_file = wave.open(stream, 'rb')
        signal = wav_file.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        fs = wav_file.getframerate()
        wav_file.close()


from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug


    class UploadAudio(Resource):
      def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        audioFile = args['file']
        audioFile.save("your_file_name.jpg")


class UploadImage(Resource):
    def post(self, fname):
        file = request.files['file']
        if file and allowed_file(file.filename):
            # From flask uploading tutorial
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            # return error
            return {'False'}