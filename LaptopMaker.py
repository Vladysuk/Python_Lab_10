from Laptop import Laptop

if __name__ == "__main__":

    laptop1 = Laptop()
    laptop2 = Laptop(2.6, 8, "HP", "Nvidia 1050Ti", "IPS Full HD", 800)
    laptop3 = Laptop(2.0, 4, "Acer", "Nvidia 1030", "IPS Full HD", 450)

    print("_________")
    print(laptop1)
    print("_________")
    print(laptop2)
    print("_________")
    print(laptop3)

    print(Laptop.get_keyboard())