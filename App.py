class catalog:
    products=[]

    def addProduct (self, code, description, quantity, price, image, supplier):
        
        if self.queryProduct(code):
            return False#checks if the product is in the list. If it is, it returns false. 
        newProduct = {'code' = code,
                        'description' = description,
                        'quantity'= quantity,
                        'price'= price,
                        'image'= image,
                        'supplier'= supplier}        
        self.products.append(newProduct)
        return True # confirms that the product was added
    
    def queryProduct(self, code):
        for product in (self.product):
            if product["code"] == code:
                return product
        return False #reports that the product is not in the list
    
    def editProduct(self, code, newDescription, newQuantity, newPrice, newImage, newSupplier):
        for product in self.products:
            if product['code']== code:
                product['description']=newDescription
                product['quantity']=newQuantity
                product['price']=newPrice
                product['image']=newImage
                product['supplier']=newSupplier
                return True
            return False#returns false if the product is not present
        
    def listProduct (self):
        print("*"*50)
        for product in self.products:
            print(f"code.........: {product["code"]}")
            print(f"description..: {product["description"]}")
            print(f"quantity.....: {product["quantity"]}")
            print(f"price........: {product["price"]}")
            print(f"supplier.....: {product["supplier"]}")
            print("*"*50)
    
    def deleteProduct(self, code):
        for product in self.products:
            if product["code"] == code:
                self.products.remove(product)
                return True
        return False
    
    def showProduct(self,code):

        product = self.inquiryProduct(code)
        if product:
            print("*"*50)
            print(f"code.........: {product["code"]}")
            print(f"description..: {product["description"]}")
            print(f"quantity.....: {product["quantity"]}")
            print(f"price........: {product["price"]}")
            print("*"*50)
        else:
            print(f": the product {product["supplier"]} does not exist")
    




