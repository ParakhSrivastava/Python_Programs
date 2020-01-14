'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        mapping = {u: l for l, u in zip('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        
        res = []
        for s in str:
            res.append(mapping[s] if s in mapping else s)
        
        return ''.join(res)
