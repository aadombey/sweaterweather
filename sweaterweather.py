#This is a program that gives you suggestions based on the temperature outside and whether
#or not you are planning on going outside. There is obviously room for improvement.

temp = float(raw_input("Enter current temperature: "))
second = raw_input("Planning on going outdoors?\n(Enter yes or no): ")
yes = 'yes'
no = 'no'
if temp > 100.0:
	if second == yes:
		print "Wear light clothing. Don't forget sunscreen!"
	elif second == no:
		print "It's too hot outside anyways"
elif temp > 70.0 and temp < 100.0:
	if second == yes:
		print "Wear shorts and a t-shirt. It's a great day to be outside"
	if second == no:
		print "You're missing out on some great weather"
elif temp > 45.0 and temp < 70.0:
	if second == yes:
		print "It's a bit chilly out. Make sure you bring a sweatshirt"
	if second == no:
		print "Nevermind, then."
elif temp > 20.0 and temp <  45.0:
	if second == yes:
		print "Make sure you wear long pants and a coat!\nYou don't want to be too cold"
	if second == no:
		print "Don't blame you. It's pretty cold out"
elif temp < 20.0:
	if second == yes:
		print "Cover up your ears and fingers (and everything else, obviously)\nNobody wants frostbite"
	if second == no:
		print "Definitely the best thing to do. It's freakin' freezing!"
elif temp < 10.0:
	if second == yes:
		print "Your not going outside its cold as shit"
	if second == no:
		print "Good call"