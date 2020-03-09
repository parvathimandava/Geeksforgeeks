'''
Write a program that calculates the day of the week for any particular date in the past or future.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of one line. The first line of each test case consists of an integer d,m and y, d is day, m is month and y is the year.

Output:
Print day of given date.

Constraints:
1 <= T <= 100
1 <= d <= 31
1 <= m <= 12
1990 <= Y <= 2100

Example:
Input:
2
28 12 1995
30 8 2010
Output:
Thursday
Monday
'''
# weeday using dictionary concept and taking keys using values
import calendar
t=int(input())
for _ in range(t):
    d,m,Y=map(int,input().split())
    weekday=calendar.weekday(Y,m,d)
    dict={'Monday':0, 'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
    key_list = list(dict.keys())
    val_list = list(dict.values())

    print(key_list[val_list.index(weekday)])

#pragram using datetime
'''
import datetime
t = int(input())
for _ in range(t):
    d,m,y = map(int,input().split(" "))
    week = datetime.date(y,m,d)
print(week.strftime("%A"))
'''