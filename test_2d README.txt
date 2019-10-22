-----------README for 'test_2d.py'----------- Version 1.3

-----------1. Introduction-----------

test_2d.py aims to simulate two robots navigating through a
field of W x H (default 20 x 20) with 2 types of objects placed
randomly inside it - object '1' and object '2'. The two robots
are displayed as 'A' and 'B' on the board.

-----------2. Implementation-----------

# random coordinate generation
Generates 2 x [up to 5] (i,j) pairs to be appended into lists
listAX, listAY, listBX and listBY, where Ax and Bx denote
object types '1' and '2'.

Generation is done with a priority for object type '1' - random
coordinates are appended to listBx only if they do not exist in
listAx. Since only 5 generations are executed regardless of
whether they are appended to the list or not, there is a bias
towards placing more object type '1's on the board.

# <bot> class
The bot class currently has 4 data variables.

1. self.x - X coordinate
2. self.y - Y coordinate
3. self.dir - direction
4. self.fov - list of coordinates inside FOV

Various utility methods are provided, including movement and FOV
scanning methods.

{MORE TO COME IN V1.4}

-----------3. Output-----------

# printing initial field
This prints the field with only the null spaces and objects.

# initial bot coordinate print
and
# initial board print
These print the first edge case of the board - after the bots are
placed on the board.

# printing loop
Iterative print of the board with bot movement. Currently has a ~200ms
time delay between prints for usability - can be modified at:
# refresh rate.