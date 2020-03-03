'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        counts=[None]+[0]*N
        for truster,trusted in trust:
            counts[trusted]+=1
            counts[truster]=-1
        for i,count in enumerate(counts):
            if count==N-1:
                return i
        return -1
'''
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust: return 1
        graph = collections.defaultdict(set)
        trust_list = set()
        
        for a,b in trust:
            graph[b].add(a)
            trust_list.add(a)
           
        res = list(set(i for i in range(1,N+1)) - trust_list)    
        if not res:
            return -1
        judge = [k for k,v in graph.items() if k in res and len(v) == N-1]
        
        if len(judge) == 1:
            return judge[0]
        else:
            return -1
'''
