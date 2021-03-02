/*
286

(rename the file to Solution.java and change L9,L15 to static and compile)
cp 286.java Solution.java; javac Solution.java; java Solution
*/
import java.util.*;
class Solution {
    public void wallsAndGates(int[][] rooms) {
    for (int i = 0; i < rooms.length; i++)
        for (int j = 0; j < rooms[0].length; j++)
            if (rooms[i][j] == 0) dfs(rooms, i, j, 0);
    }

    private void dfs(int[][] rooms, int i, int j, int d) {
        if (i < 0 || i >= rooms.length || j < 0 || j >= rooms[0].length || rooms[i][j] < d) return;
        rooms[i][j] = d;
        dfs(rooms, i - 1, j, d + 1);
        dfs(rooms, i + 1, j, d + 1);
        dfs(rooms, i, j - 1, d + 1);
        dfs(rooms, i, j + 1, d + 1);
    }
    public static void main(String[] args)
    {
        int[][] input = {{-1}};
        wallsAndGates(input);
        for (int[] row : input) {
            System.out.println(Arrays.toString(row) + ", shoudl be -1");
        }
    }
}