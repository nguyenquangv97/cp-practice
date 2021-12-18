n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(('Oh, my keyboard!', 'I become the guy.')[n <= len(set(x[1:] + y[1:]))])