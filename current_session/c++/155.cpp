#include <iostream>
#include <stack>

using namespace std;

// simply use 2 vector, to leverage dynamic size array
// push: put everything into snstt, if smaller than last element in mst, put into mst
// pop: pop nst, if equal to mst then pop mst
// top: return nst[-1]
// getMin: return mst[-1]

class MinStack {
 public:
  /** initialize your data structure here. */
  MinStack() {
  }
  
  void push(int val) {
    nStack.push(val);
    if (mStack.empty() || val <= mStack.top()) mStack.push(val);
    return;
  }
  
  void pop() {
    if (!mStack.empty() && nStack.top() == mStack.top()) mStack.pop();
    nStack.pop();
    return;
  }
  
  int top() {
    return nStack.top();
  }
  
  int getMin() {
    return mStack.top();
  }
 private:
  stack<int> mStack;
  stack<int> nStack;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

int main() {
  MinStack ms = MinStack();
  ms.push(1);
  ms.pop();

}