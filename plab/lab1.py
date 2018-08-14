# s=" "
# v=s.join("abcdefghghgfhghjghjsdasdaksld")
# v=v.split("g")
# print(v)

# num = "5"
# v = int(num, base=10)
# r=v.bit_length()
# print(r)

# name=input()
# r=name.strip()
#
# print(r)

# li="alexericrain"
# r="_".join(li)
# print(r)


# r=0
# while True:
#     i = int(input("enter a number"))
#     if i!=0:
#         r+=i
#     print(r)

# content=input('请输入内容：')
# num=0
# alp=0
# i=0
# while i < len(content):
#     ar=content[i].isalnum()
#     r=content[i].isdecimal()
#     if ar:
#         if r:
#             num+=1
#             i+=1
#         else:
#             alp+=1
#             i+=1
#     else:
#         break
# print('number' + str(num))
# print('character' +str(alp))

# name=input("Enter your name")
# # location=input("Enter the location")
# # thing=input("what are you doing")
# #
# # print("Dear "+str(name)+" like "+str(thing)+" at the " +str(location))

# def check_code():
#     import random
#     checkcode=''
#     for i in range(4):
#         current=random.randrange(0,4)
#         # print('current'+str(current))
#         if current != i:
#             temp=chr(random.randint(65,90))
#             # print('temp1'+str(temp))
#         else:
#             temp=random.randint(0,9)
#             # print('temp2'+str(temp))
#         checkcode=str(temp)
#     return checkcode
# code=check_code()
# print(code)
#
# ui=input("enter the code")
# while check_code():
#     if ui==code:
#         print("success")
#         break
#     else:
#         print("fail")
#         break
#

# s=input("Enter the words")
# # s=s.replace("PK", "***")
# # s=s.replace("Die", "***")
# # print(s)

# v = ""
# while True:
#     a = input("Your name\n")
#     b = input("Your password\n")
#     c = input("your email address\n")
#     d = input("continue(Y/N)\n")
#     s = "{0}\t{1}\t{2}\n"
#     p = s.format(a, b, c)
#     v = v+p
#     if d == "N":
#         break
# print(v.expandtabs(20))

# content = input("content")
# a, b = content.split("+")
# a = int(a)
# b = int(b)
# v2 = a + b
#
# print(v2)

# content=input('请输入内容：')
# num=0
# alp=0
# for item in content:
#     p=item.isalpha()
#     t=item.isnumeric()
#     if p==True:
#         alp+=1
#     if t==True:
#         num+=1
# print('number' + str(num))
# print('character' +str(alp))

d = {

}
p = {}
for k, v in d.items():
    p.setdefault(k, []).append(v)
    print(v,k)