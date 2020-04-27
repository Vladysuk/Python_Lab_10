from Laptop import Laptop

if __name__ == "__main__":

    laptop1 = Laptop()
    laptop2 = Laptop(2.6, 8, "HP", "Nvidia 1050Ti", "IPS Full HD", 800)
    laptop3 = Laptop(2.0, 4, "Acer", "Nvidia 1030", "IPS Full HD", 450)

    for laptop in [laptop1, laptop2, laptop3]:
        print(laptop)

    print(Laptop.get_keyboard())
