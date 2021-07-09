class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # check the length given the initial char
        def checkLength(char):
            if char<128:
                return 1
            elif 192<=char<224:
                return 2
            elif 224<=char<240:
                return 3
            elif 240<=char<248:
                return 4
            else:
                return -1

        # check the UTF8 character
        def isValidUTF8(arr):
            # print([bin(a) for a in arr])
            for a in arr[1:]:
                if a<128 or a>=192:
                    return False
            return True
        
        i = 0
        while i < len(data):
            l = checkLength(data[i])
            if l<0 or l!=len(data[i:i+l]) or not isValidUTF8(data[i:i+l]):
                return False
            i += l
        return True

print(Solution().validUtf8([197,130,1]))
print(Solution().validUtf8([235,140,4]))
print(Solution().validUtf8([64]))
print(Solution().validUtf8([167]))
print(Solution().validUtf8([255]))
print(Solution().validUtf8([2,15,76,44,88]))
print(Solution().validUtf8([100,100,200,100,300,200,1,2,3,4,5,6,7,10]))
print(Solution().validUtf8([12,22,32,43,23,22]))