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

# declaring bot
class bot:  
    def __init__(self, x, y, botDir, fovList = = [[0 for x in range(2)] for y in range(3)]):
        self.x = x;
        self.y = y;
        self.dir = botDir;
        self.fov = fovList;

    def direction(self):
        return self.botDir;

    def fov(self):
        #botDir = 1 implies facing upwards, with each +1 rotating 90deg clockwise
        if botDir == 1:
            self.fovList = [[self.x, self.y+1], [self.x-1, self.y+1], [self.x+1][self.y+1]]

        elif botDir == 2:
            self.fovList = [[self.x+1, self.y+1], [self.x+1, self.y-1], [self.x+1][self.y]]
            
        elif botDir == 3:
            self.fovList = [[self.x+1, self.y-1], [self.x-1, self.y-1], [self.x][self.y-1]]
            
        elif botDir == 4:
            self.fovList = [[self.x-1, self.y+1], [self.x-1, self.y-1], [self.x-1][self.y]]

        return self.fovList;
