#include <iostream>

using namespace std;

// simply use a counter and return the current value

class RLEIterator {
public:
  int cnt = 0;
  int eIndex = 1;
  vector<int> encodingArr;
  RLEIterator(vector<int>& encoding) {
    encodingArr = encoding;
  }
  
  int next(int n) {
    // get the answer while maintain the array
    int ans = -1;

    // keep decreasing n
    // move to next index (also consider cnt == encodingArr[eIndex-1])
    while (eIndex < encodingArr.size() && cnt+n > encodingArr[eIndex-1] ) {
      n -= (encodingArr[eIndex-1] - cnt);
      cnt = 0;
      eIndex += 2;
    }
    
    // get the answer
    if (eIndex < encodingArr.size() && cnt+n <= encodingArr[eIndex-1]) {
      cnt += n;
      ans = encodingArr[eIndex];
      n = 0;
    }
   
    return ans;
  }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */