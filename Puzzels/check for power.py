'''
Given two positive numbers x and y, check if y is a power of x or not.

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain two positive numbers x and y.

Output:
Print 1 if y is a power of x, else print 0.

Constraints:
1 <= T <= 30
1 <= x <= 103
1 <= y <= 108

Example:
Input:
2
2 8
1 3
Output:
1
0
'''
import math
t=int(input())
for i in range(t):
    x,y=[int(i) for i in input().split(" ") if i]
    if(x!=0 or x!=1 or y!=0):
        try:
            p=math.log(y,x)
            q=int(p)
            if(q-p==0):
                print(1)
            else:
                print(0)
        except ZeroDivisionError:
            print(0)