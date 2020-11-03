"""
see https://leetcode.com/problems/robot-bounded-in-circle/
"""
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # check the position, if it stays at original spot -> true
        direction, i, lr, pos = [(0,1),(1,0),(0,-1),(-1,0)], 0, 0, [0,0]
        for ins in instructions:
            if ins == 'L':
                i, lr = i-1, lr-1
                if i < -1*(len(direction)):
                    i += len(direction)
            elif ins == 'R':
                i, lr = i+1, lr+1
                if i == len(direction):
                    i -= len(direction)
            else:
                x, y = direction[i]
                pos[0], pos[1] = pos[0]+x, pos[1]+y

        # circle won't exist if overall operation has no direction
        return True if (pos[0] == 0 and pos[1] == 0) else lr%4 != 0
        

print(Solution().isRobotBounded("GGLLGG"))
print(Solution().isRobotBounded("GLGLGGLGL"), "should be False")
print(Solution().isRobotBounded("GG"))
print(Solution().isRobotBounded("GL"))
