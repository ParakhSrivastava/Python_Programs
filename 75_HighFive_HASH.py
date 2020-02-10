'''
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
The average score is calculated using integer division.

Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
'''

class Solution:
    def highfive(self,items):
        dic={}
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]]=[item[1]]
        result=[]
        for key,value in dic.items():
            value.sort(reverse=True)
            if len(value)>5:
                val=value[:5]
            else:
                val=value
            dic[key]=sum(val)/len(val)
            result.append([key, dic[key] ])
        print(result)
sol=Solution()
sol.highfive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
