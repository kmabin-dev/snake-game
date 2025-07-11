#Kaylynn S. Mabin
#Outcome: User interactive Snake Game
"""                                             In summary
This code is made up of two distinct classes. The first is the Node class. This class stores individual
pieces of data (called values in this instance) and a pointer that connects each node to the next, like a chain link.

The second is the Linkedlist class, which acts as the main data structure. This class contains several custom functions
(or methods) that define how the list behaves, such as adding new nodes, printing values, or navigating through the
chain. Throughout these methods, we use control structures like if statements, and while loops to handle the logic for
checking conditions and repeating actions as needed.

The linkedlist class is designed to simulate the body of a snake within a simple grid-based game environment.
Each part of the snakes body ("0") is represented by a node, which simultaneously stores a pair of (x,y) coordinates
that tell us where on the grid that body segment is located. These nodes are connected using a list structure,
with the HEAD of the list representing the snake's head.

The Node class starts with a constructor (__init__) that sets up the list and defines the size of the game grid.

The add_node() method adds a new segment to the end of the snake.

The insert_at_position() method allows us to place a new segment at a specific spot on the list. This is used to insert
a new head when the snake moves.

The delete_tail() method removes the last segment of the snake, which helps simulate movement without growing the body.

The move_snake(direction) method reads user input ('w','a','s','d') and uses a direction map to calculate the new
position of the head. It inserts the new head at the start of the list and deletes the tail. This gives the appearance
the snake is actually moving.

The print_grid() method draws a visual representation of the game board in the terminal. It prints dots (.) for empty
spaces and uses "0" to show the current position of the snake.

Together these two classes create a system that allows us to store, link and manage data efficiently using a linked list
to simulate a basic game."""


class Node:
    def __init__(self, value):
        """Create a new node"""
        self.value = value #The node
        self.next = None #The pointer for the node and what it's pointing to;
"""This block of code defines a custom class called Node.
Inside the class we create a constructor which will run automatically whenever we create a new node. 
The constructor sets two things. 1. The value of the node(number,or piece of data). 2. A pointer called "next" which
starts off empty "NONE". This pointer is how the node will eventually connect to another node. Placing this function 
inside a class helps us to keep everything organized and reusable."""

