from flask import jsonify,request
from flask_restful import Resource
from flask_expects_json import expects_json
from Controllers.Instance import products,ProductBLL

newProductModel = {
    'type':'object',
    'properties':{
        'name': {'type':'string'},
        'price': {'type':'number'}, 
        'quantity':{'type':'number'} 
    },
    'required':['name','price','quantity']
}

#Related operations to products entity
class Products():
    #Transactions that does not require any query on url
    class Default(Resource):
        #get all products
        def get(self):
            return jsonify({'products':products,'message':'found '+ str(len(products)) + ' matches'})    

        #add new product
        @expects_json(newProductModel)
        def post(self):
            # newProduct= ProductBLL().validateNewProduct(request.json)
            newProduct = request.json
            products.append(newProduct)
            return jsonify({'message':'product added successfully!',"products":products})            
        
        

    
    #Transactions that require query on url by product name
    class QueryByProductName(Resource):
        #get specific product by product_name
        def get(self,product_name):
            print(product_name)
            resp = [p for p in products if p['name']==product_name]
            return jsonify({'products':resp,'message':'found '+ str(len(resp)) + ' matches'})

        #update specific product by product name
        def put(self,product_name):
            productFound = [p for p in products if p['name'] == product_name]
            if productFound:
                productFound[0]['name'] = request.json['name']
                productFound[0]['price'] = request.json['price']
                productFound[0]['quantity'] = request.json['quantity']
                return jsonify({
                    "message": 'Product updated',
                    "product": productFound[0]
                    })
            return jsonify({"message":"product not found"})

        #delete specific product by product name
        def delete(self,product_name):
            productFound = [p for p in products if p['name'] == product_name]
            if productFound:
                products.remove(productFound[0])
                return jsonify({"message":"product deleted","products":products})
            return jsonify({"message":"product not found"})

