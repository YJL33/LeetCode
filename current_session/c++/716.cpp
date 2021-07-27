#include <iostream>
#include <vector>

using namespace std;

// simply use a vector (to simulate stack)
// store pair(value, index of maxSeen)

class MaxStack {
public:
  /** initialize your data structure here. */
  vector<pair<int,int>> st;
  MaxStack() {
  }
  
  void push(int x) {
    if (st.empty()) {
      st.push_back(pair<int,int>{x, 0});
    } else if (x >= st[st[st.size()-1].second].first) {         // a new maxSeen
      st.push_back(pair<int,int>{x,st.size()});
    } else {
      st.push_back(pair<int,int>{x,st[st.size()-1].second});    // maxSeen is same
    }
    // cout << "push chk" << endl;
    // for_each(st.begin(), st.end(), [](auto x){cout << "1st: " << x.first << " 2nd: " << x.second << endl;});
  }
  
  int pop() {
    int tmp = st[st.size()-1].first;
    st.pop_back();
    return tmp;
  }
  
  int top() {
    // cout << "top chk" << endl;
    // for_each(st.begin(), st.end(), [](auto x){cout << "1st: " << x.first << " 2nd: " << x.second << endl;});
    return st[st.size()-1].first;
  }
  
  int peekMax() {
    // cout << "peekMax chk" << endl;
    // for_each(st.begin(), st.end(), [](auto x){cout << "1st: " << x.first << " 2nd: " << x.second << endl;});
    int maxIndex = st[st.size()-1].second;
    return st[maxIndex].first;
  }
  
  int popMax() {
    int maxIndex = st[st.size()-1].second;    // all elements after maxIndex needs to be updated

    int cur = st.size()-1;
    vector<int> toHandle;                     // pop them out first, handle them later
    while (cur > maxIndex) {
      toHandle.push_back(st[cur].first);
      st.pop_back();
      cur--;
    }
    
    int tmp = st[maxIndex].first;             // max
    st.pop_back();                            // pop max out

    while (!toHandle.empty()) {               // simply push these elements back
      int x = toHandle[toHandle.size()-1];
      toHandle.pop_back();
      push(x);
    }
    return tmp;
  }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */

int main() {
}