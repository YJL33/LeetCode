#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

// usrpost map: key=user, val=list of tweets
// usrfollow map: key=user, val=set of following kols
// follow/unfollow: insert/remove from usrfollow[user]
// getNewsFeed: for all kols in usrfollow[user], get all posts from usrpost[kol]
// post: add into userPost map with timestamp
// sort and get top 10.

class Twitter {
public:
    map<int, vector<pair<int, int>>> usrPost;
    map<int, set<int>> usrFollow;
    int timestamp = 30003;
    /** Initialize your data structure here. */
    Twitter() {  
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
      if (usrPost.find(userId) == usrPost.end()) {usrFollow[userId].insert(userId);}
      usrPost[userId].push_back(pair<int, int>{--timestamp,tweetId});
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
      vector<pair<int,int>> feed;
      for (auto kol: usrFollow[userId]) {
        for (auto t: usrPost[kol]) {
          feed.push_back(pair<int, int>{t.first, t.second});
        }
      }
      // sort
      sort(feed.begin(), feed.end());
      vector<int> res;
      for (int i=0; i<feed.size() && i<10; ++i) {
        res.push_back(feed[i].second);
      }
      return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
      usrFollow[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
      usrFollow[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */