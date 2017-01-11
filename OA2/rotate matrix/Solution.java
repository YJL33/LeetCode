/*
Rotate matrix 90 degree
*/
public class Solution {
    public static int[][] rotate(int[][] matrix, int flag) {
        // flag = 0: counter-clockwise, vertical mirror => diagonal mirror
        // flag = 1: clockwise, horizontal mirror => diagonal mirror
        if (matrix == null || matrix.length == 0) return null;
        int m = matrix.length, n = matrix[0].length, tmp;
        int[][] res = new int[n][m];
        if (flag == 1) {
            // vertical mirroring
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n/2; j++) {
                    tmp = matrix[i][j];
                    matrix[i][j] = matrix[i][n-1-j];
                    matrix[i][n-1-j] = tmp;
                }
            }
        }
        else {
            // horizontal mirroring
            for (int j = 0; j < n; j++) {
                for (int i = 0; i < m/2; i++) {
                    tmp = matrix[i][j];
                    matrix[i][j] = matrix[m-1-i][j];
                    matrix[m-1-i][j] = tmp;
                }
            }
        }
        // i, j switch (diagonal mirroring)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[j][i] = matrix[i][j];
            }
        }
        // restore the matrix
        return res;
    }
    public static void mirror(int[][] matrix)
    public static void printMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++) System.out.print(matrix[i][j] + " ");
            System.out.println("");
        }
    }
    public static void main(String[] args) {
        int[][] input = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] output1 = rotate(input, 0);
        int[][] output2 = rotate(input, 1);
        System.out.println("input");
        printMatrix(input);
        System.out.println("output1");
        printMatrix(output1);
        System.out.println("output2");
        printMatrix(output2);
    }
}