'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
'''

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freq_q = []
        for word in queries:
            mini = ord('z')+1
            count=0
            for i in word:
                if ord(i)<mini:
                    mini = ord(i)
            for i in word:
                if mini == ord(i):
                    count+=1
            freq_q.append(count)
        freq_w = []
        mini = ord('z')+1
        for word in words:
            mini = ord('z')+1
            count=0
            for i in word:
                if ord(i)<mini:
                    mini = ord(i)
            for i in word:
                if mini == ord(i):
                    count+=1
            freq_w.append(count)
        result=[]
        for i in freq_q:
            count=0
            for j in freq_w:
                if i<j:
                    count+=1
            result.append(count)
        return result
