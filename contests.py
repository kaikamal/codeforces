
'''
from itertools import combinations_with_replacement
n = int(input())
for _ in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    b = [x for x in range(0,9) if x not in a ]
    comb = combinations_with_replacement(b,4)
    for i in list(comb):
        for j in i:
            if i.count(j)==1 and i.count(j)==3 and i.count(j)== 4 :
                continue
            
        print(i)


'''    
    
'''
    for comb in itertools.combinations(b, 4):
        new_list = [item for item in comb for i in range(2)]
        print(new_list)

'''
# A problem from Div.2 contest could be solved in following way, according to the Muso agai's solution 
import math
n = int(input())
for _ in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    print(math.comb(10-k, 2)* 6)
