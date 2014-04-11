'''
astar.py
By Anna Quinlan and Sophia Davis
'''

from puzzle8 import *
from heuristic import *
import Queue

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def __cmp__(self,other):
        '''__cmp__ is supposed to return a negative number if self is
        "smaller" than other, 0 if equal, and a positive number if
        "greater."'''
        return  (self.g + self.h) - (other.g + other.h)
    
    def __str__(self):
    	print "--- node ---"
    	print self.state
    	print self.parent
    	print self.g
    	print self.h
    	return "---"

def astar(state, heuristic):
	
	null_parent = Node(0,0,0,0)
	node = Node(state, null_parent, 0, heuristic(state))
	# print node.state
	# print "G:"
	# print node.g
	
	frontier = Queue.PriorityQueue()
	frontier.put(node)
	
	explored = []
	
	while not frontier.empty():
		node = frontier.get()
		state = node.state
		if state == solution():
			return getpath(node)
		explored.append(state)
		
		blank = blankSquare(state)
		# print "------"
		# print blank
		neighbors_list = neighbors(blank)
		for neighbor in neighbors_list:
			new_state = moveBlank(state, neighbor)
			if new_state not in explored:
				# print "G:"
				# print node
				new_node = Node(new_state, node, node.g+1, heuristic(new_state))
				frontier.put(new_node)
				
	return Node("failure", 0, 0, 0)
			
def getpath(result):
	
	if result.state == "failure":
		return "failure"
	else:
		path = []
		state = result.state
		parent = result.parent
		while parent.state != 0:
			blank_to = blankSquare(state)
			blank_from = blankSquare(parent.state)
			path.insert(0, (blank_from, blank_to))
			
			state = parent.state
			parent = parent.parent
		return path	



