Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

ALGORITHMS ARRAYS


Solution:

def snail(snail_map):
    
    def step(v,h):
        blank_map[v][h] = 1
    
    def step_history(v,h):
        path_history_v.append(v)
        path_history_h.append(h)
    
    import numpy as np
    
    #if list adds up to 0 then return []
    if sum([sum(i) for i in snail_map]) == 0:
        return []
    
    #create blank map
    snail_map = np.array(snail_map)
    blank_map = np.zeros(np.shape(snail_map))
    
    #starting position
    v=0
    h=0
    
    path_history_v = []
    path_history_h = []
    
    #first step
    step(v,h)
    step_history(v,h)
    
    while np.sum(blank_map) != np.size(blank_map):

        #go right till reach the end or 1
        while len(blank_map[0])> h+1 and blank_map[v][h+1] != 1:
            h += 1
            step(v,h)
            step_history(v,h)

        #go down till reach the end or 1
        while len(blank_map)> v+1 and blank_map[v+1][h] != 1:
            v += 1
            step(v,h)
            step_history(v,h)

        #go left till reach the end or 1
        while h>0 and blank_map[v][h-1] != 1:
            h -= 1
            step(v,h)
            step_history(v,h)

        #go up till reach the end or 1
        while v>0 and blank_map[v-1][h] != 1:
            v -= 1
            step(v,h)
            step_history(v,h)
    
    #create solution list according to the steps recorded in the path history lists
    solution = []
    for i in range(0,len(path_history_v)):
        solution.append(snail_map[path_history_v[i]][path_history_h[i]])
    
    return solution
