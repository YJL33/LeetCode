/*
286

(rename the file to Solution.java and change L9 to static and compile)
cp 286.java Solution.java; javac Solution.java; java Solution
*/
import java.util.*;
class Solution {
    public void wallsAndGates(int[][] rooms) {
        List<int[]> stack = new ArrayList<int[]>();
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    int arr[] = {i,j,0};
                    stack.add(arr);
                    // dfs(rooms, i, j, 0);
                }
            }
        }
        while (!stack.isEmpty()) {
            int[] x = stack.get(stack.size()-1);    // {i, j, dist}
            stack.remove(stack.size()-1);
            if (x[0] < 0 || x[1] < 0 || x[0] >= rooms.length || x[1] >= rooms[0].length || rooms[x[0]][x[1]] < x[2]) {
                continue;
            }
            rooms[x[0]][x[1]] = x[2];
            stack.add(new int[]{x[0]+1, x[1], x[2]+1});
            stack.add(new int[]{x[0]-1, x[1], x[2]+1});
            stack.add(new int[]{x[0], x[1]+1, x[2]+1});
            stack.add(new int[]{x[0], x[1]-1, x[2]+1});
        }
        return;
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