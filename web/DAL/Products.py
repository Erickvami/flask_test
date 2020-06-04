from pymongo import MongoClient
import sys
class Products():
    def __init__(self):
        self.db= MongoClient('mongodb://27017').Storage
        self.products = self.db['Products']
    def getAllProducts(self):
        products = self.products.find({})
        print(products)
        return {'products':products,'message':'found '+ str(len(products)) + ' matches'}
    
    def getProductByName(self,product_name):
        products= self.products.find({"name":product_name}).limit(1)
        return {'products':products,'message':'found '+ str(len(products)) + ' matches'}
    
    def addProduct(self,newProduct):
        try:
            self.products.insert(newProduct)
            return {"message":'product added successfully!',"products":self.getAllProducts()}
        except:
            return {"message":'Error:' + sys.exc_info()[0],"products":self.getAllProducts()}
    
    def updateProduct(self,product_name,updatedProduct):
        try:
            self.products.update({"name":product_name},{'$set':updatedProduct})
            return {"message":'product updated',"product":self.getProductByName(product_name)}
        except:
            return {"message":'Error:' + sys.exc_info()[0]}        
    def removeProduct(self,product_name):
        try:
            self.products.delete_one({"name":product_name})
            return {"message":"product deleted","products":self.getAllProducts()}
        except:
            return {"message":"Not found or can't be deleted","products":self.getAllProducts()} 