#include <iostream>
#include <string>
#include <vector>

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
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        // go through each item, if NI: add into result
        // else: recursively call this method
        // maintain a vector, and calculate the sum after visit all nodes
        // vector[i] = result of level i-1
        vector<int> result;

        dfs(nestedList, 0, result);
        // post processing
        int levelSum = 0;
        int maxDepth = result.size();
        for (int i=0; i<result.size(); i++) {
            levelSum += result[i]*(maxDepth-i);
            // cout<<levelSum;
        }
        return levelSum;
    }
private:
    void dfs(vector<NestedInteger>& nl, int lv, vector<int> &res) {
        if (res.size()<lv+1) res.resize(lv+1);
        for (auto n : nl) {
            if (n.isInteger()) {
                res[lv] += n.getInteger();
            } else {
                vector<NestedInteger> x = n.getList();
                dfs(x, lv+1, res);
            }
        }
        cout<<"lv:"<<lv<<" res[lv]:"<<res[lv]<<endl;
        return;
    }
};