'''
Given a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. You are given a number N, you have to print the number of integers less than N in the sample space S.

Input :
The first line contains an integer T, denoting the number of test cases.Then T test cases follow. The first line of each test case contains an integer N, denoting the number.

Output :
Print the answer of each test case in a new line.

Constraints :
1<=T<=100
1<=N<=10^18

Example
Input :
2
9
3

Output :
2
1
'''
import math
t=int(input())
for _ in range(t):
    n=int(input())
    flag=1
    res=math.sqrt(n)
    l=str(res).split('.')
    for i in l[1]:
        if i!='0':
            flag=0
    if flag:
        ceel=int(l[0])
    else:
        ceel=int(l[0])+1
    print(ceel-1)