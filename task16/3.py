#create a product class with htotal cost. Take these values from the user and display the product name and totalcost
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def  calculate_total(self):
        return self.price * self.quantity

name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

product = Product(name, price, quantity)
print(f"Product: {product.name}")
print(f"Total Cost: {product.calculate_total()}")