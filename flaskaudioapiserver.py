# flask api version 
from flask import Flask, Response
from flask_restful import Api, Resource
import base64
app = Flask(__name__)
api = Api(app)
class Audio(Resource):
    def get(self):
        with open("exp.wav" , "rb") as fwav:
            audio_enc = base64.b64encode(fwav.read())
            

            data = {
                "type": f"{type(audio_enc)}",
                "content" : f"{(audio_enc.decode('utf-8'))}" 
            }
        return data

api.add_resource(Audio,"/wav")
        
if __name__ == "__main__":
    app.run(debug=True,port=80)