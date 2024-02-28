import os

class Product:
    def __init__(self, name, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
        self.name = name
    
    def getProductInfo(self):
        if len(list) >= 1:
            for self in list:
                print("Name: ", self.name, "\nPrice: ", self.price, "\nQuantity: ", self.quantity.rstrip('\n'), "\nProduct ID: ", self.id, "\n")
            else:
                print("No products to display!")
         
    def addProduct(self, list):
        product = Product(name = input("Enter product name: "), price = input("Enter price: "), id = int(index1 + 1), quantity = input("Enter the quantity: "))
        list.append(product)
        
    def removeProduct(self):
        index = int(input("Enter the product ID of the product to remove: "))
        if 0 < index:
            with open(filePath,'rb') as read_file:
                lines = read_file.readlines()
                currentLine = 1
            with open(filePath,'wb') as write_file:
                for line in lines:
                    if currentLine == index:
                        pass
                    else:
                        write_file.write(line)
                    currentLine += 1
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
        os.remove(filePath)
        for self in list:
            stringArr = [self.name, " ", self.price, " ", str(self.id), " ", self.quantity.rstrip('\n'), "\n"]
            print(stringArr)
            with open(filePath, "ab") as file:
                for string in stringArr:
                    byteArray = string.encode()
                    file.write(byteArray)
            file.close()
    
def loadFromFile():
    i = 0
    with open(filePath, "rb") as file:
        for string in file:
            byteArray = string.decode()
            data = byteArray.split(" ", 4)
            list.append(Product(data[0], data[1], data[2], data[3]))
            i = i + 1
    file.close() 
    global index1 
    index1 = int(list[i-1].id)
    return index1
                
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
product = Product("name", "price", 0, "quantity")

loadFromFile()
menu()