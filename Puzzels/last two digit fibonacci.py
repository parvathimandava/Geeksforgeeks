'''
Somedays ago Leeana Learned about Fibonacci Number and then her uncle gave her a task. The task is to find the last two digits of nth Fibonacci number. The Fibonacci number sequence are: 0 1 1 2 3 5 8 13 21....... (0 based indexing)
Note: Incase the fibonacci number is a single digit number print it with appending a 0 at its front ie for no 2 print 02.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer n.

Output:
For each test case print the required answer in a new line.

Constraints:
1 <= T <= 100
0 <= n <= 1018

Example:
Input:
2
0
7
Output:
00
13
'''
t=int(input())
for _ in range(t):
    n=int(input())
    x=1
    y=1
    z=0
    count=0
    result=0
    while(count!=n):
        z=x+y
        y=z
        x=y
        if(z%2==0):
            count+=1
            result=z%10000007
    num=str(result)
    if(len(num)==1):
        num='0'+num
        print(num)
    elif(len(num)==2):
        num=num
        print(num)
    elif(len(num)>=3):
        num=num[-2:]
        print(num)

