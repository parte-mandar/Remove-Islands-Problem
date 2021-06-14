inputList = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1]
]

from removeIslands import RemoveIslandClass

rm = RemoveIslandClass(inputList)

result = rm.returnResult()

for list in result:
    print(list)
