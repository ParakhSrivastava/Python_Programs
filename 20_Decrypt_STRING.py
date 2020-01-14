'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
'''

class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        ascii_of_a = ord('a')
        
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == '#':
                diff = int(s[i-2:i]) - 1
                i = i - 3
            else:
                diff = int(s[i]) - 1
                i = i - 1
            
            res = chr(ascii_of_a + diff) + res

        
        return res
