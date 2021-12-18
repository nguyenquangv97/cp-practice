import os
import sys
import math
from io import BytesIO, IOBase
def main():
	sys.stdin = open('in.txt','r')
	sys.stdout = open('out.txt', 'w')
	solve()


def solve():

	dx = [-1, 0, 0]
	dy = [0, 1, -1]

	direction = ['forth', 'right', 'left']
	path = 'IEHOVA#'

	def valid(i, j):
		return i >= 0 and i < n and j >= 0 and j < m

	res = []

	def dfs(i, j, idx):
		if idx == len(path): return
		for k in range(3):
			toX = i + dx[k]
			toY = j + dy[k]
			if valid(toX, toY) and a[toX][toY] == path[idx]:
				res.append(direction[k])
				dfs(toX, toY, idx + 1)


	t = int(input())

	# while t:
	m, n = map(int, input().split())
	a = [[None] * 9 for _ in range(9)]

	st = []
	for i in range(n):
		for j in range(m):
			a[i][j] = input()
			print(a[i][j])

			if a[i][j] == '@':
				st = [i, j]
	res.clear()
	dfs(st[0], st[1], 0)
	print(res[0])
	for i in range(1, len(res)):
		print(' ', res[i])
	print()


if __name__ == '__main__':
	main()
