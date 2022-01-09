class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]     # N E S W
        i = 0       # facing north
        pos = [0,0]
        for ins in instructions:
            if ins == "L":
                i -= 1
            elif ins == "R":
                i += 1
            else:
                dy, dx = direction[i%4]
                pos = pos[0]+dx, pos[1]+dy
        # if position != (0,0), check direction
        return (pos[0] == 0 and pos[1] == 0) or (i%4 != 0)