class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0

        # treat as positive
        is_negative = False
        if num < 0:
            is_negative = True
            num = -1*num

        # use arr
        arr = []
        while num > 0:
            arr.append(num%10)
            num = num//10

        arr.sort()
        if is_negative:
            # simply use the reversed array
            return -1*sum([arr[i]*(10**i) for i in range(len(arr))])
        else:
            # pick the smallest non-zero as first one, swap with first and rest are the same
            i = 0
            while arr[i] == 0:
                i += 1
            
            arr[i], arr[0] = arr[0], arr[i]
            return sum([arr[~i]*(10**i) for i in range(len(arr))])