# difficult way of solving, failed on 1st test as well
'''
import sys
n = sys.stdin.readline().split()[0]
tasks = [[0 for x in range(3) for y in range(n)]] 
row = 0
for line in sys.stdin:
    column = 0
    for word in line.split():
        tasks[row][column]
        column+=1
    row+=1
tasks_to_implement = 0
for task in tasks: 
    if sum(task) >= 2:
        tasks_to_implement +=1 
print(tasks_to_implement)
'''
#231A Codeforces 
#correct and full solution
'''
n = int(input())
tasks_to_implement = 0
for i in range(n):
    arr = [x for x in input().split()]
    if arr.count('1')>= 2:
        tasks_to_implement+=1
print(tasks_to_implement)
'''

#263A Codeforces
'''
n = 5 
for i in range(n):
    for j in range(n):
        matrix = [x for x in input().split()]
for a in range(n):
    index = matrix[a].find('1')
    if index != -1:
        print(abs(i-2)+abs(index-2))
        break
'''   

'''
mat = []
for r in range(5):
    mat.append(''.join(input().split()))
 
for i in range(5):
    index = mat[i].find('1')
    if index != -1:
        print(abs(i - 2)+abs(index - 2))
        break
'''
'''
arr = []
for row in range(5):
    arr.append(''.join(input().split()))
for i in range(5):
    index = arr[i].find('1')
    if index != -1:
        print(abs(i-2)+abs(index-2))
        break 
'''

#112 A
'''
string1 = input().lower()
string2 = input().lower()
if string1 == string2:
    print (0)
elif string1> string2 :
    print(1)
else:
    print(-1)
'''
#339 A
'''
string = input()
n1=n2=n3=0 
for i in range(0, len(string)):
    if string[i] == '1':
        n1+=1
    elif string[i] =='2':
        n2+=1
    elif string[i] == '3':
        n3+=1
result = '1+'*n1+'2+'*n2+'3+'*n3
print(result[:-1])
'''
#281 A
#tried myself,weir and long
'''string = input()
capitalized =[]
for i in range(0, len(string)):
    if string[i] == 0:
        capitalized.append(string[i].upper)
    else:
        capitalized.append(string[i])
print(capitalized)
'''
#correct one 
'''
string1 = input()
print(string1[0].upper() + string1[1:])
'''
# 236 A
#correct
'''
username = input()
unique = len(set(username))
if unique % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
'''
#266 A
#initial solution, not fully correct
'''
n = int(input())
stones = input()
unique = len(set(stones))
if n > unique:
    print(n-unique)
elif n == unique:
    print(0)
'''
#correct 
'''
n = int(input())
colors = input()
def colored_stones(n, colors):
    counter = 0 
    for i in range(0, len(colors)-1):
        if colors[i] == colors[i+1]:
            counter += 1
        else:
            continue
    return counter
print(colored_stones(n, colors))
'''
#791 A
#correct
'''
x,y = map(int, input().split())
counter = 0
while x <= y:
    x*=3
    y*=2
    counter+=1
print(counter)
'''

#546 A
'''
k,n,w = map(int, input().split())
total = k*(w*(w+1)//2)
if total > n:
    print(total -n)
else:
    print(0)
'''
#59 A
'''
word = input()
if sum(1 for char in word if char.isupper()) > sum(1 for char in word if char.islower()):
    print(word.upper())
else:
    print(word.lower())
'''
#997 A
'''
n, k = map(int,input().split())
#last_digit = int(repr(n)[-1])
for i in range(k):
    if n%10 == 0:
        n = n//10
    else:
        n=n-1
print(n)
'''
#110 A
'''
num = list(input())
happy_digits =["4","7"]
counter =0
for i in num:
    if i in happy_digits:
        counter+=1
if counter == 4 or counter ==7:
    print("YES")
else:
    print("NO")
'''
#116 A
'''
n = int(input())
res = 0
a = []
for i in range(n):
    temp = list(map(int, input().split()))
    res = res - temp[0]
    res += temp[1]
    a.append(res)
    ans= max(a)

print(ans)
'''
#486 A
'''
n = int(input())
if (n %2) ==0:
    print(int(n/2))
else:
    print(-int(n+1)//2)
'''
#200 B
'''
n = int(input())
drinks = list(map(int, input().split(" ")))
ans = sum(drinks)/n
print(ans)
'''

#61 A
'''
a = list(map(int, input()))
b = list(map(int, input()))
res = []
for i in range(len(a)):
    if a[i]!=b[i]:
        res.append(1)
    else:
        res.append(0)
    ans = ''.join(map(str,res))
print(ans)
'''
#734 A
'''
n = int(input())
s = input()
a = s.count('A')
d = s.count('D')
if a> d:
    print("Anton")
elif a< d:
    print("Danik")
else:
    print("Friendship")
'''
#41 A 
'''
s1 = input()
s2 = input()
if s1 == s2[::-1]:
    print("YES")
else:
    print("NO")
'''

#271 A
'''
year = int(input())+1
while len(set(str(year))) < 4:
    year+=1
print(year)
'''
#467 A
'''
n = int(input())
rooms = []
for i in range(n):
    a,b = map(int, input().split(" "))
    rooms.append([a,b])
counter = 0
for i in rooms:
    if (i[1]-i[0])>=2:
        counter+=1
print(counter)
'''
#1030 A
'''
n = int(input())
a = list(map(int, input().split()))
if a.count(1)>= 1:
    print("HARD")
else:
    print("EASY")
'''

