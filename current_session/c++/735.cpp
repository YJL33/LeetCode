#include <iostream>
#include <vector>

using namespace std;

// think about 2 situations
// <- ->    do nothing
// -> <-    handle
// only need to handle if incoming asteroid is negative

class Solution {
public:
  vector<int> asteroidCollision(vector<int>& asteroids) {
    vector<int> res;
    for (int i=0; i<asteroids.size(); ++i) {
      int cur = asteroids[i];
      if (cur > 0) {
        res.push_back(cur);
      } else {
        while (!res.empty() && 0<res.back() && res.back()<-1*cur) {
          res.pop_back();
        }
        if (!res.empty() && res.back()==-1*cur) {
          res.pop_back();
        } else if (res.empty() || res.back()<0) {
          res.push_back(cur);
        }
      }
    }
    return res;
  }
};