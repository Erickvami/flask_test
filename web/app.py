from flask import Flask
from flask_restful import Api
from Controllers.ProductsController import Products
from Controllers.RedisController import RedisController

#Initialize application
app = Flask(__name__)
api = Api(app)

#Routing resources
#Routes for transactions related to products

#Transactions that does not require any query on url
api.add_resource(Products.Default,'/products/',methods=['GET','POST'])
#Transactions that require query on url by product name
api.add_resource(Products.QueryByProductName,'/products/<string:product_name>',methods=['GET','PUT','DELETE'])

api.add_resource(RedisController.RedisDefault,'/redis/',methods=['GET','POST'])
#Default api route
@app.route('/')
def home():
    return 'API Ready!!!'

#Init api service
if __name__ == '__main__':
    app.run(host='0.0.0.0')

