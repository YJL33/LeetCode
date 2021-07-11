#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
 public:
  vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
    // 1st pass: change the click into 'X' if it's mine
    // 2nd pass: dfs, count its nbs
    // and stop searching when we hit "digits"

    if (board[click[0]][click[1]] == 'M') {
      // modify the place to 'X', return
      board[click[0]][click[1]] = 'X';
      return board;
    }

    dfs(click[0], click[1], board);
    return board;
  }
 private:

  bool valid(int i, int j, const vector<vector<char>>& board) {
    return (0<=i && i<board.size() && 0<=j && j<board[0].size());
  }

  // click the point
  // if blank: check its 8 nbs
  // if number: simply change the board to number
  void dfs(int i, int j, vector<vector<char>>& board) {
    // only handle inbound unrevealed squares
    if (valid(i,j,board) && board[i][j] == 'E') {
      // count the nbs
      int cnt = 0;
      if (valid(i-1,j+1,board) && board[i-1][j+1] == 'M') cnt += 1;
      if (valid(i-1,j-1,board) && board[i-1][j-1] == 'M') cnt += 1;
      if (valid(i+1,j+1,board) && board[i+1][j+1] == 'M') cnt += 1;
      if (valid(i+1,j-1,board) && board[i+1][j-1] == 'M') cnt += 1;
      if (valid(i-1,j,board) && board[i-1][j] == 'M') cnt += 1;
      if (valid(i+1,j,board) && board[i+1][j] == 'M') cnt += 1;
      if (valid(i,j-1,board) && board[i][j-1] == 'M') cnt += 1;
      if (valid(i,j+1,board) && board[i][j+1] == 'M') cnt += 1;
      
      // either blank or digit
      if (cnt == 0) {
        board[i][j] = 'B';
        dfs(i-1,j+1,board);
        dfs(i-1,j-1,board);
        dfs(i+1,j+1,board);
        dfs(i+1,j-1,board);
        dfs(i-1,j,board);
        dfs(i+1,j,board);
        dfs(i,j-1,board);
        dfs(i,j+1,board);
      } else {
        board[i][j] = '0'+cnt;
      } 
    }
    return;
  }
};