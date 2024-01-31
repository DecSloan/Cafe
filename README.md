# Cafe
**Use dictionaries and lists to store and access saved information regarding stock levels**

The aim of this task is calculate the total stock in the cafe from the individual item stock levels and prices.

---
## Dictionaries

I created two seperate dictionaries, one for the current stock levels 'stock_dict' and one containing the current price 'price_dict'.

    import math

    stock_dict = {'Tea' : 18,
             'Coffee' : 11, 
             'Hot Chocolate' : 14,
             'Water' : 37,
             'Croissant' : 8,
             'Pan au Chocolat' : 10
              }

    price_dict = {'Tea' : 1.5,
             'Coffee' : 2, 
             'Hot Chocolate' : 2,
             'Water' : 1,
             'Croissant' : 2.5,
             'Pan au Chocolat' : 3
              }

## Lists

I have created a list of all the menu items - menu_list. 
I then converted the stock dictionary values into a list so I can access them later.
I also converted the proce dictionary values into a list so I can access them later.
Lastly I made a item_stock_list so I can save the new values after each iteration (stock x price)

    menu_list  = ["Tea", "Coffee", "Hot Chocolate", "Water", "Croissant", "Pan au Chocolat"]

    stock_dict_values = list(stock_dict.values())
    price_dict_values = list(price_dict.values())

    item_stock_list = []

## Iteration

Iterate through the number of items in the menu list.
Work out the total stock for each item (stock  x price).
Then print each individual item total stock in an easy to read format. 
Add this value to the item stock list I made earlier. 

    for i in range(len(menu_list)):
        item_stock = (stock_dict_values[i]) * (price_dict_values[i])
        print(f"{menu_list[i]} stock is £{item_stock}")
        item_stock_list.append(item_stock)

    print( )
    print(f"The total stock = £{sum(item_stock_list)}")

Lastly I get the total for all stock by adding all the values in the item_stock_list.
Printing out this total in a clear and coherent manner. 


Thanks for checking this out, as always you can run the code and try it for yourself.
