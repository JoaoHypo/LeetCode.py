'''
Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = dict()
        for letra in magazine:
            check[letra] = check.get(letra,0) + 1
        for letra in ransomNote:
            if letra not in check.keys():
                return False
            check[letra] = check.get(letra) -1 
            if check[letra] < 0:
                return False   
        return True
