"""
You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water. Grid cells are connected
horizontally/vertically (not diagonally). The grid is completely surrounded
by water, and there is exactly one island (i.e., one or more connected land
cells). The island doesn't have "lakes" (water inside that isn't connected
to the water around the island). One cell is a square with side length 1.
The grid is rectangular,width and height don't exceed 100. Determine the
perimeter of the island.


Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
The perimeter is 16.
"""

class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        X = len(grid[0]) # width
        Y = len(grid)    # height
        perimeter = 0
        for i in range(X):
            for j in range(Y):
                if grid[j][i] == 1: 
                    perimeter += 4 # each land provides perimeter with 4
                    if j > 0 and grid[j-1][i] == 1:
                        perimeter -= 2 # a land next to one land, perimeter-1
                                       # a land next to two lands, perimeter-2
                                       # one 'next' involves two lands so -2
                    if i > 0 and grid[j][i-1] == 1:
                        perimeter -= 2
        return perimeter

if __name__ == '__main__':
    print(Solution().islandPerimeter([[0,1,0,0],
                                      [1,1,1,0],
                                      [0,1,0,0],
                                      [1,1,0,0]]))
