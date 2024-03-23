from BockState import BlockState

def purple_heuristic(state:BlockState):
      for r, row in enumerate(state.blockstate):
        for c, col in enumerate(row):
          if col == 6:
            return r+c
def red_and_purple_heuristic(state:BlockState):
  return (red_right_heuristic(state) + purple_heuristic(state))
def red_right_heuristic(state:BlockState):
    for row in state.blockstate:
      for i, col in enumerate(row):
          if col == 1:
            return 6-i