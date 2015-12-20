def gameofthree(number):
	if number == 1:
		print "do:",number,"...wait a sec..."
		print "You are done! You win!"
		return 

	if (number % 3 == 0):
		print "do:",number, "/ 3 =",number/3,"then"
		return gameofthree(number/3)
	if ((number-1)%3 == 0):
		print "do:","(",number,"- 1 )/ 3 =", (number-1)/3,"then"
		return gameofthree((number-1)/3)
	if ((number+1)%3 == 0):
		print "do:","(",number,"+ 1 )/ 3 =",(number+1)/3,"then"
		return gameofthree((number+1)/3)
		
ans = raw_input("What number do you chose to play?")
num = int(ans)
print gameofthree(num)