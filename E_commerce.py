# E-commerce System

class Product:

    def __init__(self, product_id, name, price):

        self.product_id = product_id
        self.name = name
        self.__price = price

    # Get Method
    def get_price(self):
        return self.__price

    # Set Method
    def set_price(self, price):

        if price > 0:
            self.__price = price
            print("Price Updated Successfully!")
        else:
            print("Invalid Price")

    def display(self):

        print("======== Product Details ========")
        print("Product Id :", self.product_id)
        print("Product Name :", self.name)
        print("Product Price :", self.__price)


# Child Class

class Mobile(Product):

    def __init__(self, product_id, name, price, brand, ram, storage):

        super().__init__(product_id, name, price)

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display(self):

        super().display()

        print("Product Brand :", self.brand)
        print("Product RAM :", self.ram, "GB")
        print("Product Storage :", self.storage, "GB")

    def buy(self):

        print("Order Placed Successfully!")
        print("Thank You for Shopping with Us.")


# Multiple Mobiles

mobiles = []

mobiles.append(Mobile(101, "iPhone 17", 85000, "Apple", 16, 256))
mobiles.append(Mobile(102, "Samsung S26", 70000, "Samsung", 12, 256))
mobiles.append(Mobile(103, "OnePlus 15", 60000, "OnePlus", 12, 512))


# Main Menu

while True:

    print("\n========== E-Commerce Menu =========")

    print("1. View Product")
    print("2. Check Price")
    print("3. Update Price")
    print("4. Buy Product")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        for mobile in mobiles:
            mobile.display()
            print("----------------------------")

    elif choice == 2:

        for mobile in mobiles:
            print(mobile.product_id, "-", mobile.name, "- ₹", mobile.get_price())

    elif choice == 3:

        pid = int(input("Enter Product ID : "))

        found = False

        for mobile in mobiles:

            if mobile.product_id == pid:

                new_price = float(input("Enter New Price : "))
                mobile.set_price(new_price)

                found = True
                break

        if not found:

            print("Product Not Found!")

    elif choice == 4:

        pid = int(input("Enter Product ID : "))

        found = False

        for mobile in mobiles:

            if mobile.product_id == pid:

                mobile.buy()

                found = True
                break

        if not found:

            print("Product Not Found!")
            
    elif choice == 5:

        print("Thank You!!!!")
        break

    else:

        print("Invalid Choice")

































'''
 
'''
