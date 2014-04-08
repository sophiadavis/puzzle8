'''
itdeep.py
By Anna Quinlan and Sohpia Davis
'''

from puzzle8 import *

def itdeep(state):
    frontier = [state]
    path = []
    
    blank_start = blankSquare(state)
    
    l = 5
    depth = 0
    
    while len(frontier) != 0:
        if depth != l:
            n = frontier.pop(0)
            print "---------Popping state n: "
            print n
            
            blank_finish = blankSquare(n)
            path.append((blank_start, blank_finish))
            print "Current path: "
            print path
            
            if n == solution():
                return path
            else:
                blank = blankSquare(n)
                blank_start = blank
                neighbors_list = neighbors(blank)
                print neighbors_list
                depth += 1
                if depth ! = l:
                    while len(neighbors_list) != 0:
                        neighbor = neighbors_list.pop()
                        print "Neighbor is: "
                        print neighbor
                        new_state = moveBlank(n, neighbor)
                        print "New state is: "
                        print new_state
                        frontier.insert(0, new_state)
        depth -= 1
        path.pop()
        
    print "No Solution"
    return "No Solution"
                    