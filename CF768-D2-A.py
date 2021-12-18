n = int(input())
arr = list(map(int, input().split()))
print(max(0, n - arr.count(max(arr)) - arr.count(min(arr))))
