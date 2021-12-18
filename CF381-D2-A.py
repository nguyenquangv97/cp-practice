n = int(input())
cards = input().split()
cards = [int(x) for x in cards]

i = 0
j = len(cards) - 1
s, d = 0, 0

sereja = True
while i <= j:

	if cards[i] < cards[j]:
		card = cards[j]
		j-= 1
	else:
		card = cards[i]
		i+= 1

	if sereja:
		s += card
	else:
		d += card
	sereja = not sereja

print(s, d)