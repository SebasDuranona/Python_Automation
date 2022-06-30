# Comma Code
# Write a function that takes a list value as an argument
# and returns a string with all the items separated by a
# comma and a space, with and inserted before the last item.

def commaCode (list):
    result = ''
    try:
        for i in range(len(list)-1):
            result += str(list[i])
            result += ', '
        result += 'and ' + str(list[len(list)-1])
    except IndexError:
        result = 'List was empty'
    return result


#Test
test = commaCode([1, 2, 3, 4])
test2 = commaCode(['apples', 'bananas', 'tofu', 'cats'])
test3 = commaCode([])
test4 = commaCode([1, True, 'bob'])
test5 = commaCode([])

print(test)
print(test2)
print(test3)
print(test4)
print(test5)
