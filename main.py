from App import *

catalogo = catalog()
#description,quantity,price,image,supplier.
catalogo.addProduct(1,"teclado usb",10,2000,"tecladoUsb.jpg",101)
catalogo.addProduct(2,"mouse usb",10,5000,"mouseUsb.jpg",102)
catalogo.addProduct(3,"Monitor LCD 22 pulgadas",10,20000,"MonitorLCD.jpg",103)
catalogo.addProduct(4,"mause pad",10,1000,"mausePad.jpg",104)
catalogo.addProduct(5,"silla gamer",10,45000,"sillaGamer.jpg",105)
catalogo.listProduct()

print(catalogo.queryProduct(3))
catalogo.editProduct(3,"Monitor 27 pulgadas",2,35000,"MonitorLCD.jpg",107)
print(catalogo.queryProduct(3))
catalogo.listProduct()
catalogo.deleteProduct(3)
catalogo.listProduct()
catalogo.showProduct(3)
catalogo.showProduct(2)