
n = int(input())
x = 0
for _ in range(n):
    user_input = input()

    if "++" in user_input:
        x=x+1
    else:
        x=x-1

print(x)