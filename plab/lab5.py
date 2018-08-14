# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
# def bacon():
#     ham = 101
#     eggs = 0
# spam()
# Global variable can be read from local scope
# def spam():
#     v1=eggs+10
#     print(v1)
# eggs = 42
# spam()
# print(eggs)

#same name of global scope and local scope, print local scope variable first
# def spam():
#     eggs = 'spam local'
#     print(eggs) # prints 'spam local'
# def bacon():
#     eggs = 'bacon local'
#     print(eggs) # prints 'bacon local'
#     spam()
#     print(eggs) # prints 'bacon local'
# eggs = 'global'
# bacon()
# print(eggs) # prints 'global'

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)