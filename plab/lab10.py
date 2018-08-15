dic = {
    '植物':
        {'草本植物':
             ['牵牛花', '瓜叶菊', '葫芦', '翠菊', '冬小麦', '甜菜'],
         '木本植物':
             ['乔木', '灌木', '半灌木', '如松', '杉', '樟'],
         '水生植物':
             ['荷花', '千屈菜', '菖蒲', '黄菖蒲', '水葱', '再力花', '梭鱼草']},
    '动物':
        {'两栖动物':
             ['山龟', '山鳖', '石蛙', '娃娃鱼', '蟾蜍', '龟', '鳄鱼', '蜥蜴', '蛇'],
         '禽类':
             ['稚鸡', '原鸡', '长鸣鸡', '昌国鸡', '斗鸡', '长尾鸡', '乌骨鸡'],
         '哺乳类动物':
             ['虎', '狼', '鼠', '鹿', '貂', '猴', '貘', '树懒', '斑马', '狗']}}

li = []
li2 = []
go = True
while go:
    for i, v in enumerate(dic, 1):
        print(i, v)
        li.append(v)
    u_c = input("i,b,q")  # 1
    if u_c.isdigit():
        u_c = int(u_c)
        while go:
            for i, v in enumerate(dic[li[u_c - 1]], 1):
                print(i, v)
                li2.append(v)
            u_c2 = input(">>>>")  # 2
            if u_c2.isdigit():
                u_c2 = int(u_c2)
                while go:
                    for v in enumerate(dic[li[u_c - 1]][li2[u_c2 - 1]]):
                        print(v)
                    u_c3 = str(input(">>>>>>"))  # b for back q for quit
                    u_c3 = u_c3.lower()
                    if u_c3 == "b":
                        li2.clear()
                        break
                    elif u_c3 == "q":
                        go = False
                        break
            elif u_c2.isalpha():
                u_c2 = u_c2.lower()
                if u_c2 == "q":
                    li.clear()
                    break
    elif u_c.isalpha():
        u_c = u_c.lower()
        if u_c == "i":
            fl = input("Enter the type")
            if dic.get(fl, 1) == 1:
                dic[fl] = {}
            f2 = input("Enter the detail type")
            if dic[fl].get(f2, 1) == 1:
                dic[fl][f2] = []
            while True:
                f3 = input("enter the name")
                f3 = f3.lower()
                if f3 == "q":
                    li.clear()
                    break
                if f3 in dic[fl][f2]:
                    print("exist")
                else:
                    dic[fl][f2].append(f3)
