'''
astar.py
By Anna Quinlan and Sophia Davis
'''

from puzzle8 import *
from heuristic import *
from itdeep import *
import Queue
import time

# Nodes contain state, parent, total path cost (g), and heuristic (h) of that state.
# Nodes can then be added to priority queue based on comparison (g+h).
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

# Astar function is an adaptation of algorithm from our textbook.
# This implementation does not prevent repeated states on the frontier, but this
# does not affect the solution found.
def astar(state, heuristic):
	
	# For experiments:
	#start = time.time()
	
	# Null parent is a fake parent for the starting node.
	null_parent = Node(0,0,0,0)
	node = Node(state, null_parent, 0, heuristic(state))
	
	frontier = Queue.PriorityQueue()
	frontier.put(node)
	
	explored = []
	count = 0
	
	# Loop through the frontier until it is empty or a solution is found.
	while not frontier.empty():
		count += 1
		node = frontier.get()
		
		# For experiments:
		#print "Node f value:"
		#print node.g + node.h
		
		state = node.state
		if state == solution():
			
			# For experiments:
			#end = time.time()
			#print heuristic
			#print "COUNT"
			#print count
			#print "DEPTH OF SOLN"
			#print node.g
			#print "ASTAR time"
			#print end - start
			
			return getpath(node)
		
		explored.append(state)
		
		# Expand possible new nodes and put on the frontier if state hasn't yet
		# been explored
		blank = blankSquare(state)
		neighbors_list = neighbors(blank)
		for neighbor in neighbors_list:
			new_state = moveBlank(state, neighbor)
			if new_state not in explored:
				new_node = Node(new_state, node, node.g+1, heuristic(new_state))
				frontier.put(new_node)
	
	# Failure node is needed for comparison.
	return Node("failure", 0, 0, 0)

# Function for finding path to solution (each node stores its parent).		
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


# Experiments

'''
A* with manhattan distance is the fastest and explores the fewest nodes, especially
obvious in our last two experiments, which were generated with 50 and 100 random moves.
Itdeep is a lot slower than A* with either heuristic and expands many more nodes. For
example, for random state 23225468, itdeep took 83.65314912794831 sec longer than A* 
manhattan distance, almost 5233 times as long.
'''
# First state from test file:
# itdeep: 0.000391960144043 sec, 8 nodes expanded, depth of soln 2
# astar (num_wrong_tiles): 0.000737190246582 sec, 3 nodes expanded, depth of soln 2
# astar (manhattan_distance): 0.000654935836792 sec, 3 nodes expanded, depth of soln 2

# Second state from test file:
# itdeep: 0.247884988785 sec, 5683 nodes expanded, depth of soln 8
# astar (num_wrong_tiles): 0.00707197189331 sec, 23 nodes expanded, depth of soln 8
# astar (manhattan_distance): 0.00457906723022 sec, 15 nodes expanded, depth of soln 8

# Random state with 5 random moves (state 253241740):
# itdeep: 0.00350904464722 sec, 51 nodes expanded, depth of soln 3
# astar (num_wrong_tiles): 0.00109601020813 sec, 4 nodes expanded, depth of soln 3
# astar (manhattan_distance): 0.00142693519592 sec, 5 nodes expanded, depth of soln 3

# Random state with 50 random moves (state 23225468):
# itdeep: 63.3641190529 sec, 1447783 nodes expanded, depth of soln 14
# astar (num_wrong_tiles): 0.0761499404907 sec, 265 nodes expanded, depth of soln 14
# astar (manhattan_distance): 0.0284729003906 sec, 83 nodes expanded, depth of soln 14

# Random state with 100 random moves (state 23225468):
# itdeep: 83.6691379547 sec, 1897014 nodes expanded, depth of soln 14
# astar (num_wrong_tiles): 0.0784840583801 sec, 268 nodes expanded, depth of soln 14
# astar (manhattan_distance): 0.0159888267517 sec, 48 nodes expanded, depth of soln 14

'''
Random state code:
teststate = randomState(numMoves=50)
print "TEST STATE"
print teststate
itdeep(teststate)
astar(teststate, num_wrong_tiles)
astar(teststate, manhattan_distance)
'''