from pymongo import MongoClient
import sys

client= MongoClient(host= 'mongodb://db:27017') 
db= client.Storage
# docs = db['Products']

class Products():
    def __init__(self):
        pass
    def getAllProducts(self):
        products = list(db.product.find())
        return {'products':products}
        # return {'products':products,'message':'found '+ str(products.count + ' matches'}
    
    def getProductByName(self,product_name):
        products= list(db.product.find({"name":product_name}).limit(1))
        return {'products':products}
        # return {'products':products,'message':'found '+ str(products.count + ' matches'}
    
    def addProduct(self,newProduct):
        try:
            db.product.insert_one(newProduct)
            return {"message":'product added successfully!',"products":self.getAllProducts()}
        except Exception as ex:
            return {"message":'Error:',"products":self.getAllProducts()}
    
    def updateProduct(self,product_name,updatedProduct):
        try:
            db.product.update({"name":product_name},{'$set':updatedProduct})
            return {"message":'product updated',"product":self.getProductByName(product_name)}
        except:
            return {"message":'Error:'}        
    def removeProduct(self,product_name):
        try:
            db.product.delete_one({"name":product_name})
            return {"message":"product deleted","products":self.getAllProducts()}
        except:
            return {"message":"Not found or can't be deleted","products":self.getAllProducts()} 