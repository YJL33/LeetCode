#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;
class Solution {
public:
    vector<vector<int> > highFive(vector<vector<int> >& items) {
        // put everything into a map: key=user, value=scores
        map<int, vector<int> > userScoreMap;
        for (int i=0; i < items.size(); i++) {
            int user = items[i][0];
            int score = (-1)*items[i][1];
            userScoreMap[user].push_back(score);
        }
        vector<vector<int> > res;
        // vector<vector<int> > res(userScoreMap.size());
        // int i = 0;
        // for each user, calculate his/her high five
        for (auto it : userScoreMap) {
            vector<int> v = it.second;
            sort(v.begin(), v.end());
            if (v.size() > 5) v.resize(5);
            int sum=0, cnt=0;
            for (int i=0; i<v.size(); i++) {
                sum = sum + v[i];
                cnt = cnt+1;
            }
            res.push_back({it.first, -1*sum/cnt});
            // res[i].push_back(it.first);
            // res[i].push_back(-1*sum/cnt);
            // i++;
        }
        return res;
    }
};

int main() {
    vector<vector<int> > vect(11);
    // vect[0].push_back(1);
    // vect[0].push_back(100);
    // vect[1].push_back(7);
    // vect[1].push_back(100);
    // [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    vect[1].push_back(1);
    vect[1].push_back(91);
    vect[2].push_back(1);
    vect[2].push_back(92);
    vect[3].push_back(2);
    vect[3].push_back(93);
    vect[4].push_back(2);
    vect[4].push_back(97);
    vect[5].push_back(1);
    vect[5].push_back(60);
    vect[6].push_back(2);
    vect[6].push_back(77);
    vect[7].push_back(1);
    vect[7].push_back(65);
    vect[8].push_back(1);
    vect[8].push_back(87);
    vect[9].push_back(1);
    vect[9].push_back(100);
    vect[10].push_back(2);
    vect[10].push_back(100);
    vect[0].push_back(2);
    vect[0].push_back(76);
    for (int i=0; i<vect.size(); i++) {
        cout<<"i:"<<i<<" 0:"<<vect[i][0]<<endl;
        cout<<"i:"<<i<<" 1:"<<vect[i][1]<<endl;
    }
    vector<vector<int> > ans = Solution().highFive(vect);
    for (int i=0; i<ans.size(); i++) {
        cout<< ans.at(i).at(0)<< ans.at(i).at(1);
    }
}