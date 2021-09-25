#include <iostream>
#include <string>
#include <vector>

using namespace std;

// bfs
// or simply go to the target (?)
// clang++ -std=c++17 c++/1138.cpp -o 1138 && ./1138 -v 
class Solution {
public:
  string alphabetBoardPath(string target) {
    vector<string> res;
    char prev = 'a';
    for (int i = 0; i < target.size(); ++i) {
      string moves = finder(prev, target[i]);
      res.push_back(moves);
      prev = target[i];
    }
    string ans = "";
    for (int i = 0; i < res.size(); ++i) {
      ans += res[i];
    }
    return ans;
  }

private:
  string finder(char prev, char tgt) {
    if (prev == tgt) {
      return "!";
    }
    string moves = "";
    pair<int, int> start = getCoord(prev);
    pair<int, int> end = getCoord(tgt);
    int y1 = start.first;
    int x1 = start.second;
    int y2 = end.first;
    int x2 = end.second;
    // cout << "prev: " << prev << x1 << y1 << endl;
    // cout << "tgt:  " << tgt << x2 << y2 << endl;

    while (y1 > y2) {
      moves.push_back('U');
      y1 -= 1;
    }
    while (x1 > x2) {
      moves.push_back('L');
      x1 -= 1;
    }
    while (y1 < y2) {
      moves.push_back('D');
      y1 += 1;
    }
    while (x1 < x2) {
      moves.push_back('R');
      x1 += 1;
    }
    return moves + "!";
  }

  pair<int, int> getCoord(char x) {
    vector<string> board = {"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z####"};
    for (int i = 0; i < board.size(); ++i) {
      for (int j = 0; j < board[0].size(); ++j) {
        if (board[i][j] == x) {
          return pair<int, int>{i,j};
        }
      }
    }
    cout << "???" << endl;
    return pair<int, int>{0,0};
  }
};

int main() {
  string test1 = "leet";
  string test2 = "code";
  cout << Solution().alphabetBoardPath(test1) << endl;
  cout << Solution().alphabetBoardPath(test2) << endl;
}