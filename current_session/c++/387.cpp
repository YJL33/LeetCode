#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

// simply use a map as counter
class Solution {
public:
  int firstUniqChar(string s) {
    map<char, int> cnt;
    for (int i=0;i<s.size();i++) {
      if (cnt.find(s[i]) == cnt.end()) {
        cnt[s[i]] = i;
      } else {
        cnt[s[i]] += INT_MAX;
      }
    }

    int ans = INT_MAX;
    for (auto it: cnt) {
      ans = min(ans, it.second);      
    }
    return (ans != INT_MAX) ? ans : -1;
  }

  // store in an array instead of map
  int firstUniqChar2(string s) {
    // vector<int> v(26,0);
    int v[26] = {0};
		for(char c : s) v[c - 'a']++;
		for(int i = 0; i < s.length(); i++){
			if(v[s[i] - 'a'] == 1) return i;
		}
    return -1;
  }
};