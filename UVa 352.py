import os
import sys
import math
from io import BytesIO, IOBase
def main():
	sys.stdin = open('in.txt','r')
	sys.stdout = open('out.txt', 'w')
	solve()


# def solve():
# 	while True:
# 		try:
# 			n = input()
# 		except EOFError: 
# 			break

# 		n = int(n)
# 		dx = [0, 0, 1, -1, 1, -1, 1, -1]
# 		dy = [1, -1, 0, 0, 1, -1, -1, 1]
		
# 		seen = [[None] * n for i in range(n)]
# 		grid = []
# 		for i in range(n):
# 			grid.append([int(i) for i in input()])

# 		def valid(i, j):
# 			return i>=0 and j>= 0 and i < n and j < n

# 		def dfs(i, j):
# 			if seen[i][j]:
# 				return
# 			seen[i][j] = 1
# 			for k in range(8):
# 				xc = dx[k] + i
# 				yc = dy[k] + j
# 				if(valid(xc, yc) and not seen[xc][yc] and grid[xc][yc] == 1):
# 					dfs(xc, yc)


# 		ans = 0


# 		for i in range(n):
# 			for j in range(n):
# 				if not seen[i][j] and grid[i][j] == 1:
# 					dfs(i, j)
# 					ans += 1

# 		print(f'Image number 1 contains {ans} war eagles.')
		

# -------------------------

def solve():
	while True:
		try:
			n = input()
		except EOFError:
			break

		n = int(n)
		# get all the directions for the dfs
		dx = [0, 0, 1, -1, 1, -1, 1, -1]
		dy = [1, -1, 0, 0, 1, -1, -1, 1]
		seen = [[None] * n for i in range(n)]
		grid = []

		# populate the grid with input
		for i in range(n):	
			grid.append([int(i) for i in input()])
		# validate if we're out of range
		def valid(i, j):
			return i >= 0 and j >= 0 and i < n and j < n


		def dfs(i, j):
			if seen[i][j]:
				return
			seen[i][j] = 1

			# go through all the directions
			for k in range(8):
				xc = dx[k] + i
				yc = dy[k] + j
				if(valid(xc, yc) and not seen[xc][yc] and grid[xc][yc] == 1):
					dfs(xc, yc)

		ans = 0

		for i in range(n):
			for j in range(n):
				if not seen[i][j] and grid[i][j] == 1:
					dfs(i, j)
					ans += 1

		print(f'Image number 1 contains {ans} war eagles.')


if __name__ == '__main__':
	main()
