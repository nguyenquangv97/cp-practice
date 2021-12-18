direction = input()
message = input()
keyboard = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
ans = [] 
for c in message:
	for k in keyboard:
		if c in k:
			if direction == 'R':
				ans.append(k[k.index(c) - 1])
				break
			else:
				ans.append(k[k.index(c) + 1])
print(''.join(ans))
