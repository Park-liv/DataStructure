shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase')

print('These items are:')
for item in shoplist:
    print(item)

print('\nI also have to buy rice')
shoplist.append('rice')
print('My shopping list is now',shoplist)

print('\nI will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)

print('\nThe first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

name = 'Park Youngmin'
print("character 1 to 3 is", name[1:3])
print("character 1 to 3 is", name[2:])
print("character 1 to 3 is", name[1:-1])
print("character 1 to 3 is", name[:])

print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])