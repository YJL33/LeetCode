from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # simply add with carry
        res = []            # reverse before return
        carry = 1
        i = len(digits)-1

        while carry > 0 or i >= 0:
            x = carry
            if i >= 0: x += digits[i]
            carry, num = x//10, x%10
            res.append(num)
            i -= 1

        res.reverse()
        return res
            

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([4,3,2,1]))
print(Solution().plusOne([0]))
print(Solution().plusOne([9,9,9]))
