/*
200. Number of Islands

    Total Accepted: 66479
    Total Submissions: 216930
    Difficulty: Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

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
*/
public class Solution {
    private char[][] grd;
    public int numIslands(char[][] grid) {
        int result = 0;
        if (grid.length == 0 || grid[0].length == 0) return 0;
        grd = new char[grid.length][grid[0].length];
        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[i].length; j++) {
                grd[i][j] = grid[i][j];
            }
        }
        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[i].length; j++) {
                result += sink(i, j);
            }
        }
        return result;
    }

    private int sink(int i, int j) {
        if (0 <= i && i < grd.length && 0 <= j && j < grd[i].length)
        {
            grd[i][j] = '0';
            sink(i+1, j);
            sink(i-1, j);
            sink(i, j+1);
            sink(i, j-1);
            return 1;
        }
        return 0;
    }
}