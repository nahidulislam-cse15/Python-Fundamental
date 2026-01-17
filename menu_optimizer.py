menu= { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }
#Display
print("Menu List:")
for key, value in menu.items():
    print(f"{key}: {value}")

#Remove expensive item
# for key, value in menu.items():
#     if value>10:
#         menu.pop(key)
# print(menu)
for key in list(menu.keys()):
    if menu[key]>10 :
        menu.pop(key)

print(menu)
