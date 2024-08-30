# from priority_queue import PriorityQueue
from icecream import ic
from classes.parking import Parking

import heapq
class PriorityQueue:
    """ O(1) access to the lowest-priority item """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item
    
    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)
class Rush_hour:
    def __init__(self, initial_state ) -> None:
        self.initial_state = initial_state
        self.frontier: PriorityQueue = PriorityQueue()
        self.explored_set = set()
        
    def run(self):
        self.frontier.push(item=self.initial_state, priority=(self.initial_state.f))
        i = 0
        while not self.frontier.isEmpty():
            state: Parking = self.frontier.pop()
            state_str = state.get_string_version()
            if state_str in self.explored_set:
                continue
            
            i += 1
            ic(i)
            
            self.explored_set.add(state_str)
            if state.check_goal():
                ic(f"Found with {state.g} moves")
                # self.show_solution(state=state)
                return
            state.generate_next_states()
            list_states = state.next_states
            self.add_to_frontier(list_states=list_states)
            
    
    def add_to_frontier(self, list_states):
        for state in list_states:
            ic(state.f)
            self.frontier.push(item=state, priority=(state.f))
    
    def add_to_explored_set(self, state_str):
        self.explored_set.add(state_str)
    
    def show_solution(self, state: Parking):
        while state:
            state.show_parking()
            print(" ")
            print(" ")
            print(" ")
            state = state.parent
            