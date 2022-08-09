garment = 20
while garment:
    number = int(input("Please enter the number of the products you bough:"))
    garment = garment - number
    if garment == 0:
        print("out of stock")
        break