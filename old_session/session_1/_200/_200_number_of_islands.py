"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        labels = [[-1 for i in xrange(width)] for j in xrange(height)]
        link = [0]
        
        #print height, width, len(link)

        def FirstPass(row, col, latest_label, label_records, relevance):
            # Use the way learned from EE569
            # 1st pass: label all grid.
            # if the coordinate is valid: check this point is land or water:
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                # if land, check the neighborhoods are empty or not:
                if grid[row][col] == '1':
                    neighbors = []
                    if row-1 >= 0:
                        if label_records[row-1][col] > 0:
                            neighbors.append(label_records[row-1][col])
                    if col-1 >= 0:
                        if label_records[row][col-1] > 0:
                            neighbors.append(label_records[row][col-1])

                    # neighbors are all empty
                    if len(neighbors) == 0:
                        label_records[row][col] = latest_label
                        relevance.append(latest_label)
                        latest_label += 1
                        return latest_label
                    # neighbors are not empty => label the minimum one, and link them
                    else:
                        label_records[row][col] = min(neighbors)
                        for n in neighbors:
                            while n != relevance[n]:
                                n = relevance[n]        # Trace to the root
                            if n > min(neighbors):
                                relevance[n] = min(neighbors)       # and link the root with its neighbor
                        return latest_label

                # if water, go next.
                if grid[row][col] == '0':
                    label_records[row][col] = 0
                    return latest_label

        def SecondPass(next, link):
            # 2nd pass: count the labels, and return the actual non-connected ones.
            island_count = 0
            for i in xrange(next):
                if link[i] == i:
                    island_count += 1
            return island_count-1
        ######

        latest_label = 1

        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                latest_label = FirstPass(i, j, latest_label, labels, link)
        
        return SecondPass(latest_label, link)


print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), "should be 1")
print(Solution().numIslands([["1","1","0","1","0"],["1","1","1","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), "should be 1")
print(Solution().numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]), "should be 1")
print(Solution().numIslands([["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]]), "should be 23")