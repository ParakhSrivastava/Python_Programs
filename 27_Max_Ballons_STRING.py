'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
    
        for i in range(len(text)):
            if text[i] in d:
                d[text[i]]+=1
            else:
                d[text[i]]=1

        compare='balon'
        result=len(text)

        for i in range(len(compare)):
            if compare[i] in d:
                if compare[i]=='l' or compare[i]=='o':
                    result=min( result,  d[compare[i]]//2)        
                else:
                    result=min( result,  d[compare[i]])
            else:
                return 0 

        return result
