from BLL.Instance import Products
class ProductBLL():
    def validateNewProduct(self,data):
        return data

    def getAllProducts(self):
        return Products().getAllProducts()
    
    def getProductByName(self,product_name):
        return Products().getProductByName(product_name)
    
    def addProduct(self,newProduct):
        return Products().addProduct(newProduct)
    
    def updateProduct(self,product_name,updatedProduct):
        productFound = self.getProductByName(product_name)
        if productFound:
                productFound[0]['name'] = updatedProduct['name']
                productFound[0]['price'] = updatedProduct['price']
                productFound[0]['quantity'] = updatedProduct['quantity']
                return Products().updateProduct(product_name,updatedProduct)
        return {"message":"product not found"}
        

    def removeProduct(self,product_name):
        productFound = self.getProductByName(product_name)
        if productFound:
            Products.removeProduct(product_name)
            return {"message":"product deleted","products":Products().getAllProducts()}
        return {"message":"product not found"}
        