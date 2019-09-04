# imports
import random;

# declarations
w, h = 21, 21;
outString = "";
Matrix = [[0 for x in range(w)] for y in range(h)];
listAX = [];
listAY = [];
listBX = [];
listBY = [];
botX = 0;
botY = 0;
flag1 = 0;
flag2 = 0;

# random coordinate generation
for i in range(5):
    r = random.randint(1,20);
    if r not in listAX: listAX.append(r);
for j in range(5):
    r = random.randint(1,20)
    if r not in listAY: listAY.append(r);
        
for i in range(5):
    r = random.randint(1,20);
    if r not in listAX:
        if r not in listBX: listBX.append(r);
for j in range(5):
    r = random.randint(1,20);
    if r not in listAY:
        if r not in listBY: listBY.append(r);

# placing object type 1
for k in listAX:
    for l in listAY:
        Matrix[k][l] = 1;

# placing object type 2
for k in listBX:
    for l in listBY:
        Matrix[k][l] = 2;

# printing
for x in range(h):
    for y in range(w):
        outString += str(Matrix[x][y]);
    print(outString);
    outString = "";
