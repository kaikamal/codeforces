#155A Codeforces
'''
n= int(input())
points = list(map(int, input().split()))
counter = 0
for i in range(1, n):
    highest_counter = 0
    lowest_counter = 0
    for a in range(0, i):
        if points[i]> points[a]:
            highest_counter+=1
        elif points[i]<points[a]:
            lowest_counter+=1
    if highest_counter==i or lowest_counter==i:
        counter+=1
print(counter)
'''

#510 A 
'''
a, b = map(int, input().split())
p = b-1
for i in range(a):
    for j in range(b):
        if i%2 == 0:
            print('#', end='')
        else:
            if j == p:
                print('#', end='')
            else:
                print('.', end='')
    if i%2!=0:
        if p == b-1:
            p=0
        else:
            p=b-1
    print()
'''

#427 A
'''
n = int(input())
a = list(map(int, input().split()))
unsolved_cases = 0
new_police_officer = 0
for i in range(len(a)):
    if a[i]> 0:
        new_police_officer+=a[i]
    else:
        if new_police_officer+a[i]>=0:
            new_police_officer-=1
        else:
            unsolved_cases+=1
print(unsolved_cases)
'''

#750 A
'''
n, k = map(int, input().split())
time_remaining = (240-k)//5
max = 240
for i in range(1, max):
    time_remaining-=i
    if time_remaining<0:
        a = i
        break
if (a-1)> n:
    print(n)
else:
    print(a-1)
'''
#581 A
'''
a, b = map(int, input().split())
different = min(a, b)
same = abs(a-b)//2
print(different, same)
'''

#Yandex training contest, 1 problem
#was correct!
'''
s = input()
j = input()
counter = 0
for x in j:
    if x in s:
        counter+=1
print(counter)
'''

#2 problem
'''
n = int(input())
for _ in range(n):
'''

#div 2, problem 2
#havent solved fully 
'''
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
'''

#1352 A
'''
n = int(input())
for _ in range(n):
    a = input()
    l = []
    for i in range(len(a)):
        if a[i]!="0":
            l.append(a[i]+"0"*(len(a)-1-i))
    print(len(l))
    print(" ".join(l))
'''
#Codeforces div1 & div2 contest 06/11/2022
# problem A
# not solved fully
'''
import random
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sorted(a) == a:
        print("Yes")
    else:
        for i in range(n):
            lst = random.sample(a, k=3)
            if lst[i]> lst[-1]:
                lst[i]+=lst[i+1]
            else:
                temp = lst[i+1]
                lst[i+1] = lst[-1]
                lst[-1] = temp
        if sorted(a) == a:
            print("Yes")
        else:
            print("No")
'''

#problem A could be solved in much easier way
'''
n = int(input())
for _ in range(n):
    a = int(input())
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        print("Yes")
    else:
        print("No")
'''
#problem B 
'''
n = int(input())
for _ in range(n):
    a = int(input())
    s = input()
    x = s.count("0")
    y = s.count("1")
    if x>0 and y>0:
        print(x*y)
    elif x>0 and y==0:
        print(x*x)
    elif x==0 and y>0:
        print(y*y)
'''  
#problem B was solved using Collections module 
'''
import collections
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = input()[:-1]
    d = collections.Counter(a) 
    ones = max(a.split("0"), key = lambda x: len(x))
    zeros = max(a.split("1"), key= lambda x: len(x))
    if n == 1:
        print(1)
    else:
        print(max(len(ones)**2,len(zeros)**2,d['0']*d['1']))
'''
#1154 A
mat = list(map(int, input().split()))
mat.sort()
a = mat[-1]-mat[0]
b = mat[-1]-mat[1]
c =mat[-1]-mat[2]
print(a,b,c)
        


