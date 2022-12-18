f=open("input.txt","r")
smallList=[]    # Small lists inside big list
bigList=[]
score=0


for line in f:                # Reading input and creating matrix
    line = line.strip()
    if line.endswith("\n"):
        line = line[:-1]
    for j in line.split(" "):
        smallList.append(j)
    bigList.append(smallList)
    smallList = []

for a in range(len(bigList)):  # Printing matrix and score firstly
    print(*bigList[a])
print("\nYour score is: 0\n")


list4 = [] # List to use inside checkaround function
list3 = [] # List to use inside checkaround function
def checkaround(k,l):    # Function for checking around the ball to see if there is the same colour
    try:
        list2 = [] # Checking the ball's up
        if bigList[k + 1][l] == bigList[k][l]:
            list2.append(k + 1)
            list2.append(l)
            if list2 not in list4:
                if list2[1]>=0 and list2[0]>=0:
                    list3.append(list2)
    except: # This except is for if there is an index error, i want to ignore it
        o=5
    try:
        list2=[] # Checking the ball's down
        if bigList[k - 1][l] == bigList[k][l]:
            list2.append(k - 1)
            list2.append(l)
            if list2 not in list4:
                if list2[1] >= 0 and list2[0] >= 0:
                    list3.append(list2)
    except: # This except is for if there is an index error, ı want to ignore it
        o=5
    try:
        list2 = [] # Checking the ball's right
        if bigList[k][l + 1] == bigList[k][l]:
            list2.append(k)
            list2.append(l + 1)
            if list2 not in list4:
                if list2[1] >= 0 and list2[0] >= 0:
                    list3.append(list2)
    except: # This except is for if there is an index error, ı want to ignore it
        o=5
    try:
        list2 = [] # Checking the ball's left
        if bigList[k][l - 1] == bigList[k][l]:
            list2.append(k)
            list2.append(l - 1)
            if list2 not in list4:
                if list2[1] >= 0 and list2[0] >= 0:
                    list3.append(list2)
    except: # This except is for if there is an index error, ı want to ignore it
        o=5

    for a in list3:
        if a not in list4:
            list4.append(a)
    try:
        for c in list3:
            k = c[0]
            l = c[1]
            list3.remove(c)
            checkaround(k, l)
    except:
        o=5



listofXs=[] # This is a list to collect activated bombs' coordinates
list10 = []
def bombfunction(k,l): # Function to see if there is an another activateed bomb when our bomb explode and taking activated bomb(s) coordinates
    for v in range(1):
        for j in range(len(bigList[k])): # I am checking here if there is an another bomb in the row
            if bigList[k][j]=="X":
                listforcoordinates=[k,j]
                if listforcoordinates not in listofXs:
                    listofXs.append(listforcoordinates)
                    l=j
                    bombfunction(k, l) # Recursion for if activated bomb activates another bomb

        for j in range(len(bigList)): # I am checking here if there is an another bomb in the column
            if bigList[j][l]=="X":
                listforcoordinates=[j,l]
                if listforcoordinates not in listofXs:
                    listofXs.append(listforcoordinates)
                    k = j
                    bombfunction(k, l) # Recursion for if activated bomb activates another bomb


