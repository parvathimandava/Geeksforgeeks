'''
Given a positive integer N, find the Nth Even Fibonacci number. Since the answer can be very large, print the answer modulo 1000000007.

Input:
The first line of input contains T denoting the number of testcases.Then each of the T lines contains a single positive integer N.

Output:
Output the Nth Even Fibonacci number.

Constraints:
1 <= T <= 200
1 <= N <= 1000

Example:
Input:
3
1
2
5
Output:
2
8
610
'''
t=int(input())
for i in range(t):
    n=int(input())
    count=0
    x=1
    y=1
    z=0
    while(count!=n):
        z=x+y
        x=y
        y=z
        if(z%2==0):
            count=count+1
            result=z%1000000007
    print(result)