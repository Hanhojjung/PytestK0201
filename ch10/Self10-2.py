import numpy as np
SIZE = np.random.choice([8, 12, 16, 20])
newRow, newCol = int(SIZE/2), int(SIZE/2)
value = 1
myAry1 = np.arange(value, value+(SIZE*SIZE),1)
myAry1 = myAry1.reshape(SIZE,SIZE)

for i in range(SIZE) :
    [ print("%3d" %myAry1[i][k], end=' ') for k in range(SIZE)]
    print()
print()

myAry2 = myAry1[newRow:SIZE+1, newCol: SIZE+1].copy()

for i in range(newRow) :
    [print("%3d" % myAry2[i][k], end=' ') for k in range (newCol)]
    print()
print()