#344 A 
'''
n = int(input())
counter = 1
a = [input() for i in range(n)]


#for i in range(0, n):
    #elements = str(input())
    #a.append(elements)

for j in range(n-1):
    if a[j]!= a[j+1]:
        counter+= 1
print(counter)
'''   
#705 A
'''
n = int(input())
l = " "
for i in range(1,n):
    if i % 2 == 0:
        l+="that I hate "
    else:
        l+="that I love "
print("I hate " + l + " it")
'''




#Codeforces contest Div.2 --> A
#from the way Muso agai solved

#PROBLEM:
'''
INPUT:
line 1--> number of operations to be performed 
line 2--> size of both arrays a and b
line 3--> array a and array b
LOGIC:
1. array a and b consist of 0s and 1s
2. we can perform only 2 operations on array a 
in order to make it the same as array b 
3. either {ith index of a} (ai) = 1- {ith index of i}(ai)
OR the array a can be rearranged the way we want 
--> as i understand, 0s in array a will be replaced with 1s
and vice versa 
4. we need to find minimum number of operations to perform 
so that the array a is identically similar to the array b
''' 

'''
for _ in range(int(input())):  #number of times to execute the program
    n = int(input()) # size of arrays 
    a = list(map(int, input().split(" "))) # accepting values for array a
    b = list(map(int, input().split(" "))) # accepting values for array b
    before = 0
    for i in range(n): #traversing through the arrays
       before += abs(a[i]-b[i]) #manhattan distance, dissimilarities in lists
    a.sort()
    b.sort()
    after = 0
    for i in range(n):
        after += abs(a[i]-b[i]) #manhattan distance, dissimilarities in lists 
    print(min(before, after+1))
'''


#148 A
'''
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
counter = 0
for i in range(1, d+1):
    if i%k != 0 and i%l!=0 and i%m!= 0 and i%n!= 0:
        counter+=1
print(d - counter)
'''

#1328 A
'''
n = int(input())
counter = 0
for i in range(n):
    arr = input().split(" ")
    a = int(arr[0])
    b = int(arr[1])
    if a%b == 0:
        print(0)
    else:
        print(b-(a%b))
'''
#520 A
'''
n = int(input())
word = input().lower()
alphbet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
for i in range(n):
    if word[i] in alphbet:
        print("YES")
    else:
        print("NO") 

'''
#520 A
'''
n = int(input())
word = input().lower()
result = ""
for i in word:
    if i not in result:
        result= result+i
if len(result)==26:
    print("YES")
else:
    print("NO")
'''
#443 A
'''
w = input()
result =""
for i in w:
    if i.isalpha():
        result = result+i
print(len(set(result)))
'''
#996 A
'''
n = int(input())
counter = 0
if n >= 100:
    counter += n//100
    n = n -100 *counter
if n>= 20:
    counter+=n//20
    n= n-20*(n//20)
if n>=10:
    counter+= n//10
    n= n-10*(n//10)
if n>= 5:
    counter+=n//5
    n = n-5*(n//5)
if n>=1:
    counter+=n
print(counter)
'''
#785 A
'''
n = int(input())
counter = 0
for _ in range(n):
    a = input()
    if a =="Tetrahedron":
        counter+=4
    elif a =="Cube":
        counter+=6
    elif a == "Octahedron":
        counter+=8
    elif a == "Dodecahedron":
        counter+=12
    elif a == "Icosahedron":
        counter+=20
print(counter)

'''
# 141 A
'''
a = input().upper()
b = input().upper()
c = input().upper()
combined = a+b
if sorted(combined) == sorted(c):
    print("YES")
else:
    print("NO")
'''
 






#Div 3--> A
'''

n = int(input())
for _ in range(1,n+1):
    k = int(input())
    arr = input()
    word = input()
    characters = dict(zip(arr,word))
    characters = set(characters.values())
    for i in arr:
        if i in characters:
            arr = arr.replace(i,characters[i])
            arr = arr.replace(" ","")
    if arr == word:
        print("YES")
    else:
        print("NO")
'''

'''    

    characters = {}
    for i, j in arr,word:
        characters[arr[i]]= word[j]
    for i in arr:
        if i in characters:
            arr = arr.replace(i,characters[i])
            arr = arr.replace(" ","")
    if arr == word:
        print("YES")
    else:
        print("NO")
'''

'''
for _ in range(n):
    for _ in arr:
        if arr.find('2'):
            new_arr = arr.replace('2','c')
        if arr.find('3'):
            new_arr = arr.replace('3','a')
        if arr.find('4'):
            new_arr = arr.replace('4','t')
        if arr.find('1'):
            new_arr = arr.replace('1','a')
print(n)
print(k)
print(arr)
print(new_arr)
'''
'''
arr = []
for _ in range(k):
    a = int(input())
    arr.append(a)
    arr = str(arr)
'''
'''
one =str(arr.find('1'))
two = str(arr.find('2'))
three = str(arr.find('3'))
four = str(arr.find('4'))
#word = input()
characters ={two:'c',
             three:'a',
             four:'t',
             one:'a',}
for _ in range(n):
        for key, value in characters.items():
            new_arr = arr.replace(key, value)
print(new_arr)
'''
# Div 3--> A //from Muso agai's method
'''
n = int(input())
for _ in range(n):
    k = int(input())
    a =list(map(int, input().split()))
    word = input()
    dictionary = {}
    ans = 1
    for i in range(k):
        if not dictionary.get(a[i]):
            dictionary[a[i]] = word[i]
        elif dictionary[a[i]]!= word[i]:
            ans*= 0
    if ans:
        print("YES")
    else:
        print("NO")
'''
#1335 A
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        print(a//2-1)
    else:
        print(a//2)
