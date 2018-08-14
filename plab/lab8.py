catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] # list concatenation
# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')