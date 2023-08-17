class Product:
    def __init__(self, name, price):
        print("It's __init__")
        self.name = name
        self.price = price


if __name__ == '__main__':
    product = Product('Car', 15000)
    print(product.price)
    print(product.name)
    