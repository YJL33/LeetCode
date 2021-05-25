/*
Maximum Minimum Path
*/
public class Solution {
    public static int find(int[][] matrix)
    {
        int m = matrix.length, n = matrix[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = matrix[i][j];
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;         // keep 0, 0 as unchanged
                int up = Integer.MIN_VALUE, left = Integer.MIN_VALUE;
                if (i - 1 >= 0) up = Math.min(dp[i][j], dp[i-1][j]);
                if (j - 1 >= 0) left = Math.min(dp[i][j], dp[i][j-1]);
                dp[i][j] = Math.max(up, left);
            }
        }
        return dp[m-1][n-1];
    }
    public static int find2(int[][] input)
    {
        int m = input.length, n = input[0].length;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(i == 0 && j == 0) continue;
                int a = Integer.MIN_VALUE, b = Integer.MIN_VALUE;
                if(i - 1 >= 0) a = Math.min(input[i][j], input[i - 1][j]);
                if(j - 1 >= 0) b = Math.min(input[i][j], input[i][j - 1]);
                input[i][j] = Math.max(a, b);
//              System.out.println("i = "+ i);
//              System.out.println("j = "+ j);
//              System.out.println("input[i][j] = "+ input[i][j]);
            }
        }
        return input[m - 1][n - 1];
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int[][] input = {{2, 2, 3 ,4}, {1, 2, 3, 4},{1, 2, 3, 4}};
        System.out.println(find(input));
        System.out.println(find2(input));
    }
 
}