db = {}
point = []
while True:
    temp = db
    for item in point:
        temp = temp[item]
    print(list(temp.keys()))
    choice = input("Enter a choice, 1: insert 2:View 3:Quit 4:Back")
    if choice == "1":
        k = input("Enter a point")
        if temp.get(k, 1) == 1:
            temp[k] = {}
        r = input("Enter a detail point")
        if temp[k].get[r, 1] == 1:
            temp[k][r] = []
        s = input("Enter a name")
        if s in temp[k][r]:
            print("exist")
        else:
            temp[k][r].append()

    elif choice == "2":
        k = input("Enter a point")
        if k in temp:
            print(list(temp.keys()))
        else:
            point.append(k)
