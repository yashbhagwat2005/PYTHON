shop = {}
ch = input("Do you want to the update shop's database?")
while ch not in 'nN':
    product = input("Enter the product's name: ")
    price = float(input("Enter the price: "))
    shop[product] = price
    product = ''
    price = 0
    ch = input("Do you want to continue: ")
product = input("Enter the product's name to which's you want to find the price of: ")
for keys in shop:
    if(keys==product):
        print(f"The price of the {product} is {shop[keys]}")
        break
else:
    print("Sorry the product does not exist")



    