iftrue=True
while iftrue==True:
    try:
        a = (input("Please enter a row and column number:")).split()  # Taking coordinates from user
        print(" ")
        list7=[]
        for b in a:
            list7.append(int(b))
        list4.append(list7)
        k = int(a[0])  # Row Coordinate
        l = int(a[1])  # Column Coordinate
        y=bigList[k][l]
        assert y!=" " # Checking for if there is a ball in that coordinates and if there is not program will want new input

        if y!="X": # If coordinates is not bomb, we will use these codes to check around of ball and change them with space
            list4=[]
            checkaround(k,l)
            for a in list4:
                m = a[0]
                n = a[1]
                bigList[m].pop(n)
                bigList[m].insert(n, ' ')
            for z in range(50): # If the ball's down is empty these codes is to drop it
                for a in range(len(bigList)):
                    for b in range(len(bigList[a])):
                        if bigList[a][b] == " ":
                            if bigList[a - 1][b] != " " and a - 1 >= 0:
                                bigList[a][b] = bigList[a - 1][b]
                                bigList[a - 1][b] = " "


        elif y=="X": # If there is a bomb in the coordinates we will use these codes
            list10=[]
            listofXs=[]
            bombfunction(k,l)
            listofXs.sort()
            listfordeleterow=[]
            listfordeleterow2=[]
            for a in listofXs:
                e= a[0]
                w= a[1]
                for b in range(len(bigList[e])):
                    list10.append(bigList[e][b])
                    bigList[e].pop(b)
                    bigList[e].insert(b, " ")
                for j in range(len(bigList)):
                    list10.append(bigList[j][w])
                    bigList[j].pop(w)
                    bigList[j].insert(w, " ")
            for a in listofXs:
                e=a[0]
                if e not in listfordeleterow:
                    listfordeleterow.append(e)
            for a in listfordeleterow:
                c=listfordeleterow.index(a)
                b=a-1*c
                listfordeleterow2.append(b)
            for i in listfordeleterow2:
                bigList.remove(bigList[i])

            for k in list10: # Scoring commands
                if k == "B":
                    score = score + 9
                elif k == "G":
                    score = score + 8
                elif k == "W":
                    score = score + 7
                elif k == "Y":
                    score = score + 6
                elif k == "R":
                    score = score + 5
                elif k == "P":
                    score = score + 4
                elif k == "O":
                    score = score + 3
                elif k == "D":
                    score = score + 2
                elif k == "F":
                    score = score + 1


        for q in range(10): # Codes to check if the column is empty and delete that column
            try:
                list9 = []
                for a in range(len(bigList[0])):
                    for j in range(len(bigList)):
                        list9.append(bigList[j][a])
                    if ("B" not in list9) and ("G" not in list9) and ("W" not in list9) and ("Y" not in list9) and (
                            "R" not in list9) and ("P" not in list9) and ("O" not in list9) and ("D" not in list9) and (
                            "F" not in list9) and ("X" not in list9):
                        for j in range(len(bigList)):
                            bigList[j].pop(a)
                            list9 = []

                    else:
                        list9 = []
            except IndexError:
                o=5


        # Check for if row is empty and delete that row
        for q in range(5):
            for a in bigList:
                if ("B" not in a) and ("G" not in a) and ("W" not in a) and ("Y" not in a) and ("R" not in a) and ("P" not in a) and ("O" not in a) and ("D" not in a) and ("F" not in a) and ("X" not in a):
                    bigList.remove(a)


        for a in range(len(bigList)): # Print codes
            print(*bigList[a])
        print(" ")

        # These codes for scoring
        list1 = []
        for a in list4:
            if a[0]<0 or a[1]<0:
                list1.append(a)
        for b in list1:
            list4.remove(b)
        n=len(list4)
        list4=[]
        if y=="B":
            score=score+n*9
        elif y=="G":
            score=score+n*8
        elif y=="W":
            score=score+n*7
        elif y=="Y":
            score=score+n*6
        elif y=="R":
            score=score+n*5
        elif y=="P":
            score=score+n*4
        elif y=="O":
            score=score+n*3
        elif y=="D":
            score=score+n*2
        elif y=="F":
            score=score+n*1
        else:
            score=score
        print("Your score is:",score)
        print(" ")

    except AssertionError:
        print("Please enter a valid size!\n")
        list4.remove(list7)
    except IndexError:
        print("Please enter a valid size!\n")
        list4.remove(list7)
    except ValueError:
        print("Please enter a valid size!\n")

# The codes below is for checking if there is no more bomb
# and there is no same ball around any ball and if there is not both the game will end
    list12 = []
    list13=[]
    for u in range(len(bigList)):
        for g in range(len(bigList[u])):
            if bigList[u][g]!=" ":
                list12.append(bigList[u][g])
                list4=[]
                if "X" not in list12:
                    checkaround(u,g)
                    if list4!=[]:
                        list13.append("b")
    if "b" not in list13 and "X" not in list12:
        print("Game Over.")
        iftrue=False