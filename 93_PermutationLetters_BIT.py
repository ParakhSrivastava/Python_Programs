'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [""]
        for s in S:
            if s.isdigit():
                ans = [c+s for c in ans]
            else:
                tmp1 = [c+s.lower() for c in ans]
                tmp2 = [c+s.upper() for c in ans]
                ans = tmp1 + tmp2
        return ans
