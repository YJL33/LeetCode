/*
155. Min Stack

    Total Accepted: 93448
    Total Submissions: 375169
    Difficulty: Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
*/

public class MinStack {
    Stack<Integer> stk;
	Stack<Integer> minstk;
    /** initialize your data structure here. */
    public MinStack() {
		stk = new Stack<>();
		minstk = new Stack<>();
    }
    
    public void push(int x) {
        stk.push(x);
        if ((minstk.empty()) || (x <= minstk.peek())) {
        	minstk.push(x);
            //System.out.println("minstk push: " + minstk.peek());
        }
        //System.out.println("Now minstk: " + minstk.peek());
    }
    
    public void pop() {
        if ((stk.peek()-minstk.peek()==0)) {
            //System.out.println("minstk popout: " + minstk.peek());
        	minstk.pop();
        }
        stk.pop();
        //if (!minstk.empty()) { System.out.println("Now minstk: " + minstk.peek()); }
    }
    
    public int top() {
        return stk.peek();
    }
    
    public int getMin() {
        return minstk.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */