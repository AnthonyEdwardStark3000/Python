picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

def showTree():
    for outer in picture:
        for inner in outer:
            if inner :
                print("*", end='')
            else:
                print(" ", end='')
        print()      
showTree()          
showTree()          