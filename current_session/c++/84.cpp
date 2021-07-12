#include<iostream>
#include <vector>
#include <stack>

using namespace std;

// brute force(?) try all l & r
// time complexity: O(n^3)
// go through the arr
// if increasing, keep add into stack
// if not, pop it out until current height is max height.
// calculate the height while poping out
// time complexity: O(n)

class Solution {
public:
  int largestRectangleArea(vector<int>& heights) {
    int maxSeenRecArea = 0;
    stack<int> st;        // store the index
    heights.push_back(0);
    int m = heights.size();
    int zeroIndex = -1;// handle edge case

    for (int i=0; i<m; ++i) {
      while (!st.empty() && heights[i] < heights[st.top()]) {             // handle edge case 
          int h = heights[st.top()];
          st.pop();
          int prevI = st.empty() ? zeroIndex : st.top();
          int w = i-(prevI+1);   // carefully calculate the rectangle in histogram
          // cout<<"H:"<<h<<"   W:"<<w<<endl;
          maxSeenRecArea = max(maxSeenRecArea, h*w);
        }
        st.push(i);
    }
    return maxSeenRecArea;
  }
};