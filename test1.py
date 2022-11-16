#n = int(input())
L = int(input())
arr = input()
arr1 = []
k= list(map(int, arr.split(' ')))
arr[0] = arr1[0]
for i in range(0, L):
    arr1[i] = arr[i]+arr[i-1]

print(arr1)

