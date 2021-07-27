#include <iostream>
#include <string>
#include <map>

using namespace std;

class Logger {
public:
  /** Initialize your data structure here. */
  map<string, int> msgMap;
  Logger() {
  }
  
  /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
      If this method returns false, the message will not be printed.
      The timestamp is in seconds granularity. */
  bool shouldPrintMessage(int timestamp, string message) {
    if (msgMap.find(message) != msgMap.end() && msgMap[message]+10 > timestamp) return false;
    msgMap[message] = timestamp;
    return true;
  }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */