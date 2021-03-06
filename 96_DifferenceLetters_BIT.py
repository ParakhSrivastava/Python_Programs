'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:        
        t = list(t)
        s = list(s)
        
        for i in s:
            t.remove(i)
        return t[0]            
