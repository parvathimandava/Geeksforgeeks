'''
Given a MxN matrix, count the number of squares in the matrix.squaresinREct


Input:

The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two space seperated integers M and N, denoting the size of the Matrix.
Output:

For each test output a single integer denoting the total number of squares.
Constraints:

1 <= T <= 102
1 <= M,N <= 104

Example:

Input:

2
2 2
4 3

Output:

5
20
'''
import math
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if (n<m):
        temp=n
        n=m
        m=temp
    squares=math.ceil((m*(m+1)*(2*m+1)/6)+(n-m)*m*(m+1)/2)
    print(squares)