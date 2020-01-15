'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        word1= []
        for word in st:
            word1.append(word[::-1])
        return ' '.join(word1)
