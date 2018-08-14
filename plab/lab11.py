db = {
}
point = []
while True:
    temp = db
    for item in point:
        temp = temp[item]
    print(temp.keys())
    choice = input("Enter a choice, 1: insert 2:View 3:Quit 4:Back")
    if choice=="1":
        k=input("Enter a point")
        if k in temp:
            print("Item exist")
        else:
            temp[k]