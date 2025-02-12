cart = []

def add_item(item):
    cart.append(item)

def view_cart():
    print("Cart:", cart)

if __name__ == "__main__":
    add_item("Laptop")
    add_item("Phone")
    view_cart()
