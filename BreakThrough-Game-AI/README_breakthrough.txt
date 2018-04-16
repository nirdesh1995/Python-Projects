
To run our program simply use the following command: 
$python3 main.py

This runs the program for Colletive_utility vs Evasive AI by default and displays the board state after each move along with whose turn it is. When the game ends, it displays the winner and prints the number of pieces remaining for O,X and the number of moves made by each player. 

The list of helper functions for the class ‘Board’ and their functionalities are listed below:
Board class methods
  
__init__ : initializes the board and takes in arguments no of rows, no of columns and no of rows with pieces. 
display_state: Prints the current board state. 
initial_state: Creates a new board in the initial state and takes in arguments no of rows, no of columns and no of rows with pieces. 
possible_moves: Takes in a piece and returns a list of all possible coordinates the piece can move to. 
move_generator: Takes in the player and generates a list of all possible moves for each piece that the player has remaining on the board.
move: Takes in initial position, destination position and moves the piece accordingly. 
terminal_test : If the game has ended, returns the winner or else returns False. 


The following are our utility functions:
collective_utility(board, player): This function takes the current board state and the player’s turn and returns the utility of the board state.

avg_dist_utility(board, player):This function takes the current board state and the player’s turn and returns the utility of the board state.

conqueror_utility(board, player):This function takes the current board state and the player’s turn and returns the utility of the board state.

evasive_utility(board, player):This function takes the current board state and the player’s turn and returns the utility of the board state.

The list of helper functions for the class ‘Node’ and their functionalities are listed below:
Node class methods

__init__(self, parent=None, state=None, utility=None, action = None): This is the constructor that creates a node in a tree with the parameters given in the method definition. 

createTree(depth, board, heuristic): Creates the tree and returns the root node.
 
recursiveTree(depth, node, root_turn, heuristic, debug=False): A helper function of createTree that generates a tree and calculates the utilities of the leaf nodes. This method also implements the minMax algorithm and updates the utility based of the leaf node of all the child nodes except the root Node. 

minMax(depth, board, heuristic): This function implements the minMax algorithm at a higher level and is responsible for creating the tree and returning the optimal move.

******
 
play_game(heuristic_O, heuristic_X, board): this function takes two heuristic for player X and O and simulates the game. 

This is the main function required to play the game. 
An example of using this function is listed below: 
    n = board()
    n.initial_state(8, 8, 2)
    print('Starting Board: ')
    n.display_state()
    play_game(collective_utility,conqueror_utility, n)

********

....................................................................................
