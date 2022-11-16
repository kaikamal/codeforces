#
'''
n = int(input())
p = list(map(int, input().split(" ")))
q = list(map(int,input().split(" ")))
a = p[1:]+q[1:]
b = set(a)
counter = 0
for i in range(1, n+1):
    if i in b:
        counter +=1
if counter == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
'''

'''
n = int(input())
arr = 0
for i in range(n):
    a, b, c = (map(int, input().split(" ")))
    arr.append([a,b,c])
    
print(arr)
'''


'''

n = int(input())
for _ in range(n):
    a,b,c = map(int, input().split(" "))
    
    if a == b + c or b == a+c or c ==b+a:
        print("YES")
    else:
        print("NO")
'''


'''
print(arr)
'''



'''
n =int(input())
for _ in range(n):
    L = int(input())
    arr = [x for x in input().split()]
    unique = set(arr)

    if len(unique) < L:
        print("NO")
    else:
        print("YES")
'''

'''
n = int(input())
arr = []
for _ in range(n):
    l = input()
    m = [list(input()) for i in range(8)]
    if m.count('R') > count('B'):
        print("R")
    else:
        print("B")
'''
# probalem C --> Div.4 
from sys import stdin
n = int(input())
lines = stdin.read().split()
a = 0
for ele in range(n):
    for i in range(8):
        if lines[i+a].count('R') == 8:
            print('R')
            break
        else:
            print('B')
    a+=8



        

