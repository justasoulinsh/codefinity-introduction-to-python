grocery_items = "milk cheese bread apples oranges chicken"


dairy1 = grocery_items[0:4]
#it is 0:4 because of the way it is indexed. It is indexed as 3 but due to the n- rule, it is actually 4.

dairy2 = grocery_items[5:11]
#it is 5:11 because of the way it is indexed. It is indexed as 10 but due to the n- rule, it is actually 11.

bakery1 = grocery_items[12:17]
#it is 12:17 because of the way it is indexed. It is indexed as 16 but due to the n- rule, it is actually 17.

print(f"We have dairy and bakery items: {dairy1}, {dairy2}, and {bakery1} in alise 5")

print("We have dairy and bakery items:", dairy1+", "+dairy2+", "+"and"+ " "+bakery1+" "+"in alise 5")