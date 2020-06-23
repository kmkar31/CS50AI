from nim import train, play

ai = train(10000)
play_again = True
while play_again:
	play(ai)
	while True:
		print()
		t = input('Play Again? (Y/N)')
		if t=='N' or t=='n':
			play_again=False
			break
		elif t=='Y' or t=='y':
			play_again=True
			break
		else:
			print('Invalid Response')
			continue

