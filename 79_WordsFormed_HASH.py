'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''


from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_chars = Counter(chars)
        result = 0
        
        for word in words:
            for key, item in Counter(word).items():
                if key not in total_chars or item > total_chars[key]:
                    break
            else:
                result += len(word)
        return result
