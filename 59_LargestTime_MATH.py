'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
'''


from itertools import permutations as p
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perm=p([1,2,3,4])
        lis=[]
        st=""
        for i in perm:
            s = [str(j) for j in list(i)]
            res = int("".join(s)) 
            lis.append(res)
        maxi=0
        flag=0
        for i in lis:
            if i <= 2359 and i > maxi:
                flag=1
                maxi=i
        if flag==0:
            return ""
        else:
            st=str(maxi)        
            return (st[:2]+":"+st[2:])
