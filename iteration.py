for i in range(len(menu_list)):
    item_stock = (stock_dict_values[i]) * (price_dict_values[i])
    print(f"{menu_list[i]} stock is £{item_stock}")
    item_stock_list.append(item_stock)

print( )
print(f"The total stock = £{sum(item_stock_list)}")