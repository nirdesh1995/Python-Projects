from random import uniform as tiebreaker
from copy import deepcopy
import time


"""-------------------------------------------------------------------------
************************** Invalid Move Exception **************************
-------------------------------------------------------------------------"""
class InvalidMove(Exception):
    pass

"""-------------------------------------------------------------------------
************************ Board-State Not Exception *************************
-------------------------------------------------------------------------"""
class StateNotIntialized(Exception):
    pass

"""-------------------------------------------------------------------------
************************ Not a Pawn *************************
-------------------------------------------------------------------------"""
class NotPawn(Exception):
    pass

"""-------------------------------------------------------------------------
************************ Not a Player *************************
-------------------------------------------------------------------------"""
class InvalidPlayer(Exception):
    pass

"""-------------------------------------------------------------------------
************************ Not a Player *************************
-------------------------------------------------------------------------"""
class InvalidTurn(Exception):
    pass

"""-------------------------------------------------------------------------
**************************Object to create a board**************************
-------------------------------------------------------------------------"""

class board:

    # Constructor of object board
    def __init__(self, row = None, col = None, num_row_pieces = None):
        self.state = []
        self.turn = 'O'
        self.X = []
        self.O = []
        if row and col and num_row_pieces:
            self.initial_state(row, col, num_row_pieces)

    # Method to display the state in a tabular format
    def display_state(self):

        # if the board state has not been initialzed, raise error
        if self.state == []:
            raise StateNotIntialized("State not initialized")

        # else print the state
        for line in self.state:
            print(''.join(line))

    # Initialize the state of the board
    def initial_state(self, row, col, num_row_pieces):

        for i in range(row):
            if i < num_row_pieces:
                column = ['X'] * col
                self.state.append(column)

            elif i >= row - num_row_pieces:
                column = ['O'] * col
                self.state.append(column)

            else:
                column = ['.'] * col
                self.state.append(column)

        self.X_num = num_row_pieces * col
        self.O_num = num_row_pieces * col

        for i in range(num_row_pieces):
            k = row - i - 1
            for j in range(col):
                self.X.append((j,i))
                self.O.append((j,k))

        return self.state

    # possible moves for a pawn
    def possible_moves(self, pawn):    #returns list of touples with possbile moves for a piece.
        x = pawn[0]  # y = rows
        y = pawn[1]  # x = no of columns

        if self.state[y][x] != 'X' and self.state[y][x] != 'O':
            raise NotPawn("Not a Pawn.")

        possible = []

        if self.state[y][x] == 'X':
            player = 'X'
            opponent = 'O'
            front = (x,y+1)
            left = (x-1,y+1)
            right= (x+1,y+1)
        elif self.state[y][x] == 'O':
            player = 'O'
            opponent = 'X'
            front = (x,y-1)
            left  = (x-1,y-1)
            right = (x+1,y-1)

        if player == 'O' and y != 0:
            if (self.state[front[1]][front[0]] == '.'):
                possible.append(front)

            if x != 0:    #if discovered as corner, don't bother to compare. # left corner
                if self.state[left[1]][left[0]] != player:
                    possible.append(left)

            if x != (len(self.state[0])-1):    # right corner
                if self.state[right[1]][right[0]] != player:
                    possible.append(right)

        if player =='X' and y != (len(self.state) - 1):
            if (self.state[front[1]][front[0]] == '.'):
                possible.append(front)

            if x != 0:    #if discovered as corner, don't bother to compare. # left corner
                if self.state[left[1]][left[0]] != player:
                    possible.append(left)

            if x != (len(self.state[0])-1) :    # right corner
                if self.state[right[1]][right[0]] != player:
                    possible.append(right)



        return possible

    # Method to return all possible moves for a player
    def move_generator(self, player):
        list_of_moves = []
        if player == "O":
            for pawn in self.O:
                possible_moves = self.possible_moves(pawn)
                if possible_moves:
                    list_of_moves.append((pawn,possible_moves))

        elif player == "X":
            for pawn in self.X:
                possible_moves = self.possible_moves(pawn)
                if possible_moves:
                    list_of_moves.append((pawn,possible_moves))

        else:
            raise InvalidPlayer("Not a Player.")

        return list_of_moves

    def move(self, initial, dest):
        if dest not in self.possible_moves(initial):
            raise InvalidMove("This move is invalid.")

        # Update state in board
        x_initial, y_initial = initial
        x_dest, y_dest = dest

        pawn = self.state[y_initial][x_initial]
        if self.turn != pawn:
            raise InvalidTurn("It is not your turn.")

        if pawn == 'O':
            if self.state[y_dest][x_dest] == 'X':
                self.X.remove((x_dest,y_dest))

            self.O.remove((x_initial,y_initial))
            self.O.append((x_dest,y_dest))

        elif pawn == 'X':
            if self.state[y_dest][x_dest] == 'O':
                self.O.remove((x_dest,y_dest))

            self.X.remove((x_initial,y_initial))
            self.X.append((x_dest,y_dest))

        self.state[y_initial][x_initial] = '.'
        self.state[y_dest][x_dest] = pawn
        self.turn = 'X' if self.turn == 'O' else 'O'

    # Method to check if goal state is achieved
    def terminal_test(self):
        if 'O' in self.state[0] or len(self.X) == 0:
            return 'O'
        if 'X' in self.state[-1] or len(self.O) == 0:
            return 'X'
        else:
            return False
        
