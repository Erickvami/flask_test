from pymongo import MongoClient
import sys
import os
client= MongoClient(host= 'mongodb://db:27017') 
db= client.Storage
# docs = db['Products']

class Products():
    def __init__(self):
        pass
    def getAllProducts(self):
        products = list(db.product.find({},{'_id': False}))
        return products
        # return {'products':products,'message':'found '+ str(products.count + ' matches'}
    
    def getProductByName(self,product_name):
        products= list(db.product.find({"name":product_name},{'_id': False}).limit(1))
        # return {'products':products}
        return products
    
    def addProduct(self,newProduct):
        try:
            db.product.insert_one(newProduct)
            return True
        except Exception as ex:
            return False
    
    def updateProduct(self,product_name,updatedProduct):
        try:
            db.product.update({"name":product_name},{'$set':updatedProduct})
            return True
        except:
            return False        
    def removeProduct(self,product_name):
        try:
            db.product.delete_one({"name":product_name})
            return True
        except:
            return False