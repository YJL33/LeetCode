#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
  string simplifyPath(string path) {
    vector<string> ans = helper(path);
    string res;
    for (auto x: ans) {
      res += x;
      res += "/";
    }
    return "/"+res.substr(0, res.size()-1);
  }
private:
  // for each i == '/' (which could stay at '/')
  // find j (which is the next '/')
  // check substr(i+1, j-i-2) (the stuff between both slash), with following cases:
  // check the length as well
  // 1. .
  // 2. ..
  // 3. others (folder name)
  vector<string> helper(string path) {
    vector<string> ans;
    for (int i=0; i<path.size(); ++i) {
      if (path[i] == '/') {
        int j=i+1;
        while (j<path.size() && path[j] != '/') ++j;
        // now check the length
        string foldername = path.substr(i+1, j-i-1);
        // cout << "now handling: " << foldername << endl;
        if (j-i-1 >= 1) {                            // .
          if (foldername == "..") {    // ..
            if (!ans.empty()) {
              ans.pop_back();
            } 
          } else if (foldername != ".") {
              ans.push_back(foldername);
          }
        }
        // cout << "ans size:" << ans.size() << endl;
      }
    }
    return ans;
  }
};