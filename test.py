import os
from colorama import Fore, Style

class Product:
    def __init__(self, name, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
        self.name = name
    
    def getProductInfo(self):
        loadFromFile()
        if len(list) >= 1:
            for self in list:
                print(f"{Fore.LIGHTCYAN_EX}{Style.NORMAL}Name: ", f"{Fore.CYAN}", self.name, f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{Style.NORMAL}\nPrice: ", f"{Fore.GREEN}", self.price, f"{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}\nQuantity: ", f"{Fore.MAGENTA}", self.quantity.rstrip('\n'), f"{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}\nProduct ID: ", f"{Fore.YELLOW}", self.id, f"{Style.RESET_ALL}", "\n")
       
    def addProduct(self, list):
        product = Product(name = input(f"{Fore.BLUE}Enter product name: "), price = "$" + input(f"Enter price: {Fore.GREEN}$"), id = int(index1 + 1), quantity = input(f"{Fore.BLUE}Enter the quantity: {Fore.MAGENTA}"))
        list.append(product)
        
    def removeProduct(self):
        index = int(input(f"{Fore.GREEN}Enter the product ID of the product to remove: "))
        print('\n')
        while 0 < index <= len(list):
            print(f"{Fore.RED}", list[index-1].name, f"{Fore.GREEN}successfully removed!")
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
            break
        else:
            print(f"{Fore.RED}Product ID entered does not exist!{Style.RESET_ALL}")        
            
    def changeQuantity(self):
        newQuantity = int(input(f"{Fore.MAGENTA}Enter the product ID of the product to update: {Style.RESET_ALL}"))
        if 0 < newQuantity <= len(list):
            print(f"{Fore.GREEN}Current quantity:", list[newQuantity-1].quantity)
            productUpdate = input(f"{Fore.LIGHTYELLOW_EX}Enter new quantity: ")
            list[newQuantity-1].quantity = productUpdate
            print("\n")
            print(f"{Fore.MAGENTA}", list[newQuantity-1].name, f"quantity successfully updated!{Fore.RED}")
        else:
            print(f"Product ID entered does not exist!{Style.RESET_ALL}")

    def saveTofile(self):
        os.remove(filePath)
        for self in list:
            stringArr = [self.name, " ", self.price, " ", str(self.id), " ", self.quantity.rstrip('\n'), "\n"]
            with open(filePath, "ab") as file:
                for string in stringArr:
                    byteArray = string.encode()
                    file.write(byteArray)
            file.close()
    
def loadFromFile():
    i = 0
    list.clear()
    with open(filePath, "rb") as file:
        for string in file:
            byteArray = string.decode()
            data = byteArray.split(" ", 4)
            list.append(Product(data[0], data[1], i+1, data[3]))
            i += 1
    file.close()
    if i > 0: 
        global index1 
        index1 = int(list[i-1].id)
        return index1
    else:
        index1 = 1
        os.system('cls')
        print(f"{Fore.GREEN}{Style.BRIGHT}Product Catalog 1.0{Style.RESET_ALL}\n")
        print(f"{Fore.RED}No products in product.bin file!{Fore.MAGENTA}\n")
                
def menu():
    os.system('cls')
    print(f"{Fore.GREEN}{Style.BRIGHT}Product Catalog 1.0{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.DIM}-------Menu------{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}\n1: List Products")
    print("2: Add Product")
    print("3: Remove Product")
    print("4: Change Quantity")
    print(f"5: Exit\n{Style.RESET_ALL}")
    
    choice = input("")
    while choice != 5:
        match choice:
            case "1":
                os.system('cls')
                product.getProductInfo()
                input(f"{Fore.MAGENTA}Press any key to continue... {Style.RESET_ALL}")
                os.system('cls')
                menu()   
            case "2":
                os.system('cls')
                product.addProduct(list)
                product.saveTofile()
                input(f"{Fore.MAGENTA}Press any key to continue... {Style.RESET_ALL}")
                os.system('cls')
                menu()
            case "3":
                os.system('cls')
                loadFromFile()
                if index1 > 0:
                    product.removeProduct()
                    input(f"{Fore.MAGENTA}\nPress any key to continue... {Style.RESET_ALL}")
                    loadFromFile()
                    product.saveTofile()
                    os.system('cls')
                    menu()
                else: 
                    os.system("cls")
                    print(f"{Fore.GREEN}{Style.BRIGHT}Product Catalog 1.0{Style.RESET_ALL}\n")
                    print(f"{Fore.RED}No products in product.bin file!{Fore.MAGENTA}\n")
                    input(f"{Fore.MAGENTA}\nPress any key to continue... {Style.RESET_ALL}")
                    menu()
            case "4":
                os.system('cls')
                if index1 > 0:
                    product.changeQuantity()
                    product.saveTofile()
                    input(f"{Fore.MAGENTA}Press any key to continue... {Style.RESET_ALL}")
                    os.system("cls")
                    menu()
            case "5": 
                os.system('cls')
                product.saveTofile()
                print(f"{Fore.LIGHTCYAN_EX}Goodbye!{Style.RESET_ALL}")
                break
            case _:
                os.system('cls')             
                print(f"{Fore.RED}Invalid menu choice!\n{Fore.MAGENTA}")
                input(f"Press any key to continue... {Style.RESET_ALL}")
                menu()
        return 0
filePath = "product.bin"       
list = []
product = Product("name", "price", 0, "quantity")

loadFromFile()
menu()