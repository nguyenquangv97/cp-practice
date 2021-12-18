n = int(input())
word = set([i.lower() for i in input()])
alphabets = set([i for i in 'abcdefghijklmnopqrstuvwxyz'])
if len(alphabets.intersection(word)) == len(alphabets):
	print('YES')
else: print('NO')





input();
print('YNEOS'[len(set(input().upper()))<26::2])
