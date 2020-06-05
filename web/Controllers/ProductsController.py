from flask import jsonify,request
from flask_restful import Resource
from flask_expects_json import expects_json
from Controllers.ValidationModels.ProductModel import ProductModel
from Controllers.Instance import ProductBLL

#Related operations to products entity
class Products():
    #Transactions that does not require any query on url
    class Default(Resource):
        #get all products
        def get(self):
            return jsonify(ProductBLL().getAllProducts())    

        #add new product
        @expects_json(ProductModel)
        def post(self):
            newProduct = request.json
            return jsonify(ProductBLL().addProduct(newProduct))            
    
    #Transactions that require query on url by product name
    class QueryByProductName(Resource):
        #get specific product by product_name
        def get(self,product_name):
            return jsonify(ProductBLL().getProductByName(product_name))

        #update specific product by product name
        def put(self,product_name):
            return jsonify(ProductBLL().updateProduct(product_name,request.json)) 

        #delete specific product by product name
        def delete(self,product_name):
            return jsonify(ProductBLL().removeProduct(product_name))

