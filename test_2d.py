# imports
import random;
from time import sleep

# declarations
w, h = 21, 21
outString = ""
Matrix = [[0 for x in range(w)] for y in range(h)]
listAX = []
listAY = []
listBX = []
listBY = []
botX = 0
botY = 0
flag1 = 0
flag2 = 0
complete = False

# random coordinate generation
for i in range(5):
    r = random.randint(1,20)
    if r not in listAX: listAX.append(r)
for j in range(5):
    r = random.randint(1,20)
    if r not in listAY: listAY.append(r)
        
for i in range(5):
    r = random.randint(1,20);
    if r not in listAX:
        if r not in listBX: listBX.append(r)
for j in range(5):
    r = random.randint(1,20)
    if r not in listAY:
        if r not in listBY: listBY.append(r)

# placing object type 1
for k in listAX:
    for l in listAY:
        Matrix[k][l] = 1

# placing object type 2
for k in listBX:
    for l in listBY:
        Matrix[k][l] = 2

# printing initial field
print("Initial Field:")
for x in range(h):
    for y in range(w):
        outString += str(Matrix[x][y])
    print(outString)
    outString = ""

# declaring bot
class bot:  
    def __init__(self, x, y, botDir, fovList = [[0 for x in range(2)] for y in range(3)]):
        self.x = x
        self.y = y
        self.dir = botDir
        self.fov = fovList

    def direction(self):
        return self.botDir;

    def fov(self):
        #botDir = 1 implies facing upwards, with each +1 rotating 90deg clockwise
        if self.dir == 1:
            self.fovList = [[self.x, self.y+1], [self.x-1, self.y+1], [self.x+1][self.y+1]]

        elif self.dir == 2:
            self.fovList = [[self.x+1, self.y+1], [self.x+1, self.y-1], [self.x+1][self.y]]
            
        elif self.dir == 3:
            self.fovList = [[self.x+1, self.y-1], [self.x-1, self.y-1], [self.x][self.y-1]]
            
        elif self.dir == 4:
            self.fovList = [[self.x-1, self.y+1], [self.x-1, self.y-1], [self.x-1][self.y]]

        return self.fovList

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def moveFwd(self):
        if self.dir == 1:
            self.y += 1

        elif self.dir == 2:
            self.x += 1
            
        elif self.dir == 3:
            self.y -= 1
            
        elif self.dir == 4:
            self.x -= 1
            
    def turnLeft(self):
        self.dir -= 1

    def turnRight(self):
        self.dir += 1

    def front(int):
        if self.dir == 1:
            return [self.x,self.y+1]

        elif self.dir == 2:
            return [self.x+1,self.y]
            
        elif self.dir == 3:
            return [self.x,self.y-1]
            
        elif self.dir == 4:
            return [self.x-1,self.y]

# bot initialization
bot1 = bot(0,0,1)
bot2 = bot(20,0,1)

# debug printing
print("Bot1 Y:", bot1.y, " Bot1 X:", bot1.x)
print("Bot2 Y:", bot2.y, " Bot2 X:", bot2.x)
#saving inital board values
last1 = Matrix[bot1.x][bot1.y]
last2 = Matrix[bot2.x][bot2.y]
Matrix[bot1.x][bot1.y] = 'A'
Matrix[bot2.x][bot2.y] = 'B'

# initial print
print("Bots Initialized Field:")
for x in range(h):
    for y in range(w):
        outString += str(Matrix[x][y])
    print(outString)
    outString = ""
print("\n\n")
sleep(0.2)

# reset board values
Matrix[bot1.x][bot1.y] = last1
Matrix[bot2.x][bot2.y] = last2

# printing loop
while not complete:
    while bot1.y < 21:        
        if bot1.y == 20:
            complete = True
            break

        # moving up condition tree
        if(Matrix[bot1.x][bot1.y+1] == 0):
            bot1.moveUp()
            Matrix[bot1.x][bot1.y-1] = last1
            last1 = Matrix[bot1.x][bot1.y]
            Matrix[bot1.x][bot1.y] = 'A'
            
        
        Matrix[bot2.x][bot2.y] = 'B'
        
        # printing bot coordinates
        print("Bot1 Y:", bot1.y, " Bot1 X:", bot1.x)
        print("Bot2 Y:", bot2.y, " Bot2 X:", bot2.x)
        
        # printing field with bots
        print("Looping:")
        for x in range(h):
            for y in range(w):
                outString += str(Matrix[x][y])
            print(outString)
            outString = ""
        print("\n")
        sleep(0.2)
