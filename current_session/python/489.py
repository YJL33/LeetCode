# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        seen = set()
        fd = [(0,1),(1,0),(0,-1),(-1,0)]               # N E S W
        # beware of its facing
        def dfs(x,y,f):
            # clean the spot
            robot.clean()
            seen.add((x,y))
            # for each of its neighbor, move there and clean it
            for _ in range(4):
                nb = (x+fd[f%4][0], y+fd[f%4][1])
                if nb not in seen and robot.move():     # try to move there and clean
                    dfs(nb[0], nb[1], f%4)
                robot.turnRight()
                f += 1
            # after all neighbor are cleaned, return to previous spot
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            return
        
        dfs(0,0,0)              # initially facing north (according to description)
        return
