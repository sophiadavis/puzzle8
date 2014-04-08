'''
itdeep.py
By Anna Quinlan and Sophia Davis
'''

from puzzle8 import *

# function for implementing iterative deepening
# relies on depthlimitedsearch and getpath helper functions
def itdeep(state):
	depth = 0
	solutionfound = False
	while solutionfound == False:
		
		# node consists of state and parent node
		# first node does not have parent, so is 0
		node = (state, 0)
		result = depthlimitedsearch(node, depth)
		depth += 1
		
		# when depthlimitedsearch finds solution, return path
		# otherwise, continue searching at deeper depth
		if result != "cutoff":
			solutionfound = True
			return getpath(result)

# function for finding path to solution (each node stores its parent)			
def getpath(result):
	
	if result == "cutoff":
		return "cutoff"
	elif result == "failure":
		return "failure"
	else:
		path = []
		state = result[0]
		parent = result[1]
		while parent != 0:
			blank_to = blankSquare(state)
			blank_from = blankSquare(parent[0])
			path.insert(0, (blank_from, blank_to))
			
			state = parent[0]
			parent = parent[1]
		return path

# an implementation of recursive depthlimitedsearch from textbook
# it can return: 
# - solution
# - "cutoff" - no solution found within limit
# - "failure" - entire search space was searched and no solution exists
def depthlimitedsearch(node, limit):
	
	state = node[0]
	if state == solution():
		return node
	elif limit == 0:
		return "cutoff"
	else:
		cutoff_occurred = False
		blank = blankSquare(state)
		neighbors_list = neighbors(blank)
		
		# recursively call depthlimitedsearch on neighbors (states produced
		# by moving blank square)
		for neighbor in neighbors_list:
			new_state = moveBlank(state, neighbor)
			new_node = (new_state, node)
			result = depthlimitedsearch(new_node, limit-1)
			if result == "cutoff":
				cutoff_occurred = True
			elif result != "failure":
				return result
		if cutoff_occurred:
			return "cutoff"
		
		# we should never return failure because there is always a 
		# solution to the 8 puzzle
		else:
			return "failure"