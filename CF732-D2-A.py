price, coin = [int(x) for x in input().split()]
count = 1
while True:
	if (count * price) % 10 == 0 or (count * price) % 10 == coin:
		print(count)
		break
	else:
		count += 1
