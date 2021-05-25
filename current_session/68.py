"""
68. Text Justification

Given an array of words and a width maxWidth,
format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text,
it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        remainingWidth = maxWidth
        r = 0
        row = {}        # words to add in each row
        row[0] = []

        res = []

        # iteratively check the maxWidth
        for i in xrange(len(words)):
            widthUsing = len(words[i]) + 1

            if remainingWidth == maxWidth:              # correct usage for initial word in row
                widthUsing -= 1

            if (remainingWidth - widthUsing) >= 0:      # keep staying in this row
                remainingWidth -= widthUsing
                row[r] += i,
            else:                                       # next row, add the substring into output
                r += 1
                remainingWidth = maxWidth - len(words[i])
                row[r] = [i]

        # generate row by row, we can combine in the previous section but put them here for readability
        for r in xrange(len(row)-1):
            if len(row[r]) == 1:        # corner case
                numOfSpaces = maxWidth - len(words[row[r][0]])
                substring = words[row[r][0]] + ''.join(numOfSpaces * ' ')
                res += substring,
            else:
                remainingWidth = maxWidth - sum([len(words[w]) for w in row[r]])
                gaps = [0] * (len(row[r])-1)
                i, numOfGaps = 0, len(gaps)
                while remainingWidth > 0:
                    gaps[i], i = gaps[i]+1, (i+1)%numOfGaps
                    remainingWidth -= 1
                wds, spaces = [words[i] for i in row[r]], [''.join(gaps[j] * ' ') for j in xrange(len(gaps))]
                substring = ''.join(i+j for i,j in zip(wds, spaces)) + words[row[r][-1]]
                res += substring,

        # handle last row individually
        lastRow = ' '.join([words[i] for i in row[len(row)-1]])
        lastRow = lastRow + ''.join((maxWidth-len(lastRow))*' ')
        res += lastRow,

        return res



print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)




"""
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Accepted 132.7K
Submissions 489.3K
"""