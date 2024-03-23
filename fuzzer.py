from puzzle_generator import *
from heuristics import *
from bbmodcache.bbSearch import SearchProblem, search

def default_herustic(state:BlockState):
    return 1

class fuzzer:
    small_fuzzer = small_puzzle_issue_generator()
    big_fuzzer = big_puzzle_issue_generator()
    hard_fuzzer = hard_puzzle_issue_generator()

    small_puzzle = None
    big_puzzle = None
    hard_puzzle = None
    def __generate__(self):
        self.small_puzzle = self.small_fuzzer.random_issue()
        self.big_puzzle = self.big_fuzzer.random_issue()
        self.hard_puzzle = self.hard_fuzzer.random_issue()

    def test_once(self, heuristic_=default_herustic):
            self.__generate__()
            self.small_search = search( self.small_puzzle , 'BF/FIFO', 10000000, heuristic = heuristic_,
                     loop_check=True, randomise=False, show_state_path=True, return_info=True)
            self.big_search = search( self.big_puzzle, 'BF/FIFO', 10000000, heuristic= heuristic_,
                     loop_check=True, randomise=False, show_state_path=True, return_info=True)
            self.hard_search = search( self.hard_puzzle, 'BF/FIFO', 10000000, heuristic= heuristic_,
                     loop_check=True, randomise=False, show_state_path=True, return_info=True)  


try:
    fuzzing = fuzzer()
    fuzzing.test_once(purple_heuristic)
except KeyboardInterrupt:
     print("")
     pritn("KeyboardInterrupt, exit.")