from tracemalloc import start


n = int(input())
strings = []
for i in range(n):
    for string in input().split():
        strings.append(string)
for string in strings:
    if len(string) > 10:
        print(string[0]+str(len(string)-2)+string[-1])
    else:
        print(string)