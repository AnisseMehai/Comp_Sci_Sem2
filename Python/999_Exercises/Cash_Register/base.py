numItems = int(input("How many items"))
total = 0
for i in range(0,numItems):
    item = input("Whats the item? ")
    price = float(input("Whats the price? "))
    print("Thanks for buying" + item)
    total = total + price
print("Your total is: " + str(total))