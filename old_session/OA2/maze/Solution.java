/*
maze
*/
import java.util.*;
public class Solution {
    static final int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public static int checkMaze(int[][] maze)
    {
        if (maze == null || maze.length == 0 || maze[0].length == 0) return 0;
        if (maze[0][0] == 9) return 1;
        Queue<int[]> path = new LinkedList<>();
        path.add(new int[]{0, 0});
        maze[0][0] = 0;             // change visited grid as 0
        while (!path.isEmpty())
        {
            int[] grid = path.poll();
            for (int i = 0; i < 4; i++)
            {
                int row = grid[0] + dir[i][0];
                int col = grid[1] + dir[i][1];
                if (row >= 0 && row < maze.length && col >=0 && col < maze[0].length) {
                    if (maze[row][col] == 9) return 1;
                    else if (maze[row][col] == 1)
                    {
                        path.add(new int[]{row, col});
                        maze[row][col] = 0;
                    }
                }
            }
        }
        return 0;
    }
    public static void printMatrix(int[][] matrix)
    {
        int m = matrix.length, n = matrix[0].length;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++) System.out.print(matrix[i][j] + " ");
            System.out.println("");
        }
    }
    public static void main(String[] args)
    {
        int[][] maze = {{1, 0, 0, 1}, {1, 1, 1, 1}, {1, 0, 0, 9}};
        printMatrix(maze);
        System.out.println(checkMaze(maze));
    }
}