#include <string>
#include <iostream>
#include <string>
#include <map>

using namespace std;

// simply use a map to store the conversion
// for each long URL, generate random string and use it as key
class Solution {
public:

  // Encodes a URL to a shortened URL.
  string encode(string longUrl) {
    counter += 1;
    string shortUrl = to_string(counter);
    urlMap[shortUrl] = longUrl;
    return shortUrl;
  }

  // Decodes a shortened URL to its original URL.
  string decode(string shortUrl) {
    return urlMap[shortUrl];
  }

private:
  int counter = 0;
  map<string, string> urlMap;
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));