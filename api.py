from flask import Flask 
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parcel_orders = []

class ParcelOrders(Resource):
    def get(self):
        return parcel_orders

    def post(self):
        #Alternative https://marshmallow.readthedocs.io/en/3.0/
        parser = reqparse.RequestParser()
        parser.add_argument('destination')
        args = parser.parse_args()
        parcel_orders.append(args)
        return parcel_orders
     
class Order(Resource): 
    def get(self, index):
        return parcel_orders[int(index)]

    def put(self, index):
        parser = reqparse.RequestParser()
        parser.add_argument('destination')
        args = parser.parse_args()
        parcel_orders[int(index)].update(args)
        return parcel_orders


api.add_resource(Orders,'/v1/parcel_orders')
api.add_resource(Order,'/v1/parcel_orders/<index>')

if __name__ == '__main__':
    app.run(debug=True)
