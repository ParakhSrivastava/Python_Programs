'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
'''
class Solution:
    def divisorGame(self, N: int) -> bool:
        l = [False]*(N+1)
        for i in range(2,N+1):
            t = [l[i-j] for j in range(1,i) if i%j==0]
            l[i] = not all(t)      
        return l[N]