class Linkedlist:
    def __init__(self, rows=10, cols=10):
        """Set up the first node in the list"""
        self.head = None #Create a variable to keep track of the first node in the list; zero nodes in list right now
        self.rows = rows #Define the dimensions for the rows created later
        self.cols = cols #Define the dimensions for the columns created later
    """This block of code sets up the Linkedlist class.
    The constructor initializes three key variables:
    - self.head, which will keep track of the first node in the list.
    - self.rows and self.cols, which define the dimensions for a grid we'll use later to visualize the linked list
    As we add nodes, HEAD will point to the first one, and each node will link to the next, thus, 
    forming a chain-link structure. This is what gives Linkedlist its name and behavior. """

    def add_node(self, value):
        """Insert new node into linkedlist"""
        new_node = Node(value) #Allow for creation of new node based on node class/node object input.

        if self.head is None: #Conditional test; if the head isn't pointing to anything
            self.head = new_node #Conditional test; set it to the value given for the new node.
            return

        current = self.head #Where the pointer is now
        while current.next: #As long as the current node has a next pointer
            current = current.next #Move on to the next node, but once we find the last node
        current.next = new_node #Attach our new node to it

    """This function adds a new node to the end of the linked list.
    It starts by accepting two inputs: 
    - self, which represents the list itself
    - value, which is the data we want to store in the new node
    
    Then, we create a new node using the Node class and passing in the value. 
    This gives us a node object that stores the data and is ready to be connected to the list.
    
    Next, we use an if statement to check if the list is empty. We do this by testing ig self.head is NONE. if it is,
    that means the list doesn't means the list doesn't have a starting point yet. So we set self.head to the new node,
    making it the first item in the list. At that point, we return and stop the function, since the new node is
    already added.

    if the list already has at least one node, we need to find the last node in the chain so we can attach our new node
    to the end.
    
    To do this, we start at the head and use a while loop to move through each node. The loop continues as long as the
    current node has a .NEXT value, which means there's another node after it. Once we reach the last node(the one where
    .NEXT is NONE), we attach the new node to it by setting CURRENT.NEXT = NEW_NODE. """

    def insert_at_position(self, index, value):
        """Insert node at specific position"""
        new_node = Node(value) #Create a new node to store the given value

        #Conditional test; if the desired index position is 0
        #Conditional test; the new node should go at the start
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head #Helps the loop continue
        count = 0 #Keeps track of how many steps we've taken

        while current and count < index - 1: #Moves through the loop until we reach the position right before where we want to insert.
            current = current.next
            count += 1
        if not current: #Conditional test; if we run out of nodes before reaching the desired position //exception handling
            print("Index out of bounds") #Conditional test; the given index is too big for the list //exception handling
            return
        new_node.next = current.next #Points to whatever comes after current
        current.next = new_node #Re-link with the new node inserted
        """This block of code uses a custom function to insert a node at a specific position in the linked list.
        First, it creates a new node with the given value. If the position index is 0, that means we're inserting at
        the beginning. The new node becomes of the new head of the list, and we update its pointer to connext to the
        old head."""

    def delete_tail(self):
        """Remove last node from the list (Delete tail)"""
        if not self.head or not self.head.next: #Conditional test; if the list is empty //exception handling
            self.head = None #Conditional test; don't delete anything //exception handling
            return
        current = self.head
        while current.next.next: #Continue through the list as long as the node after the current still has another after
            current = current.next
        current.next = None #Cut-off the last node; its "empty"
        """This custom defined function removes the last node(the tail) from the linked list.
        First, it checks if the list is either empty or only has one node. If either case is true, there's nothing to 
        'trail behind' anymore, so we set the head to NONE and return. If the list has more than one node, we start at
        the head and move through the list until we find the second-to-last-node. Once we reach it, we set its .NEXT 
        pointer to NONE, which disconnects the last node from the list. We use this deletion to simulate motion in the 
        Snake game: as a new head is added to the front, we remove the tail to make it look like the snake is
        moving forward. """

    def move_snake(self,direction):
        """Set up logic for matching user input with linked list"""
        direction_map = {
            'w' : (0, -1), #(up) Move the snake up
            's' : (0, 1), #(down) Move the snake down
            'a' : (-1, 0), #(left) Move the snake left
            'd' : (1, 0) #(right) Move the snake right
        }
        if direction not in direction_map: #Conditional test; if input given != accepted values
            print("Invalid direction. ") #Conditional test; tell the user their input is invalid
            return
        dx, dy = direction_map[direction] #Connect direction values with row/column position
        head_x, head_y = self.head.value
        new_x, new_y = head_x + dx, head_y + dy

        #Bounds check
        if not (0 <= new_x < self.cols and 0 <= new_y < self.rows): #Conditional test; if direction goes beyond grid scope
            print("Move out of bounds!") #Conditional test; Tell the user they hit a wall or something
            return

        self.insert_at_position(0, (new_x, new_y))
        self.delete_tail()

        """This function defines how the snake moves based on user input, connecting keyboard commands to motion across
        the grid using the linked list. First a dictionary is created called direction_map, where each key ('w', 's', 
        'a', 'd') represents a direction: 
   
        Each direction is mapped to a tuple representing how it changes the snake's position on the grid
        either its row(y) or column(x) index.
        
        Next, the function checks if the input is valid (i.e exists in direction_map) if not, it prints an error and stops.
        
        If the input is valid, we:
        1. Get the change in position (dx, dy)"
        2. Get the current head's coordinates
        3. Calculate the new head's position
        
        Then, we run a bounds check to make sure the new position doesn't go off the grid. if the new position is outside
        the allowed range, we stop the move and display an error. 
        
        Finally if the move is valid:
        1. We insert the new position at the start of the list using insert_at_position(0,...), making it the new head."
        2. We remove the tail with delete_tail() to stimulate movement, so the snake appears to glide forward rather 
        than grow indefinetly.
        """

    def print_grid(self):
        """Create the Environment For The Snake to Move in"""
        grid = [[' . ' for _ in range(self.cols)] for _ in range(self.rows)] #Draw the grid
        current = self.head
        while current: #While the pointer loops through the list, update the snake too
            x, y = current.value
            grid[y][x] = '0'
            current = current.next
        for row in grid:
            print(''.join(row)) #Combine each element of a row into a single string for clean display


            """This function prints a visual representation of the grid to show where the snake currently is. 
            It starts by creating a 2D list called grid, filled with dots('-') to represent empty spaces. The number of 
            rows and columns is based on the values stored in self.rows and self.cols.
            
            Next, it uses a while loop to go through every node in the linked list. Each node contains a pair of
            coordinates that represent the snakes body segments. As it loops through each node, it updates the 
            corresponding spot in the grid to '0', which visually makes the snake position.
            
            After that, it uses a for loop to print each row of the grid. The ''.join(row) part combines each element
            of a row into a single string so the grid displays cleanly in the console.
            
            Overall, this function makes the snake's movement visible by showing its updated position on the grid each 
            time it's called."""

    def accept_direction(self):
        """Accept input and match it to a directional action"""
        print("Control the snake with: (w) up, (s) down, (a) left, (d) right")
        while True:
            self.print_grid()
            direction = input("Control the snake with: (w) up, (s) down, (a) left, (d) right\n Enter direction: "
                              " ").lower()
            if direction == 'n':
                print("Game Over!")
                break
            self.move_snake(direction)

    """This block of code creates a function to take in user input and then uses an if statement to run a conditional
    check. If the input matches the stored values of acceptable input for movement then the node
    moves to the aligned position. """

#Call an instance of the linked list
my_list = Linkedlist(rows=10, cols=10)
my_list.add_node((5,5)) #start position
my_list.accept_direction()


