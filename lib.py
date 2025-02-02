# Cafe Management System
# We use python dictionery and conditional statements ..
menu={
    "Cheese Burgur": 34,"Cheese Sandwich": 22,"Chiken Burgurs": 23,
    "Fruit Salad":13,"Cocktails":12,"Nuggets":14,"Sandwich":13,"French Fries":15,
    "Milk Shake":3,"Iced Tea":2,"Orange Juice":4,"Lemon Tea":3,"Coffee":5
}

print("Welcome to Our Chai Churi")
print("MAIN COURSE\nCheese Burgur    : $34\nCheese Sandwich    : $22\nChiken Burgurs    : $23")   # showing Menu to customers
print("APPENTIZERS\nFruit Salad    : $13\nCocktails    : $12\nNuggets    : $14\nSandwich    : $13\nFrench Fries    : $15")
print("BEVERAGES\nMilk Shake    : $3\nIced Tea    : $2\nOrange Juice   : $4\nLemon Tea    : $3\nCoffee   : $5") 

order_total=0
item=input("Order something..")  # customer enters items to order
if item in menu:
    order_total+=menu[item]
    print(f"{item} has been added to the Order. ")
    
else:
    print("Order Unavailable ")
another_order=input("Do you want another order ? (Yes/No)")
if another_order=="Yes":
    item=input("Order something..")
    if item in menu:
        order_total+=menu[item]
        print(f"{item} has been added to the Order. ")
    else:
        print("Order Unavailable ")
print(f"The Total amount of items to pay ${order_total}")        
print("Thanks For Visting At Chai Churi cafe")