'''
Check whether the number is Triangular or not. A number is termed as triangular number if we can represent it in the form of triangular grid of points such that the points form an equilateral triangle and each row contains as many points as the row number, i.e., the first row has one point, second row has two points, third row has three points and so on. The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the number to be checked if it is traingular or not.

Output:
If the number is Triangular then display 1 otherwise 0.

Constraints:
1 <= T <= 100
1 <= N <= 107

Example:
Input:
5
3
4
6
55
345

Output:
1
0
1
1
0
'''
for _ in range(int(input())):
    n = int(input())
    flag = 0

    for i in range(n + 1):
        equation = ((i ** 2) + i - (2 * n))
        if equation == 0:
            flag = 1
            print(1)

        elif equation > 0:
            break
    if flag == 0:
        print(0)