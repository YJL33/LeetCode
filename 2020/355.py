"""
355
"""
import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seenUser = {}          # key: id, val: list of newsFeed
        self.followingOfId = {}     # key: id, val: set of following KOLs
        self.t = 30009              # decreasing: easier for heap operation

    def _initUser(self, id):
        self.seenUser[id] = []
        self.followingOfId[id] = set([id])      # follow themselves

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.seenUser: self._initUser(userId)
        self.seenUser[userId] += (self.t, tweetId),
        self.t -= 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        sources = []
        tmp = {}
        if userId not in self.seenUser: return []
        for kol in self.followingOfId[userId]:
            if len(self.seenUser[kol]) != 0:                # has some post
                tmp[kol] = len(self.seenUser[kol])-1        # get the latest post of kol
                t, tweetId = self.seenUser[kol][-1]
                heapq.heappush(sources, (t, tweetId, kol))
        
        while len(res) < 10 and sources:
            _, tid, kol = heapq.heappop(sources)
            tmp[kol] -= 1
            if tmp[kol] >= 0:
                t, newTid = self.seenUser[kol][tmp[kol]]
                heapq.heappush(sources, (t, newTid, kol))
            res.append(tid)

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.seenUser: self._initUser(followerId)
        if followeeId not in self.seenUser: self._initUser(followeeId)
        self.followingOfId[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.seenUser: self._initUser(followerId)
        if followeeId not in self.seenUser: self._initUser(followeeId)
        if followeeId in self.followingOfId[followerId]: self.followingOfId[followerId].remove(followeeId)
        return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)