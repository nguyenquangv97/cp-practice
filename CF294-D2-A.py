n = int(input())

arr = list(map(int, input().split()))

matrix = [[1 for _ in range(arr[i])] for i in range(n)]

shots = int(input())

for shot in range(shots):
	wire, y = list(map(int, input().split()))
	wire = wire - 1
	y = y - 1
	if wire - 1 >= 0:
		matrix[wire-1].extend(matrix[wire][:y])
	if wire + 1 < n:
		matrix[wire+1].extend(matrix[wire][y+1:])
	matrix[wire] = []

for i in matrix:
	print(len(i))


''' Better '''
n = int(input())

arr = list(map(int, input().split()))

shots = int(input())

for shot in range(shots):
	wire, y = map(int, input().split())

	current_birds = arr[wire - 1]
	if wire  - 2 >= 0:
		arr[wire-2] +=  y - 1 
	if wire < len(arr):
		arr[wire] += (current_birds - y)
	arr[wire -1] = 0


for i in arr:
	print(i)