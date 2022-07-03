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

def addToInventory(inventory, addedItems): # Function to add items to an already created inventory.
    # NOTE: Eventually will need to update the character inventory file
    if type(addedItems) == list:
        for i in range(len(addedItems)):
            if addedItems[i] not in inventory.keys():
                inventory.setdefault(addedItems[i], 1)
            else:
                inventory[addedItems[i]] = inventory[addedItems[i]] + 1
    else:
        if addedItems not in inventory.keys():
            inventory.setdefault(addedItems, 1)
        else:
            inventory[addedItems] = inventory[addedItems] + 1

testList = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(stuff, testList)
print(stuff)
testValue = 'gold coin'
addToInventory(stuff, testValue)
print(stuff)
#f = open(r'inventories/test.txt', 'a+')
#print('Enter Something')
#something = input()
#f.write(something)
#print(f.read())
#f.close()
