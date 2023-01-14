'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = dict()
        auxlist = [x for x in strs]
        for word in strs:
            auxlist = [x for x in auxlist if x != word]
            for w in auxlist:
                prefixletters = ''
                for ind,l in enumerate(w):
                    if word[ind] == l:
                        prefixletters = prefixletters + l
                    else:
                        break
                prefix[prefixletters] =  prefix.get(prefixletters,0) + 1
        mostreps = 0
        for pref,reps in prefix.items():
            if reps > mostreps:
                mostreps = reps
                mostcommon = pref

        return mostcommon

strs = ["flower","flow","flight"]

expectedRes = 'fl'

teste = Solution()

print(teste.longestCommonPrefix(strs))

assert teste.longestCommonPrefix(strs) == expectedRes , "False"
