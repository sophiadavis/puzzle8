'''
heuristic.py 
by Anna Quinlan and Sophia Davis
'''

from puzzle8 import *
import math

# returns the number of misplaced tiles for a given state
def num_wrong_tiles(state):
	countwrong = 0
	for i in range(9):
		if i == blankSquare(state):
			continue
		elif misplaced(state,i):
			countwrong += 1
	return countwrong

# given a square and state, returns whether the correct number is there
def misplaced(state, square):
	if square < 3:
		if getTile(state,square) != square+1:
			return True
	elif square == 3:
		if getTile(state,square) != 8:
			return True
	elif square == 4:
		if getTile(state,square) != 0:
			return True
	elif square == 5:
		if getTile(state,square) != 4:
			return True
	# last row is backwards so subtract from 13
	else:
		if getTile(state,square) != 13-square:
			return True
	return False

# give a value, returns the correct square index in the solution
def get_correct_square(value):
	if value == 1:
		return 0
	if value == 2:
		return 1
	if value == 3:
		return 2
	if value == 4:
		return 5
	if value == 5:
		return 8
	if value == 6:
		return 7
	if value == 7:
		return 6
	if value == 8:
		return 3
	# value is 0
	else:
		return 4

# returns the total Manhattan distance for the misplaced tiles for the 
# indicated state.
def manhattan_distance(state):
	distance = 0
	for i in range(9):
	    
	    # for all misplaced values
		if misplaced(state,i):
		
			# find actual location of the value
			xi = xylocation(i)[0]
			yi = xylocation(i)[1]
			
			# find correct location for the value
			value = getTile(state, i)
			j = get_correct_square(value)
			xj = xylocation(j)[0]
			yj = xylocation(j)[1]
	
	        # add Manhattan distance to total Manhattan distance
			distance += math.fabs(xi - xj) + math.fabs(yi - yj)

	return distance
	
