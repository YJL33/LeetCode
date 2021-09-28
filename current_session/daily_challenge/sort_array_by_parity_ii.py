from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # swap in-place
        # simply use a stack
        stack1 = []          # store those odd number in even indexes
        stack2 = []

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            return

        for i in range(len(nums)):
            if i%2:
                if nums[i]%2:
                    continue
                else:
                    if stack1:
                        swap(i, stack1[-1])
                        stack1.pop()
                    else:
                        stack2.append(i)
            else:
                if nums[i]%2:
                    if stack2:
                        swap(i, stack2[-1])
                        stack2.pop()
                    else:
                        stack1.append(i)
                else:
                    continue
        return nums

print(Solution().sortArrayByParityII([4,2,5,7]))
print(Solution().sortArrayByParityII([1,3,5,7,9,2,4,6,8,10]))
print(Solution().sortArrayByParityII([2,4,6,8,10,1,3,5,7,9]))