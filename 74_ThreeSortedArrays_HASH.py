'''
Compare Three sorted arrays. Printout Instersection!
'''

from collections import Counter
class Solution:
    def sortedarrays(self,A,B,C):
        h1=Counter(A)
        h2=Counter(B)
        h3=Counter(C)
        s1=set()
        s2=set()
        s3=set()
        for key in h1:
            s1.add(key)
        for key in h2:
            s2.add(key)
        for key in h3:
            s3.add(key)
        intersect=list(s1.intersection(s2,s3))
        for i in intersect:
            if h1[i]==h2[i]==h3[i]:
                print(h1[i])
            else:
                print(min(h1[i],h2[i],h3[i]))
        
sol=Solution()
sol.sortedarrays([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120])
