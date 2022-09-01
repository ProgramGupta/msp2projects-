items = [
  ['Apple',0.75],
  ['Carrot',0.25],
  ['Bannana',2.0],
  ['Avacado',1.99],
  ['Dragonfruit',2.25],
  ['Lemon',0.25],
]

#what products they want
cart = []
total = 0
for item in items:
  do_you_want_to_buy = input(f'Would you like to buy a {item[0]} for ${item[1]}, yes or no : ')
  if (do_you_want_to_buy == "yes"):
      cart.append(item)
      total = total + item[1]
    
#print of current cart
print('This is your cart:')
for item in cart:
  print(item[0])

print("Your total is $", total)


#delete stuff from cart
items_to_delete = []

for item in cart:
  do_you_want_to_delete = input(f'Would you like to delete {item[0]} for ${item[1]}, yes or no : ')
  if (do_you_want_to_delete == "yes"):
    items_to_delete.append(item)

for item in items_to_delete:
  cart.remove(item) 
  total = total - item[1]

#print final cart 
print('This is your final cart:')
for item in cart:
  print (item[0])
print ("Your total is $",total)
