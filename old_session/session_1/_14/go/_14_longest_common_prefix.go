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
    // fmt.Printf("strs: %v\n", strs)
    if len(strs) == 0 {
        return ""
    }
    i, res, isComplete := 0, "", false
    for (!isComplete) && i < len(strs[0]) {
        char := string(strs[0][i])
        // fmt.Println("char: ", char)
        for _, s := range strs[1:] {
            if i >= len(s) || string(s[i]) != char {
                isComplete = true
                return res
            }
        }
        res = res + char
        i = i+1
    }
    return res
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