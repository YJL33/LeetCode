class Solution {
    public int majorityElement(int[] nums) {
        int pick = nums[0];
        int cnt = 1;
        for (int i=1; i<nums.length; i++) {
            if (cnt == 0) {
                pick = nums[i];
                cnt = 1;
            } else if (nums[i] == pick) {
                cnt++;
            } else {
                cnt--;
            }
        }
        return pick;
    }
}