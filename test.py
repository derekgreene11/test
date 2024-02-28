import os

class Product:
    def __init__(self, name, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
        self.name = name
    
    def getProductInfo(self):
            if len(listcpy) >= 1:
                for self in listcpy:
                    print("Name: ", self.name, "\nPrice: ", self.price, "\nQuantity: ", self.quantity, "\nProduct ID: ", self.id,"\n")
            else:
                print("No products to display!")
         
    def addProduct(self, list):
        product = Product(name = input("Enter product name: ") + " ", price = input("Enter price: ") + " ", id = len(listcpy) + 1, quantity = " " + input("Enter the quantity: " + " "))
        print("Product ID: ", len(listcpy) + 1)
        list.append(product)
        listcpy.append(product)
    
    def removeProduct(self):
        index = int(input("Enter the product ID of the product to remove: "))
        if 0 <= index < len(listcpy):
            print("Product removed!")
        else:
            print("Product ID entered does not exist!")
            
    def changeQuantity(self):
        newQuantity = (input("Enter the product ID of the product to update: "))
        if 0 <= newQuantity < len(list):
            productUpdate = input("Enter new quantity: ")
            list[newQuantity].quantity = productUpdate
        else:
            print("Product ID entered does not exist!")

    def saveTofile(self):
        for self in list:
            stringArr = [self.name, self.price, str(self.id), self.quantity, "\n"]
            with open(filePath, "ab") as file:
                for string in stringArr:
                    byteArray = string.encode()
                    file.write(byteArray)
            file.close()
        del list[:]
    
def loadFromFile():
    with open(filePath, "rb") as file:
        for string in file:
            byteArray = string.decode()
            data = byteArray.split(" ", 4)
            listcpy.append(Product(data[0], data[1], data[2], data[3]))
    file.close()     
                
def menu():
    os.system('cls')
    print("Product Catalog 1.0")
    print("-------Menu------")
    print("\n1: List Products")
    print("2: Add Product")
    print("3: Remove Product")
    print("4: Change Quantity")
    print("5: Save File")
    print("6: Exit\n")
    
    choice = input("")
    while choice != 5:
        match choice:
            case "1":
                os.system('cls')
                product.getProductInfo()
                input("Press any key to continue... ")
                os.system('cls')
                menu()   
            case "2":
                os.system('cls')
                product.addProduct(list)
                input("Press any key to continue... ")
                os.system('cls')
                menu()
            case "3":
                os.system('cls')
                product.removeProduct()
                input("Press any key to continue... ")
                os.system('cls')
                menu()
            case "4":
                os.system('cls')
                product.changeQuantity()
                input("Press any key to continue... ")
                os.system("cls")
                menu()
            case "5":
                os.system('cls')
                product.saveTofile()
                print("File saved!")
                input("Press any key to continue... ")
                os.system('cls')
                menu()
            case "6": 
                os.system('cls')
                product.saveTofile()
                print("Goodbye!")
                break
        return 0

filePath = "product.bin"       
list = []
listcpy = []
product = Product("name", "price", 0, "quantity")

loadFromFile()
menu()