# Create menu of 4+ items sold in cafe
# Creat a dictionary to hold a value of the stock for each item
# Create another dictionary with the prices
# Calculate the total stock in the cafe (stock x price)

import math

# Dictinary containing current stock levels for each item
stock_dict = {'Tea' : 18,
         'Coffee' : 11, 
         'Hot Chocolate' : 14,
         'Water' : 37,
         'Croissant' : 8,
         'Pan au Chocolat' : 10
          }

# Dictionary containing current price for each item
price_dict = {'Tea' : 1.5,
         'Coffee' : 2, 
         'Hot Chocolate' : 2,
         'Water' : 1,
         'Croissant' : 2.5,
         'Pan au Chocolat' : 3
          }

# List of menu items sold in cafe
menu_list  = ["Tea", "Coffee", "Hot Chocolate", "Water", "Croissant", "Pan au Chocolat"]

# Convert the stock dictionary values into a list
# Convert the price dictionary values into a list
# So we can multiply them together
stock_dict_values = list(stock_dict.values())
price_dict_values = list(price_dict.values())

# Make a new list to collect individual item stocks after each iteration
item_stock_list = []

# Iterate through for the number of items in menu list
# Print the stock total for each item
# Save the item stock into a new list so we can calculate the total
for i in range(len(menu_list)):
    item_stock = (stock_dict_values[i]) * (price_dict_values[i])
    print(f"{menu_list[i]} stock is £{item_stock}")
    item_stock_list.append(item_stock)

# Print out the sum of the item stock list to get a total
print( )
print(f"The total stock = £{sum(item_stock_list)}")
