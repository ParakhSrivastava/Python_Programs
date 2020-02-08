'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
'''

from collections import defaultdict
class Solution:
    def hasGroupsSizeX(self, deck):
        dic=defaultdict(int)
        for i in deck:
            dic[i]+=1
        flag=0
        c=0
        b=0
        for k, v in dic.items():
            b+=1
            if dic[deck[0]]==v:
                c+=1
        if b==c and dic[deck[0]]>=2:
            return "true"
        else:
            return "false"
