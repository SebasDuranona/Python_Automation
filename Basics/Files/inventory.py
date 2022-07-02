# This program allows the user to create an inventory for a Fantasy Game. The inventory is saved in
# a txt file and can be retrieved.
from os import system
from os.path import exists

def createInventory(name): # Function to create the inventory
    file_exists = exists(r'inventories/' + name + '.txt')
    if file_exists:
        print ('This champion already has an inventory')
    else:
        print ('Welcome, new champion!')
        f = open(r'inventories/' + name + '.txt', 'a+')
        f.close()


stuff = {}

print ('How many items do you want to add?')
itemNum = int(input())
for i in range (itemNum):
    print('Item number ' + str(i+1) + ': ')
    item = input()
    print('How many ' + item + '?')
    itemQuant = int(input())
    stuff.setdefault(item, itemQuant)
print('Here is your inventory: ')
for k, v in stuff.items():
    print(str(v) + ' ' + k)
print('Number of items: ' + str(itemNum))

#f = open(r'inventories/test.txt', 'a+')
#print('Enter Something')
#something = input()
#f.write(something)
#print(f.read())
#f.close()
