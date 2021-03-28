from flask import  Flask,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def __init__(self):
        pass

    def get(self):
        return "sucess";

api.add_resource(HelloWorld,'/')
if __name__ == '__main__':
    app.run(debug=True)