stones = input()
instructions = input()

i, j = 0, 0
while i < len(stones) and j < len(instructions):
	if instructions[j] == stones[i]:
		i+= 1
	j+= 1
print(i + 1)	