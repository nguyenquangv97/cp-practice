import os
import sys
from io import BytesIO, IOBase
def main():
	sys.stdin = open('in.txt','r')
	sys.stdout = open('out.txt', 'w')
	solve()




def solve():
	string = input()

	l, u = 0, 0
	for c in string:
		if c.isupper():
			u += 1
		else:
			l += 1

	if l < u:
		print(string.upper())
	else:
		print(string.lower())



if __name__ == '__main__':
	main()