"""-------------------------------------------------------------------------
**************************      utility fxns      **************************
-------------------------------------------------------------------------"""
def attacked(board, player, piece):
    att_num = 0
    x, y = piece
    up_down = 1 if player == 'X' else -1
    y_check = y + up_down
    
    opp = 'O' if player == 'X' else 'X'
    
    if not (y == 0 and player == 'O') and not ((y == len(board.state) - 1) and player == 'X'):
    
        if x != 0:
            if board.state[y_check][x - 1] == opp:
                att_num += 1
        if x != len(board.state[0]) - 1:
            if board.state[y_check][x + 1] == opp:
                att_num += 1
    return att_num

def protected(board, player, piece):
    p_x, p_y = piece
    up_down = -1 if player == 'X' else 1
    protect_num = 0
    
    # if not vertical boundary for O and X
    if not (p_y == 0 and player == 'X') and not ((p_y == len(board.state) - 1) and player == 'O'):
    
        # if not left col, check left
        if p_x != 0:
            # check left
            if board.state[p_y + up_down][p_x - 1] == player:
                protect_num += 1

        # if not right col, check right
        if p_x != len(board.state) - 1:
            # check right
            if board.state[p_y + up_down][p_x + 1] == player:
                protect_num += 1
    return protect_num

# takes a board, a player, and an opponent piece and uses y val
# to calculate how dangerous that piece is
def piece_danger(board, player, piece):
    _, y = piece
    if player == 'X':
        danger = len(board.state) - y
    else:
        danger = y
    return danger

def collective_utility(board, player):
    util = 0
    if player == 'X':
        
        last_row = len(board.state) - 1
        
        # if we're winning, that's perfect!
        if any([piece[1] == last_row for piece in board.X]):
            return float('inf')
        
        # if we're almost winning, add 50 to util
        almost_there = [p for p in board.X if p[1] == last_row - 1]
        if not any([attacked(board, player, p) for p in almost_there]):
            util += 50
            
        # Calculated the number of protected pieces
        for piece in board.X:
            util += protected(board, player, piece)
            util -= attacked(board, player, piece)
            
        for piece in board.O:
            util -= piece_danger(board, player, piece)
            
    else:
        last_row = 0
        
        # if we're winning, that's perfect!
        if any([piece[1] == last_row for piece in board.O]):
            return float('inf')
        
        # if we're almost winning, add 50 to util
        almost_there = [p for p in board.O if p[1] == last_row - 1]
        if not any([attacked(board, player, p) for p in almost_there]):
            util += 50
            
        # Calculated the number of attacked and protected pieces
        for piece in board.O:
            util += protected(board, player, piece)
            util -= attacked(board, player, piece)
        
        # Calculate the danger of each opponents piece
        for piece in board.X:
            util -= 3 * piece_danger(board, player, piece)
    return util

def avg_dist_utility(board, player):
    y = len(board.state) - 1
    o_ys = [(y - piece[1] + 100) ** 2 for piece in board.O]  #avg distance
    x_ys = [(piece[1] + 100) ** 2 for piece in board.X]
    
    if any([py == 0 for py in o_ys]) and player == 'O':   #check if any piece is very close to winning 
        return float('inf')
    if any([py == y for py in x_ys]) and player == 'X':
        return float('inf')
    
    o_y_avg = float(sum(o_ys)) / max(len(o_ys), 1)    #sum of avg, 
    x_y_avg = float(sum(x_ys)) / max(len(x_ys), 1)
    
    
    
    util = (o_y_avg - x_y_avg) if player == 'O' else (x_y_avg - o_y_avg)
    
    # Calculate the danger of each opponents piece
    for piece in board.X:
        util -= 3 * piece_danger(board, player, piece)
        
    # Calculated the number of attacked and protected pieces
    pieces = board.O if player == 'O' else board.X
    for piece in pieces:
        util += protected(board, player, piece)
        util -= attacked(board, player, piece)
    return util

