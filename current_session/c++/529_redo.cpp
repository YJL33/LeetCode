#include <iostream>
#include <vector>

using namespace std;

// simply use dfs
// check whether it's bombed or not, return board with 'X' if bombed
// if not, check its neighbors and count bomb.
// in DFS, we usually need to track visited or not
// but here we can first check whether its unrevealed or not, and is inbound or not.
// if 0 then check 8 nbs
// if any return digit

class Solution {
 public:
  vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
    if (board[click[0]][click[1]] == 'M') {
      board[click[0]][click[1]] = 'X';
      return board;
    } else {
      dfs(click[0], click[1],board);
      return board;
    }
  }
 private:
  bool isValid(int x, int y, const vector<vector<char> >& board) {
    return (0<=x && x<board.size() && 0<=y && y<board[0].size());
  }
  void dfs(int x, int y, vector<vector<char> >& board) {
    if (isValid(x,y,board) && board[x][y] == 'E') {
      // cnt nbs
      int cnt = 0;
      if (isValid(x+1,y+1,board) && board[x+1][y+1] == 'M') cnt += 1;
      if (isValid(x+1,y-1,board) && board[x+1][y-1] == 'M') cnt += 1;
      if (isValid(x-1,y+1,board) && board[x-1][y+1] == 'M') cnt += 1;
      if (isValid(x-1,y-1,board) && board[x-1][y-1] == 'M') cnt += 1;
      if (isValid(x+1,y,board) && board[x+1][y] == 'M') cnt += 1;
      if (isValid(x-1,y,board) && board[x-1][y] == 'M') cnt += 1;
      if (isValid(x,y+1,board) && board[x][y+1] == 'M') cnt += 1;
      if (isValid(x,y-1,board) && board[x][y-1] == 'M') cnt += 1;
      // blank, dfs 8 nbs
      if (cnt==0) {
        board[x][y] = 'B';
        dfs(x+1,y+1,board);
        dfs(x+1,y-1,board);
        dfs(x-1,y+1,board);
        dfs(x-1,y-1,board);
        dfs(x+1,y,board);
        dfs(x-1,y,board);
        dfs(x,y+1,board);
        dfs(x,y-1,board);
      } else {
        board[x][y] = '0' + cnt;
      }
   }
 }
};