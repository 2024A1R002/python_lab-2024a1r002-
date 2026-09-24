#write a menu-driven python program where the user  can add items remove items view cart and exitcart = []
cart =[]
while True:
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        cart.append(item)

    elif choice == 2:
        item = input("Enter item: ")
        cart.remove(item)

    elif choice == 3:
        print("Cart:", cart)

    elif choice == 4:
        break

    else:
        print("Wrong choice")