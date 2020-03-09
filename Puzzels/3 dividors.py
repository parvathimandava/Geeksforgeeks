'''
Given a value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

Input:
The first line contains integer T, denoting number of test cases. Then T test cases follow. The only line of each test case contains an integer N.

Output :
For each testcase, in a new line, print the answer of each test case.

Constraints :
1 <= T <= 103
1 <= N <= 1012

Example:
Input :
3
6
10
30
Output :
1
2
3

Explanation:
Testcase 1: There is only one number 4 which has exactly three divisors 1, 2 and 4.
'''

def numbersWith3Divisors(n):
    prime = [True] * (n + 1);
    prime[0] = prime[1] = False;
    p = 2;
    count=0
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

        # print squares of primes upto n.
    print("Numbers with 3 divisors :");
    i = 0;
    while (i * i <= n):
        if (prime[i]):
            count+=1
            print(i * i, end=" ");

        i += 1;
    print(count)
# driver program
t=int(input())
for _ in range(t):
    n = int(input());
    numbersWith3Divisors(n);
