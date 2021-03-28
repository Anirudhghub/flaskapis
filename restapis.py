from flask import  Flask,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)
user=[]
class Restapis(Resource):
    def __init__(self):
        pass

    def get(self,name):
        if name in user:
            return "found"+name
    
    def post(self,name):
        user.append(name)
        return "Added"+name

    def delete(self,name):
        user.remove(name)
        return "Deleted"+name

api.add_resource(Restapis,'/post/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)