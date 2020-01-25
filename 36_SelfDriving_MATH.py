'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        sdn = []
        
        for i in range(left,right+1):
            nums.append(i)
            
        for i in range(len(nums)):
            if nums[i]<10 and nums[i]!=0:
                sdn.append(nums[i])
            else:
                num = str(nums[i])
                if '0' in num:
                    continue
                else:
                    flag=0
                    num = nums[i]
                    while(num!=0):
                        d = num%10
                        if nums[i]%d==0:
                            flag=1
                        else:
                            flag=0
                        num=num//10
                        if flag==0:
                            break
                    if flag==1:
                        sdn.append(nums[i])
        return sdn
