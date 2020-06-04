from pymongo import MongoClient
import sys

client= MongoClient('mongodb://db:27017') 
db= client.Storage
docs = db['Products']
class Products():
    def __init__(self):
        pass
    def getAllProducts(self):
        products = docs.find({})
        print(products)
        return {'products':products,'message':'found '+ str(products.count()) + ' matches'}
    
    def getProductByName(self,product_name):
        products= docs.find({"name":product_name}).limit(1)
        return {'products':products,'message':'found '+ str(products.count()) + ' matches'}
    
    def addProduct(self,newProduct):
        try:
            docs.insert(newProduct)
            return {"message":'product added successfully!',"products":self.getAllProducts()}
        except:
            return {"message":'Error:' + str(sys.exc_info()[0]),"products":self.getAllProducts()}
    
    def updateProduct(self,product_name,updatedProduct):
        try:
            docs.update({"name":product_name},{'$set':updatedProduct})
            return {"message":'product updated',"product":self.getProductByName(product_name)}
        except:
            return {"message":'Error:' + sys.exc_info()[0]}        
    def removeProduct(self,product_name):
        try:
            docs.delete_one({"name":product_name})
            return {"message":"product deleted","products":self.getAllProducts()}
        except:
            return {"message":"Not found or can't be deleted","products":self.getAllProducts()} 