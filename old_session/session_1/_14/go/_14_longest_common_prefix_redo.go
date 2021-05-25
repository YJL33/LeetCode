package main

import "fmt"

// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
// Note:

// All given inputs are in lowercase letters a-z.
func longestCommonPrefix(strs []string) string {
    // binary search
    
}

func main() {
    testCases := [][]string{
        {"flower","flow","flight"},
        {"dog","racecar","car"},
        {"a"}
    }
    for _, test := range testCases {
        res := longestCommonPrefix(test)
        fmt.Println(res)
    }
}