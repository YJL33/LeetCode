/*
#440
*/
public class Solution {
    public int findKthNumber(int n, int k) {
        if (n <= 9 || k == 1) return k;
        int init = 1;
        int res = 0;
        int bktID = 0;
        int[] sumOfBkts = new int[] {n};

        while (k > 0)
        {
            k -= 1;
            sumOfBkts = getBucket(sumOfBkts[bktID], init);
            int[] bktAndK = findDigit(sumOfBkts, k);
            if (bktAndK[0] != 10) { res = res*10+(bktAndK[0]+init); }
            else { res += 1; }
            init = 0;
        }
        return res;
    }
    private int[] getBucket(int n, int init) {
        int length;
        if (init == 0) {
            n -= 1;
            length = 10;
        }
        else { length = 9; }
        int[] newBkt = new int[length];
        int num = 1;
        int b = 0;
        while (n > 0)
        {
            int add;
            if (n-num > 0) { add = num;}
            else { add = n; }
            newBkt[b] += add;
            n -= num;
            b += 1;
            if (b == length) {
                num *= 10;
                b = 0;
            }
        }
        return newBkt;
    }
    private int[] findDigit(int[] sumBkt, int k) {
        int[] pair = new int[2];
        pair[0] = 0;
        pair[1] = k;
        while (pair[1]-sumBkt[pair[0]] >= 0)
        {
            pair[1] -= sumBkt[pair[0]];
            pair[0] += 1;
        }
        return pair;
    }
}