def evasive_utility(board, player):
    utility = len(board.O) if player == 'O' else len(board.X)
    return utility + tiebreaker(0, 1)

def conqueror_utility(board, player):
    utility = 0 - (len(board.X) if player == 'O' else len(board.O))
    return utility + tiebreaker(0, 1)

"""-------------------------------------------------------------------------
*************************Object to create the tree**************************
-------------------------------------------------------------------------"""

class Node(object):
    def __init__(self, parent=None, state=None, utility=None, action = None):
        self.parent = parent
        self.child = []
        self.action = action
        self.state = state
        self.utility = utility

def createTree(depth, board, heuristic):
    root = Node(state = board)
    recursiveTree(depth, root, board.turn, heuristic)
    return root

def recursiveTree(depth, node, root_turn, heuristic, debug=False):
    board = node.state
    if debug:
        print()
        board.display_state()

    if depth == 0 or board.terminal_test():
        turn = 'X' if board.turn == 'O' else 'O'
        node.utility = heuristic(board, turn)
        if debug:
            print("node utility:", node.utility)
        return node.utility

    moves = board.move_generator(board.turn)
    for m in moves:
        piece = m[0]
        children = m[1]
        for c in children:
            c_board = deepcopy(board)
            c_board.move(piece, c)
            c_node = Node(parent = node, state = c_board, action = (piece, c))
            node.child.append(c_node)

    for c in node.child:
        #print("C----"+str(c.action))
        c_utility = recursiveTree(depth - 1, c, root_turn, heuristic)

        # if utility is not None
        if node.utility:

            # Check against the root turn
            if board.turn != root_turn:

                # maximize utility
                if c_utility > node.utility: node.utility = c_utility

            else:
                # minimize
                if c_utility < node.utility: node.utility = c_utility
        else:
            node.utility = c_utility

    return node.utility

def minMax(depth, board, heuristic):
    root = createTree(depth, board, heuristic)
    #max_child = sorted(root.child, key=lambda x: x.utility, reverse=True)[0]
    #return max_child.action
    max_utility_child = None
    for c in root.child:
        if max_utility_child:
            if max_utility_child.utility < c.utility:
                max_utility_child = c
        else:
            max_utility_child = c
    return max_utility_child.action

"""-------------------------------------------------------------------------
*********************** Functions to actually run it ***********************
-------------------------------------------------------------------------"""

def play_game(heuristic_O, heuristic_X, board):
    depth = 3
    O_move = X_move = 0
    while not board.terminal_test():
        if board.turn == 'O':
            move = minMax(depth, board, heuristic_O)
            O_move += 1
            print("\n--------")
            print("O moves =>")
        else:
            move = minMax(depth, board, heuristic_X)
            X_move += 1
            print("\n--------")
            print("X moves =>")

        board.move(move[0], move[1])
        print()
        board.display_state()

    if (O_move > X_move):
        print("\n****** O wins! ******")
    else:
        print("\n****** X wins! ******")

    print()
    print("The number of O pieces remaning: ", len(board.O))
    print("The number of X pieces remaning: ", len(board.X))
    print("The number of moves by O: ", O_move)
    print("The number of moves by X: ", X_move)

def heur_test(heuristic_O, heuristic_X, board, num_gm = 10):
    depth = 3
    O_w = X_w = 0
    iteration = 0
    total_time = 0
    for i in range(num_gm):
        t_board = deepcopy(board)
        while not t_board.terminal_test():
            iteration += 1
            start = time.time()
            if t_board.turn == 'O':
                move = minMax(depth, t_board, heuristic_O)
            else:
                move = minMax(depth, t_board, heuristic_X)
            runtime = time.time() - start
            total_time += runtime
            t_board.move(move[0], move[1])
        if t_board.terminal_test() == 'O':
            O_w += 1
        else:
            X_w += 1
    avg_time = total_time/iteration
    print("\tAvg time per move: ", avg_time)
    return O_w / num_gm, X_w / num_gm

if __name__ == '__main__':
    
    n = board()
    n.initial_state(5, 5, 2)
    print('Starting Board: ')
    n.display_state()
    play_game(conqueror_utility, avg_dist_utility, n) 
    
