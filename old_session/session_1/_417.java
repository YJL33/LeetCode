/*
417. Pacific Atlantic Water Flow

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Given an m x n matrix of non-negative integers representing the height of each
unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right)
from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow,
to both the Pacific and Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
(positions with parentheses in above matrix).
*/
import java.util.ArrayList;
import java.util.List;

public class Solution {

    public static List<int[]> pacificAtlantic(int[][] matrix) {
        int height = matrix.length;
        if (height == 0) { return new ArrayList(); }
        int width = matrix[0].length;
        if (width == 0) { return new ArrayList(); }

        Square[][] grid = new Square[height][width];
        // create Square objects
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                grid[row][col] = new Square();
            }
        }
        // mark .canGoPac and .canGoAtl as true for edges
        for (int row = 0; row < height; row++) {
            grid[row][0].canGoPac = true;
            grid[row][width-1].canGoAtl = true;
        }
        for (int col = 0; col < width; col++) {
            grid[0][col].canGoPac = true;
            grid[height-1][col].canGoAtl = true;
        }
        // visit every square and drop water on it
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                if (!grid[row][col].visited)
                    dropWater(row, col, grid, matrix);
            }
        }
        // Re-visit every square and drop water on it
        boolean noCorrection = false;
        while (!noCorrection) {
            noCorrection = true;
            for (int row = 0; row < height; row++) {
                for (int col = 0; col < width; col++) {
                    boolean beforep = grid[row][col].canGoPac;
                    boolean beforea = grid[row][col].canGoAtl;
                    revisit(row, col, grid, matrix);
                    if ((beforep != grid[row][col].canGoPac) || (beforea != grid[row][col].canGoAtl)) {
                        noCorrection = false;
                    }
                }
            }
        }

        ArrayList<int[]> res = new ArrayList<int[]>();
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                int[] arr = new int[2];
                if (grid[row][col].canGoPac && grid[row][col].canGoAtl) {
                    arr[0] = row;
                    arr[1] = col;
                    res.add(arr);
                }
            }
        }
        return res;
    }
    public static class Square {
        public boolean canGoPac;
        public boolean canGoAtl;
        public boolean visited;

        public Square() {
            canGoPac = false;
            canGoAtl = false;
            visited = false;
        }
    }
    // drop water on a square, let it flow to surrounding squares if possible,
    // and then update the current square's .canGoPac and .canGoAtl
    // instance variables
    public static void dropWater(int row, int col, Square[][] grid, int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;

        grid[row][col].visited = true;


        // up
        if (row != 0 && matrix[row][col] >= matrix[row-1][col]) {
            if (!grid[row-1][col].visited)
                dropWater(row-1, col, grid, matrix);
            grid[row][col].canGoPac |= grid[row-1][col].canGoPac;
            grid[row][col].canGoAtl |= grid[row-1][col].canGoAtl;
        }

        // down
        if (row != height-1  && matrix[row][col] >= matrix[row+1][col]) {
            if (!grid[row+1][col].visited)
                dropWater(row+1, col, grid, matrix);
            grid[row][col].canGoPac |= grid[row+1][col].canGoPac;
            grid[row][col].canGoAtl |= grid[row+1][col].canGoAtl;
        }

        // left
        if (col != 0 && matrix[row][col] >= matrix[row][col-1]) {
            if (!grid[row][col-1].visited)
                dropWater(row, col-1, grid, matrix);
            grid[row][col].canGoPac |= grid[row][col-1].canGoPac;
            grid[row][col].canGoAtl |= grid[row][col-1].canGoAtl;
        }

        // right
        if (col != width-1 && matrix[row][col] >= matrix[row][col+1]) {
            if (!grid[row][col+1].visited) {
                dropWater(row, col+1, grid, matrix);
            }

            grid[row][col].canGoPac |= grid[row][col+1].canGoPac;
            grid[row][col].canGoAtl |= grid[row][col+1].canGoAtl;
        }
    }
    public static void revisit(int row, int col, Square[][] grid, int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;

        // up
        if (row != 0 && matrix[row][col] >= matrix[row-1][col]) {
            grid[row][col].canGoPac |= grid[row-1][col].canGoPac;
            grid[row][col].canGoAtl |= grid[row-1][col].canGoAtl;
        }

        // down
        if (row != height-1  && matrix[row][col] >= matrix[row+1][col]) {
            grid[row][col].canGoPac |= grid[row+1][col].canGoPac;
            grid[row][col].canGoAtl |= grid[row+1][col].canGoAtl;
        }

        // left
        if (col != 0 && matrix[row][col] >= matrix[row][col-1]) {
            grid[row][col].canGoPac |= grid[row][col-1].canGoPac;
            grid[row][col].canGoAtl |= grid[row][col-1].canGoAtl;
        }

        // right
        if (col != width-1 && matrix[row][col] >= matrix[row][col+1]) {
            grid[row][col].canGoPac |= grid[row][col+1].canGoPac;
            grid[row][col].canGoAtl |= grid[row][col+1].canGoAtl;
        }
    }
    public static void main(String[] args) {
        /*
        int[][] height = {
            {3, 3, 3, 3, 3, 3},
            {3, 0, 3, 3, 3, 3},
            {3, 3, 3, 3, 3, 3},
        };

        List<int[]> divide = pacificAtlantic(height);
        System.out.println();

        for (int[] p : divide) {
            System.out.print(p[0]);
            System.out.print(p[1]);
            System.out.println();
        }
        */
    }
}

