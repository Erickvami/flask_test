from BLL.Instance import Products
class ProductBLL():
    def validateNewProduct(self,data):
        return data

    def getAllProducts(self):
        products= Products().getAllProducts()
        return {'products':products,'message':'found '+ str(len(products)) + ' matches'} 
    
    def getProductByName(self,product_name):
        products= Products().getProductByName(product_name)
        return {'products':products,'message':'found '+ str(len(products)) + ' matches'} 
    
    def addProduct(self,newProduct):
        dal= Products()
        if dal.addProduct({
                "name":newProduct["name"],
                "price":newProduct["price"],
                "quantity":newProduct["quantity"]
                }):
            return {"message":'product added successfully!',"products":dal.getAllProducts()} 
        
        return {"message":'Error:',"products":dal.getAllProducts()}

    def updateProduct(self,product_name,updatedProduct):
        dal= Products()
        productFound = dal.getProductByName(product_name)
        if productFound:
                productFound[0]['name'] = updatedProduct['name']
                productFound[0]['price'] = updatedProduct['price']
                productFound[0]['quantity'] = updatedProduct['quantity']
                if dal.updateProduct(product_name,updatedProduct):
                    return {"message":'product updated',"product":productFound[0]}
                return {"message":'Error:Can\'t finish transaction'}
        return {"message":"product not found"}
        

    def removeProduct(self,product_name):
        dal= Products()
        productFound = dal.getProductByName(product_name)
        if productFound:
            if dal.removeProduct(product_name):
                return {"message":"product deleted","products":dal.getAllProducts()}
            return {"message":"Not found or can't be deleted","products":dal.getAllProducts()} 
        return {"message":"product not found"}
        