'''
For an integer n find number of trailing zeroes in n! .

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, it contains an integer 'N'.

Output:
In each seperate line output the answer to the problem.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
1
9
Output:
1
'''
import math
for _ in range(int(input())):
    n=int(input())
    s=math.factorial(n)
    s=str(s)
    s=s[::-1]
    j=0
    for i in s:
        if int(i)>0:
            break
        j+=1
    print(j)

