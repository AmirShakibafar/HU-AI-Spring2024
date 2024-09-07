import numpy as np
from icecream import ic
from copy import deepcopy
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
            
class Stock_Basket:
    def __init__(self, w, r) -> None:
        self.w: list = w
        self.r: list = r
        self.frontier: PriorityQueue = PriorityQueue()
        
    def evaluation_function(self, lamda = 1):
        return np.dot(self.w.T, self.r) - lamda * np.sqrt(np.dot(self.w.T, self.w.T) * np.cov(self.w))
    
    def generate_next_states(self, step):
        for i in range(len(self.w)):
            temp_weights = deepcopy(self.w)
            rest = len(temp_weights) - 1
            temp_weights[i] += step
            percent_to_cut = step / rest
            
            for j in range(len(self.w)):
                if j == i:
                    continue
                temp_weights[j] -= percent_to_cut
                
            stock_basket: Stock_Basket = Stock_Basket(w=temp_weights, r=self.r)
            self.frontier.push(item=stock_basket, priority= -1 * stock_basket.evaluation_function())
            
class Sim_annealing:
    def __init__(self, initial) -> None:
        self.initial: Stock_Basket = initial
    
    
    def hill_climbing_loop(self, curr, best_child, step):
        
        while curr.evaluation_function() <= best_child.evaluation_function():
            curr = best_child
            curr.generate_next_states(step)
            best_child: Stock_Basket = curr.frontier.pop()
        
        return curr
            
    def run(self):
        curr = self.initial
        max_portfolio = self.initial
        curr.generate_next_states(step=1)
        best_child: Stock_Basket = max_portfolio.frontier.pop()
        
        for i in range(100, 0, -1):
            
            candidate: Stock_Basket = self.hill_climbing_loop(curr=curr, best_child=best_child, step=i / 10)
            if candidate.evaluation_function() >= max_portfolio.evaluation_function():
                max_portfolio = candidate
    
        return max_portfolio
 

        
w = np.array([25, 46, 29])
r = np.array([15, 10, 2])
   
            
s = Stock_Basket(w=w, r=r)
test = Sim_annealing(initial=s)
res = test.run().evaluation_function()
ic(res)

