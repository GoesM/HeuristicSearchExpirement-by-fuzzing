# fuzzing test
import random
from BockState import BlockState
from SlidingBlockPuzzle import SlidingBlocksPuzzle

class PuzzleMatrixGenerator:
    height = 0
    width = 0

    num  = 0
    left_num = 0

    maxn_size_ = 4

    initial_puzzle_matrix_ = [[]]
    goal_puzzle_matrix_ = [[]]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(0,0)]  # right,left,up,down,change
    
    def __init__(self, height, width, num,left_num=1,maxn_size=4):
        self.height = height
        self.width  = width
        self.num    = num
        self.left_num = left_num
        self.maxn_size_ = maxn_size
        # init matrixs
        self.__cleanup__()
        return 
    def __empty_matrix__(self):
        return [[0 for _ in range(self.width)] for _ in range(self.height)]
    def __cleanup__(self):
        self.initial_puzzle_matrix_ = self.__empty_matrix__()
        self.goal_puzzle_matrix_ = self.__empty_matrix__()
        return 

    # for initial_state
    def __random_empty_position__(self):
        empty_positions = [(i, j) for i in range(self.height) for j in range(self.width) if self.initial_puzzle_matrix_[i][j] == 0]
        if empty_positions:
            return random.choice(empty_positions)
        else:
            return None
    def __random_fill__(self, n):
        empty_position = self.__random_empty_position__()
        if empty_position!=None:
            i, j = empty_position
            self.initial_puzzle_matrix_[i][j] = n
            self.__expand_fill__(i, j, n, self.maxn_size_)
        else:
            print("No empty position to fill.")
    def __expand_fill__(self, i, j, n, expand_times_):
        if expand_times_ <= 0 :
            return
        direction = random.choice(self.directions)
        ni, nj = i + direction[0], j + direction[1]
        if 0 <= ni < self.height and 0 <= nj < self.width and self.initial_puzzle_matrix_[ni][nj] == 0:
            self.initial_puzzle_matrix_[ni][nj] = n
        expand_times_ -=1
        self.__expand_fill__(ni,nj,n,expand_times_)
        return 
    def __generate_initial_puzzle_matrix__(self):
        for i in range(self.num):
            color = i+1
            self.__random_fill__( color )
        return self.initial_puzzle_matrix_

    # for goal_state
    def __random_goal_position_fill__(self, color ):
        # Find boundaries of left_color_instance
        min_i, min_j, max_i, max_j = float('inf'), float('inf'), -float('inf'), -float('inf')
        for i in range(self.height):
            for j in range(self.width):
                if self.initial_puzzle_matrix_[i][j] == color:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)

        # Determine shape and size of left_color_instance
        shape = [[self.initial_puzzle_matrix_[i][j] if self.initial_puzzle_matrix_[i][j] == color else 0
                  for j in range(min_j, max_j + 1)] for i in range(min_i, max_i + 1)]

        # Randomly select a position for left_color_instance
        start_i = random.randint(0, self.height - len(shape))
        start_j = random.randint(0, self.width - len(shape[0]))

        # validation check     # Check if all positions in the range are empty
        valid_position = True
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] != 0 and self.goal_puzzle_matrix_[start_i + i][start_j + j] != 0:
                    valid_position = False
                    break
            if not valid_position:
                break
        
        if valid_position:
            pass
        else:
            return 

        # Place left_color_instance in goal puzzle matrix
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] != 0:
                    self.goal_puzzle_matrix_[start_i + i][start_j + j] = shape[i][j]

        return
    def __generate_goal_puzzle_matrix__(self):
        left_color = random.sample(range(1, self.num + 1), self.left_num)

        for color in left_color:
            self.__random_goal_position_fill__(color)

        return self.goal_puzzle_matrix_
        

    # API
    def generate_random_puzzle_issue(self):
        self.__cleanup__()
        self.__generate_initial_puzzle_matrix__()
        self.__generate_goal_puzzle_matrix__()
        return  SlidingBlocksPuzzle(self.initial_puzzle_matrix_, self.goal_puzzle_matrix_)
    def display(self):
        bs = BlockState( self.initial_puzzle_matrix_ )
        bs.display()
        bs = BlockState( self.goal_puzzle_matrix_ )
        bs.display()
        return 



class small_puzzle_issue_generator:
    G1 =  PuzzleMatrixGenerator(3,3,3,1,2)
    def random_issue(self):
        issue = self.G1.generate_random_puzzle_issue()
        self.G1.display()
        return issue
class big_puzzle_issue_generator:
    G1 =  PuzzleMatrixGenerator(5,7,6,1,3)
    def random_issue(self):
        issue = self.G1.generate_random_puzzle_issue()
        self.G1.display()
        return issue

class hard_puzzle_issue_generator:
    G1 = PuzzleMatrixGenerator(5,7,6,2,4)
    def random_issue(self):
        issue = self.G1.generate_random_puzzle_issue()
        self.G1.display()
        return issue


if __name__ == "__main__":
    aa = small_puzzle_issue_generator()
    aa.random_issue()
    bb = big_puzzle_issue_generator()
    bb.random_issue()
    cc = hard_puzzle_issue_generator()
    cc.random_issue()