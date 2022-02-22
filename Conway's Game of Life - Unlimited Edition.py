Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any live cell with two or three live neighbours lives on to the next generation.
Any dead cell with exactly three live neighbours becomes a live cell.
Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:

print(htmlize(cells))


Solution:
  
import numpy as np

def get_generation(cells, generations):
    
    current_world= np.array(cells)
    for i in range(generations):
        current_world = next_gen(current_world)
        current_world = crop_matrix(current_world)
    
    return current_world.tolist()

  
def count_neighbours(cells,x,y):
    x_pos = [-1,0,1]
    y_pos = [-1,0,1]
    
    sum = 0
    for i in x_pos:
        for j in y_pos:
            if len(cells[:,0]) > x+i >=0 and len(cells[0,:]) > y+j >=0:
                    if x+i != x or y+j != y:
                        if cells[x+i][y+j] == 1:
                            sum += 1
    return sum

  
def next_gen(cells):
    
    zeros = zero_matrix(len(cells[:,0])+2,len(cells[0,:])+2)
    
    #expand original cells
    cells_zeros = zero_matrix(len(cells[:,0])+2,len(cells[0,:])+2)
    for x in range(len(cells[:,0])):
        for y in range(len(cells[0,:])):
            cells_zeros[x+1][y+1] = cells[x][y]
    
    #create matrix of neighbour info
    for x in range(len(zeros[:,0])):
        for y in range(len(zeros[0,:])):
            zeros[x][y] = count_neighbours(cells_zeros,x,y)
    
    #next gen based on the 4 rules
    for x in range(len(cells_zeros[:,0])):
        for y in range(len(cells_zeros[0,:])):
            if cells_zeros[x][y]==1:
                if 1<zeros[x][y]<4:
                    zeros[x][y]=1
                else:
                    zeros[x][y]=0
            else:
                if zeros[x][y]==3:
                    zeros[x][y]=1
                else:
                    zeros[x][y]=0

    return zeros

  
def zero_matrix(x,y):
    return np.zeros((x,y))

  
def crop_matrix(matrix):
    for i in range(4):
        for i in matrix:
            if sum(i)!=0:
                break
            else:
                matrix = np.delete(matrix,0,axis=0)
        matrix = np.rot90(matrix)
    
    return matrix
