#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
class NestedInteger {
  public:
    // Constructor initializes an empty nested list.
    NestedInteger();
    // Constructor initializes a single integer.
    NestedInteger(int value);
    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;
    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;
    // Set this NestedInteger to hold a single integer.
    void setInteger(int value);
    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    void add(const NestedInteger &ni);
    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger> &getList() const;
};

class Solution {
public:
  vector<int> res;
  int depthSum(vector<NestedInteger>& nestedList) {
    helper(nestedList, 1);
    return accumulate(res.begin(), res.end(), 0);
  }
  void helper(vector<NestedInteger>& nestedList, int d) {
    for (auto n: nestedList) {
      if (n.isInteger()) {
        res.push_back(d*n.getInteger());
      } else {
        vector<NestedInteger> x = n.getList();
        helper(x, d+1);
      }
    }
    return;
  }
};