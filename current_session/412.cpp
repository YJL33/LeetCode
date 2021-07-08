#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        // simply add everything into the vector
        vector<string> res;
        for (int i = 1; i < n+1; i++) {
            string tmp = "";
            if (i%3 == 0) tmp = "Fizz";
            if (i%5 == 0) tmp = tmp + "Buzz";
            if (tmp=="") tmp = to_string(i);
            res.push_back(tmp);
            // cout << "size:" << res.size() << endl;
        }
        return res;
    }
};

int main() {
    vector<string> ans1 = Solution().fizzBuzz(15);
    for (int i = 0; i < ans1.size(); i++) cout << ' ' << ans1.at(i);
    cout << endl;
    vector<string> ans2 = Solution().fizzBuzz(10);
    for (int i = 0; i < ans2.size(); i++) cout << ' ' << ans1.at(i);
    cout << endl;
    vector<string> ans3 = Solution().fizzBuzz(5);
    for (int i = 0; i < ans3.size(); i++) cout << ' ' << ans1.at(i);
    cout << endl;
    vector<string> ans4 = Solution().fizzBuzz(3);
    for (int i = 0; i < ans4.size(); i++) cout << ' ' << ans1.at(i);
    cout << endl;
}