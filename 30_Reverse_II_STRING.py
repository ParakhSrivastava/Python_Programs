'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
'''

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        
        i = 0
        j = len(S) - 1
        l = list(S)
        while i < j:
            if l[i].isalpha() and l[j].isalpha():
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            
            if not l[i].isalpha():
                i += 1
            if not l[j].isalpha():
                j -= 1
        return ''.join(l)
