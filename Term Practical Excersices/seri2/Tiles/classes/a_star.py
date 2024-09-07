from data_structures.p_queue import PriorityQueue
from icecream import ic

class A_star:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal: list[list] = goal
        self.frontier:PriorityQueue = PriorityQueue()
        self.explored_set: set = set()
        
    def run(self):
        self.initial.heuristic(goal_state=self.goal)
        self.frontier.push(item=self.initial, priority=(self.initial.f))
        while not self.frontier.isEmpty():
            state = self.frontier.pop()
            state_str = state.generate_string_version()
            if state_str in self.explored_set:
                continue
            
            self.explored_set.add(state_str)
            if state.check_goal(self.goal):
                ic(f"Found with {state.g} moves")
                self.print_result(state=state)
                return
            
            state.generate_next_states()
            self.add_to_frontier(list_of_next_states=state.next_states)
            
        ic(f"not Found with {state.g} moves")
        
        
    
    def add_to_frontier(self, list_of_next_states):
        for state in list_of_next_states:
            state.heuristic(self.goal)
            self.frontier.push(item=state, priority=(state.f))
            
    def print_result(self, state):
        while state:
            print(f"we reach this with move {state.move_that_created}")
            ic(state.board)
            state = state.parent