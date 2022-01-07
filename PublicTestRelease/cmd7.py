#!/usr/bin/env python3
print("Welcome to PY-DOS")
print("Version 7 Sleepy Sloth Public Test Release 3")
print("Developed by Gautham Nair")
first_name = input("Type your First Name: ")
pydos_ver = "7"
dev = "Public Test Release 3 , Build 6000.98 , PY-DOS 7 , Sleepy Sloth"
calc_ver = "2.00"
calendar_ver = "1.00"
randomnumber_ver = "1.00"
chat_ver = "3.01"
table_ver = "1.00"
dtm_ver = "1.00"
neocommand_ver = "7"
#Major Update (3JLY)
#PY-DOS Base Version 2.00
#Non-Loop Program....
#Only If and Else commands...
#Expected Loop commands in next version of PY-DOS (May come or May not)
#Public Test Release 3
#Released on 18-07-2021 10:00 PM IST
#Gautham Nair
#Suraj Varma
#Zanvok Corporation
#Browser not inbuilt with PY-DOS
#Place PY-DOS (cmd7.py) file and Browser (browser.py) file in the same directory/folder.
#Recommended to keep in the directory: C:\\Py
#Also create another directoy in C: drive as My Websites
#C:\\My Websites
#C:\\Py
#Python
#Python Software Foundation
#Guido Van Rossum
#Created using Visual Studio 2022 Preview Community in a Windows 11 System
#Python 3.10 IDLE (64-bit)
if first_name == "":
		first_name = input("Please type your first name to proceed: ")
		last_name = input("Type your Last Name: ")
		print(first_name + " " + last_name + "," + " " + "I like That Name!!")
		user_name = input("Type your User Name: ")
		if user_name == "":
			user_name + input("Please type a username to start using PY-DOS!: ")
			password = input("Password: ")
			password_verify = input("Confirm Password: ")
			if password_verify == password:
				pc_name =  input("Name your PC: ")
				print("Welcome! " + first_name  + " " +  last_name)
				print("You are signed in as " + user_name)
				command = ""
				while command != "quit":
					command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(PTR)" + "$").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "version":
						print("PY-DOS version-7")
					elif command == "randomnumber":
						print("Generates random number from 0 to 9")
						import random
						print(random.randint(0,9))
					elif command == "browser":
						import browser.py
						exit_browser = input("Press enter to exit")
					elif command == "age calc":
						import datetime
						print("This program is written in Python for PY-DOS!!!")
						january = "1"
						february = "2"
						march = "3"
						april = "4"
						may = "5"
						june = "6"
						july = "7"
						august = "8"
						september = "9"
						october = "10"
						november = "11"
						december = "12"
						birth_year = int(input("Enter your year of birth: "))
						birth_month = int(input("Enter your month of birth: "))
						birth_day = int(input("Enter your day of birth: "))
						current_year = datetime.date.today().year
						current_month = datetime.date.today().month
						current_day = datetime.date.today().day
						age_year = abs(current_year - birth_year)
						age_month = abs(current_month - birth_month)
						age_day = abs(current_day - birth_day)
						print("Your age is " , age_year , " Years," , age_month , " Months and" , age_day , " Days")
					elif command == "programver":
						print(" Calculator Suite: " + calc_ver)
						print("  Calc+ 1.00")
						print("  Calc- 1.00")
						print("  Calc* 1.00")
						print("  Calc/ 2.00")
						print("  CalcSQRT 1.00")
						print("  AgeCalc 1.00(BETA)")
						print(" RandomNumber " + randomnumber_ver)
						print(" Chat " + chat_ver)
						print(" PY Browser 1.00 ")
						print(" Table " + table_ver)
						print(" Calendar " + calendar_ver)
						print(" Date and Time Manager " + dtm_ver)
						print(" NeoCommand " + neocommand_ver)
					elif command == "py-dos":
						print(" PY-DOS Version Version History")
						print("   PY-DOS 1")
						print("   PY-DOS 2")
						print("   PY-DOS 2.5")
						print("   PY-DOS 3")
						print("   PY-DOS 3.1")
						print("   PY-DOS 4")
						print("   PY-DOS 5")
						print("   PY-DOS 6")
						print("   PY-DOS 7 ---> Current version")
					elif command == "microsoft":
						print("Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.")
					elif command == "google":
						print("Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple.")
					elif command == "apple":
						print("Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five companies in the U.S. information technology industry, along with Amazon, Google, Microsoft, and Facebook. It is one of the most popular smartphone and tablet companies in the world.")
					elif command == "facebook":
						print("Facebook is a for-profit corporation and online social networking service based in Menlo Park, California, United States. The Facebook website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.")
					elif command == "amazon":
						print("Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as one of the most influential economic and cultural forces in the world, as well as the world's most valuable brand.")
					elif command == "newupdates":
						print(" Expected changes to come in next version of PY-DOS")
						print("   An updated new calculator in PY-DOS 8 --> Under Developent")
						print("   New Easter-Egg command --> May Come")
					elif command == "table":
						print("This program is written in Python!!!")
						num = int(input("Enter the number : "))
						i = 1
						print("Here you go!!!") 
						while i<=10:
							num = num * 1
							print(num,'x',i,'=',num*i)
							i += 1
					elif command == "clock":
						from turtle import *
						from datetime import datetime

						def jump(distanz, winkel=0):
							penup()
							right(winkel)
							forward(distanz)
							left(winkel)
							pendown()

						def hand(laenge, spitze):
							fd(laenge*1.15)
							rt(90)
							fd(spitze/2.0)
							lt(120)
							fd(spitze)
							lt(120)
							fd(spitze)
							lt(120)
							fd(spitze/2.0)

						def make_hand_shape(name, laenge, spitze):
							reset()
							jump(-laenge*0.15)
							begin_poly()
							hand(laenge, spitze)
							end_poly()
							hand_form = get_poly()
							register_shape(name, hand_form)

						def clockface(radius):
							reset()
							pensize(7)
							for i in range(60):
								jump(radius)
								if i % 5 == 0:
									fd(25)
									jump(-radius-25)
								else:
									dot(3)
									jump(-radius)
								rt(6)

						def setup():
							global second_hand, minute_hand, hour_hand, writer
							mode("logo")
							make_hand_shape("second_hand", 125, 25)
							make_hand_shape("minute_hand",  130, 25)
							make_hand_shape("hour_hand", 90, 25)
							clockface(160)
							second_hand = Turtle()
							second_hand.shape("second_hand")
							second_hand.color("gray20", "gray80")
							minute_hand = Turtle()
							minute_hand.shape("minute_hand")
							minute_hand.color("blue1", "red1")
							hour_hand = Turtle()
							hour_hand.shape("hour_hand")
							hour_hand.color("blue3", "red3")
							for hand in second_hand, minute_hand, hour_hand:
								hand.resizemode("user")
								hand.shapesize(1, 1, 3)
								hand.speed(0)
							ht()
							writer = Turtle()
							#writer.mode("logo")
							writer.ht()
							writer.pu()
							writer.bk(85)

						def wochentag(t):
							wochentag = ["Monday", "Tuesday", "Wednesday",
								"Thursday", "Friday", "Saturday", "Sunday"]
							return wochentag[t.weekday()]

						def datum(z):
							monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
									 "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
							j = z.year
							m = monat[z.month - 1]
							t = z.day
							return "%s %d %d" % (m, t, j)

						def tick():
							t = datetime.today()
							sekunde = t.second + t.microsecond*0.000001
							minute = t.minute + sekunde/60.0
							stunde = t.hour + minute/60.0
							try:
								tracer(False)  # Terminator can occur here
								writer.clear()
								writer.home()
								writer.forward(65)
								writer.write(wochentag(t),
											 align="center", font=("Courier", 14, "bold"))
								writer.back(150)
								writer.write(datum(t),
											 align="center", font=("Courier", 14, "bold"))
								writer.forward(85)
								tracer(True)
								second_hand.setheading(6*sekunde)  # or here
								minute_hand.setheading(6*minute)
								hour_hand.setheading(30*stunde)
								tracer(True)
								ontimer(tick, 100)
							except Terminator:
								pass  # turtledemo user pressed STOP

						def main():
							tracer(False)
							setup()
							tracer(True)
							tick()
							return "EVENTLOOP"

						if __name__ == "__main__":
							mode("logo")
							msg = main()
							print(msg)
							mainloop()

					elif command == "who made you":
						print("Gautham Nair!!!")
					elif command == "who made you?":
						print("Gautham Nair!!!")
					elif command == "do you know gautham":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham?":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham nair":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham nair?":
						print("Oh, yeah, he created me!!")
					elif command == "do you know zanvok corporation":
						print("Sure, I do!!...A great company...!!!")
					elif command == "do you know zanvok corporation?":
						print("Sure, I do!!...A great company...!!!")
					elif command == "do you know zanvok":
						print("Sure!! Zanvok Corporation is awesome!!")
					elif command == "do you know zanvok?":
						print("Sure!! Zanvok Corporation is awesome!!")
					elif command == "neofetch":
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("**********     **********")
						print(" **********   **********")
						print("  ********** **********")
						print(" **********   **********")
						print("**********     **********")
						print("            7")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 7")
						print("Sleepy Sloth")
						print("------------------------------------")
						print("Written in Python")
						print("---------------------------------------")
						print("Zanvok Corporation")	
					elif command == "help":
						print("Commands for using PY-DOS")
						print(" calc+ - addition calculator")
						print(" calc- - subtraction calculator")
						print(" calc/ - division calculator")
						print(" calc* - multiplication calculator")
						print(" calcsqrt - square root calculator")
						print(" age calc - age calculator")
						print(" table - display table")
						print(" py-dos - PY-DOS Version History")
						print(" browser - starts PY Browser, a PyQt-Chromium based browser")
						print(" about - about PY-DOS")
						print(" status - PY-DOS Update and Base Version Details")
						print(" credits - display credits")
						print(" user - display user information")
						print(" change username - changes your username")
						print(" date - displays date")
						print(" time - display time")
						print(" date and time - display date and time")
						print(" chat - start a chat with PY-DOS")
						print(" clock - displays clock, inaccessible sometimes")
						print(" calendar - display calendar for the provided month and year")
						print(" randomnumber - generates a random number between 0 to 9")
						print(" programver - display version of all programs in PY-DOS")
					elif command == "about":
						print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
					elif command == "status":
						print(" PY-DOS Version & Update Status")
						print("  Version: 7 Sleepy Sloth")
						print("  About Update")
						print("   Update Name: 3JLY")
						print("   Update Version: 2021.7.7")
						print("   PY-DOS Base Version: 2.00")
					elif command == "calc+":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type the first number: ")
						second_number = input("Type the second number: ")
						sum = float(first_number) + float(second_number)
						print(sum)
					elif command == "calendar":
						import calendar
						yy = int(input("Enter Year: "))
						mm = int(input("Enter Month: "))
						print(calendar.month(yy , mm))
					elif command == "change username":
						userInput = input("Type current UserName: ")
						if userInput == user_name:
							userInput = input("Password?\n")
							if userInput == password:
								print("Change UserName")
							else:
								print("That is the wrong password.")
								break
						else:
								print("That is the wrong username.")
								break

						user_name = input("Type user name: ")
						print("Username changed to " + user_name)	
					elif command == "user":
						print("Name: " + first_name + " " + last_name)
						print("UserName: " + user_name)	
					elif command == "calc-":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						diff = float(first_number) - float(second_number)
						print(diff)
					elif command == "calc/":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						div = float(first_number) / float(second_number)
						print("your answer is ")
						print(div)
					elif command == "calc*":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						mul = float(first_number) * float(second_number)
						print(mul)	
					elif command == "calcsqrt":
						sqrt = input("Type the number: ")
						import math
						print(math.sqrt(float(sqrt)))	
					elif command == "date":
						from datetime import datetime

						now = datetime.now()
						date = now.strftime("%d/%m/%Y ")
						print("Date =", date)
					elif command == "time":
						from datetime import datetime

						now = datetime.now()
						time = now.strftime("%H:%M:%S")
						print("Time =", time)	
					elif command == "date and time":
						from datetime import datetime

						now = datetime.now()
						datetime = now.strftime("%d/%m/%Y  %H:%M:%S ")
						print("Date and Time =", datetime)	
					elif command == "time and date":
						from datetime import datetime

						now = datetime.now()
						datetime = now.strftime("%H:%M:%S %d/%m/%Y   ")
						print("Time and Date =", datetime)	
					elif command == "neofire":
						print("PY-DOS")
						print("Written in Python")
						print("Version 7")
						print("Sleepy Sloth")
						print("Type: Public Test Release 3 ")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 6 Panicked Pig")
						print("Python ")
						print("Build number: 6000.98")
						print("Build version: Sleepy Sloth")
					elif command == "chat":
						print("Hello! " + first_name +  " " + last_name + "😀")
						print("Welcome to PY-DOS Chat  {Preview}")
						chat_1 = input("How are you? [sad/happy/frustrated/bored/angry/confused] ")
						sad_var = "sad"
						zc_var = "do you know Zanvok Corporation"
						creation_var = "Who created you"
						happy_var = "happy"
						angry_var = "angry"
						frustrated_var = "frustrated"
						confused_var = "confused"
						bored_var = "bored"
			
						if chat_1 == sad_var:
							print("😢!!! Sad?? ")
							sad_reason = input("Tell me the reason why you are sad??")
							print("OK, so that's the reason")
						elif chat_1 == zc_var:
							print("There is no better place than home")
						elif chat_1 == creation_var:
							print("Gautham Nair")
						elif chat_1 == happy_var:
							print("😄, I'am happy to hear that!!!")
						elif chat_1 == angry_var:
							print("😠, Angry??")
							angry_reason = input("Tell me the reason why are you angry??")
							print("OK")
						elif chat_1 == frustrated_var:
							print("Why are you frustrated? ")
							frustrated_reason = input("What!! happened??!!")
							print("OK!!!")
						elif chat_1 == bored_var:
							print("Well, I can recommend you a few things!!")
							print("You can play games, watch movies, or explore PY-DOS!!")
						elif chat_1 == creation_var:
							print("Gautham Nair!!")
						elif chat_1 == zc_var:
							print("There is no better place than home")	
						elif chat_1 == confused_var:
							print("Confused what to do???")
							confused_sol = input("Any addition , subtraction , division , multiplication , or square root??")
							yes_var = "yes"
							no_var = "no"
							if confused_sol == yes_var:
								print(" Type calc+ for + , calc- for - , calc/ for / , calc* for * , calcsqrt for square root")
								if command == "calc+":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type the first number: ")
									second_number = input("Type the second number: ")
									sum = float(first_number) + float(second_number)
									print(sum)
						
								elif command == "calc-":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									diff = float(first_number) - float(second_number)
									print(diff)
								elif command == "calc/":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									div = float(first_number) / float(second_number)
									print(div)
								elif command == "calc*":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									mul = float(first_number) * float(second_number)
									print(mul)	
								elif command == "calcsqrt":
									sqrt = input("Type the number: ")
									import math
									print(math.sqrt(float(sqrt)))
							elif confused_sol == no_var:
								print("Ok!!!")					  	 
						else:
							print("Sorry, I didn't understand that!!")	
				
					elif command == "exit":
						break
					else:
						print("Bad command...Command not found!!")
			else:
				print("Oops!! password didn't match!!")
				print("This program will terminate now")
		else:
				password = input("Password: ")
				password_verify = input("Confirm Password: ")
				if password_verify == password:
					pc_name =  input("Name your PC: ")
					print("Welcome! " + first_name  + " " +  last_name)
					print("You are signed in as " + user_name)
					command = ""
					while command != "quit":
						command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(PTR)").lower()
						if command == "credits":
							print("________________________")
							print("Gautham Nair")
							print("------------------------")
							print("Zanvok Corporation")
						elif command == "version":
							print("PY-DOS version-7")
						elif command == "randomnumber":
							print("Generates a random number from 0 to 9")
							import random
							print(random.randint(0,9))
						elif command == "browser":
							import browser.py
						elif command == "age calc":
							import datetime
							print("This program is written in Python for PY-DOS!!!")
							birth_year = int(input("Enter your year of birth: "))
							birth_month = int(input("Enter your month of birth: "))
							birth_day = int(input("Enter your day of birth: "))
							current_year = datetime.date.today().year
							current_month = datetime.date.today().month
							current_day = datetime.date.today().day
							age_year = abs(current_year - birth_year)
							age_month = abs(current_month - birth_month)
							age_day = abs(current_day - birth_day)
							print("Your age is " , age_year , " Years," , age_month , " Months and" , age_day , " Days")
						elif command == "programver":
							print(" Calculator Suite: 2.00 ")
							print("  Calc+ 1.00")
							print("  Calc- 1.00")
							print("  Calc* 1.00")
							print("  Calc/ 2.00")
							print("  CalcSQRT 1.00")
							print(" RandomNumber 1.00")
							print(" Chat 3.01")
							print(" PY Browser ")
							print(" Table 1.00")
							print(" Calendar 1.00")
							print(" Date and Time Manager 1.00")
							print(" NeoCommand 7.00")
						elif command == "py-dos":
							print(" PY-DOS Version Version History")
							print("   PY-DOS 1")
							print("   PY-DOS 2")
							print("   PY-DOS 2.5")
							print("   PY-DOS 3")
							print("   PY-DOS 3.1")
							print("   PY-DOS 4")
							print("   PY-DOS 5")
							print("   PY-DOS 6")
							print("   PY-DOS 7 --->Current Version")
						elif command == "microsoft":
							print("Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.")
						elif command == "google":
							print("Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple.")
						elif command == "apple":
							print("Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five companies in the U.S. information technology industry, along with Amazon, Google, Microsoft, and Facebook. It is one of the most popular smartphone and tablet companies in the world.")
						elif command == "facebook":
							print("Facebook is a for-profit corporation and online social networking service based in Menlo Park, California, United States. The Facebook website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.")
						elif command == "amazon":
							print("Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as one of the most influential economic and cultural forces in the world, as well as the world's most valuable brand.")
						elif command == "newupdates":
							print(" Expected changes to come in next version of PY-DOS")
							print("   An updated new calculator in PY-DOS 8 --> Under Developent")
							print("   New Easter-Egg command --> May Come")
						elif command == "table":
							print("This program is written in Python!!!")
							num = int(input("Enter the number : "))
							i = 1
							print("Here you go!!!") 
							while i<=10:
								num = num * 1
								print(num,'x',i,'=',num*i)
								i += 1
						elif command == "who made you":
							print("Gautham Nair!!!")
						elif command == "who made you?":
							print("Gautham Nair!!!")
						elif command == "do you know gautham":
							print("Oh, yeah, he created me!!")
						elif command == "do you know gautham?":
							print("Oh, yeah, he created me!!")
						elif command == "do you know gautham nair":
							print("Oh, yeah, he created me!!")
						elif command == "do you know gautham nair?":
							print("Oh, yeah, he created me!!")
						elif command == "do you know zanvok corporation":
							print("Sure, I do!!...A great company...!!!")
						elif command == "do you know zanvok corporation?":
							print("Sure, I do!!...A great company...!!!")
						elif command == "do you know zanvok":
							print("Sure!! Zanvok Corporation is awesome!!")
						elif command == "do you know zanvok?":
							print("Sure!! Zanvok Corporation is awesome!!")
						elif command == "neofetch":
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("**********     **********")
							print(" **********   **********")
							print("  ********** **********")
							print(" **********   **********")
							print("**********     **********")
							print("            7")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("PY-DOS ")
							print("-----------------")
							print("Version 7")
							print("Sleepy Sloth")
							print("------------------------------------")
							print("Written in Python")
							print("---------------------------------------")
							print("Zanvok Corporation")	
						elif command == "help":
							print("Commands for using PY-DOS")
							print(" calc+ - addition calculator")
							print(" calc- - subtraction calculator")
							print(" calc/ - division calculator")
							print(" calc* - multiplication calculator")
							print(" calcsqrt - square root calculator")
							print(" age calc - age calculator")
							print(" table - display table")
							print(" py-dos - PY-DOS Version History")
							print(" browser - starts PY Browser, a PyQt-Chromium based browser")
							print(" about - about PY-DOS")
							print(" status - PY-DOS Update and Base Version Details")
							print(" credits - display credits")
							print(" user - display user information")
							print(" change username - changes your username")
							print(" date - displays date")
							print(" time - display time")
							print(" date and time - display date and time")
							print(" chat - start a chat with PY-DOS")
							print(" clock - displays clock, inaccessible sometimes")
							print(" calendar - display calendar for the provided month and year")
							print(" randomnumber - generates a random number between 0 to 9")
							print(" programver - display version of all programs in PY-DOS")
						elif command == "about":
							print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
						elif command == "status":
							print(" PY-DOS Version & Update Status")
							print("  Version: 7 Sleepy Sloth")
							print("  About Update")
							print("   Update Name: 3JLY")
							print("   Update Version: 2021.7.7")
							print("   PY-DOS Base Version: 2.00")
						elif command == "calc+":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type the first number: ")
							second_number = input("Type the second number: ")
							sum = float(first_number) + float(second_number)
							print(sum)
						elif command == "change username":
							userInput = input("Type current UserName: ")
							if userInput == user_name:
								userInput = input("Password?\n")
								if userInput == password:
									print("Change UserName")
								else:
									print("That is the wrong password.")
									break
							else:
									print("That is the wrong username.")
									break

							user_name = input("Type user name: ")
							print("Username changed to " + user_name)	
						elif command == "user":
							print("Name: " + first_name + " " + last_name)
							print("UserName: " + user_name)	
						elif command == "calc-":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type first number: ")
							second_number = input("Type second number: ")
							diff = float(first_number) - float(second_number)
							print(diff)
						elif command == "calc/":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type first number: ")
							second_number = input("Type second number: ")
							div = float(first_number) / float(second_number)
							print("your answer is ")
							print(div)
						elif command == "calc*":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type first number: ")
							second_number = input("Type second number: ")
							mul = float(first_number) * float(second_number)
							print(mul)	
						elif command == "calcsqrt":
							sqrt = input("Type the number: ")
							import math
							print(math.sqrt(float(sqrt)))	
						elif command == "date":
							from datetime import datetime

							now = datetime.now()
							date = now.strftime("%d/%m/%Y ")
							print("Date =", date)
						elif command == "time":
							from datetime import datetime

							now = datetime.now()
							time = now.strftime("%H:%M:%S")
							print("Time =", time)	
						elif command == "date and time":
							from datetime import datetime

							now = datetime.now()
							datetime = now.strftime("%d/%m/%Y  %H:%M:%S ")
							print("Date and Time =", datetime)	
						elif command == "time and date":
							from datetime import datetime

							now = datetime.now()
							datetime = now.strftime("%H:%M:%S %d/%m/%Y   ")
							print("Time and Date =", datetime)
						elif command == "calendar":
							import calendar
							yy = int(input("Enter Year: "))
							mm = int(input("Enter Month: "))
							print(calendar.month(yy , mm))
						elif command == "neofire":  
							print("PY-DOS")
							print("Written in Python")
							print("Version 7")
							print("Sleepy Sloth")
							print("Developed by Gautham Nair")
							print("Updated version of PY-DOS 6 Panicked Pig")
							print("Python ")
							print("Build number: 6000.98")
							print("Build version: Sleepy Sloth")
						elif command == "chat":
							print("Hello! " + first_name +  " " + last_name + "😀")
							print("Welcome to PY-DOS Chat  {Preview}")
							chat_1 = input("How are you? [sad/happy/frustrated/bored/angry/confused] ")
							sad_var = "sad"
							zc_var = "do you know Zanvok Corporation"
							creation_var = "Who created you"
							happy_var = "happy"
							angry_var = "angry"
							frustrated_var = "frustrated"
							confused_var = "confused"
							bored_var = "bored"
			
							if chat_1 == sad_var:
								print("😢!!! Sad?? ")
								sad_reason = input("Tell me the reason why you are sad??")
								print("OK, so that's the reason")
							elif chat_1 == zc_var:
								print("There is no better place than home")
							elif chat_1 == creation_var:
								print("Gautham Nair")
							elif chat_1 == happy_var:
								print("😄, I'am happy to hear that!!!")
							elif chat_1 == angry_var:
								print("😠, Angry??")
								angry_reason = input("Tell me the reason why are you angry??")
								print("OK")
							elif chat_1 == frustrated_var:
								print("Why are you frustrated? ")
								frustrated_reason = input("What!! happened??!!")
								print("OK!!!")
							elif chat_1 == bored_var:
								print("Well, I can recommend you a few things!!")
								print("You can play games, watch movies, or explore PY-DOS!!")
							elif chat_1 == creation_var:
								print("Gautham Nair!!")
							elif chat_1 == zc_var:
								print("There is no better place than home")	
							elif chat_1 == confused_var:
								print("Confused what to do???")
								confused_sol = input("Any addition , subtraction , division , multiplication , or square root??")
								yes_var = "yes"
								no_var = "no"
								if confused_sol == yes_var:
									print(" Type calc+ for + , calc- for - , calc/ for / , calc* for * , calcsqrt for square root")
									if command == "calc+":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type the first number: ")
										second_number = input("Type the second number: ")
										sum = float(first_number) + float(second_number)
										print(sum)
						
									elif command == "calc-":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type first number: ")
										second_number = input("Type second number: ")
										diff = float(first_number) - float(second_number)
										print(diff)
									elif command == "calc/":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type first number: ")
										second_number = input("Type second number: ")
										div = float(first_number) / float(second_number)
										print(div)
									elif command == "calc*":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type first number: ")
										second_number = input("Type second number: ")
										mul = float(first_number) * float(second_number)
										print(mul)	
									elif command == "calcsqrt":
										sqrt = input("Type the number: ")
										import math
										print(math.sqrt(float(sqrt)))
								elif confused_sol == no_var:
									print("Ok!!!")					  	 
							else:
								print("Sorry, I didn't understand that!!")	
				
						elif command == "exit":
							break
						else:
							print("Bad command...Command not found!!")
					else:
						print("Oops!! password didn't match!!")
						print("This program will terminate now")
				password = input("Password: ")
				password_verify = input("Confirm Password: ")
				if password_verify == password:
					pc_name =  input("Name your PC: ")
					print("Welcome! " + first_name  + " " +  last_name)
					print("You are signed in as " + user_name)
					command = ""
					while command != "quit":
						command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(PTR)").lower()
						if command == "credits":
							print("________________________")
							print("Gautham Nair")
							print("------------------------")
							print("Zanvok Corporation")
						elif command == "version":
							print("PY-DOS version-7")
						elif command == "randomnumber":
							print("Generates a random number from 0 to 9")
							import random
							print(random.randint(0,9))
						elif command == "browser":
							import browser.py
						elif command == "age calc":
							import datetime
							print("This program is written in Python for PY-DOS!!!")
							birth_year = int(input("Enter your year of birth: "))
							birth_month = int(input("Enter your month of birth: "))
							birth_day = int(input("Enter your day of birth: "))
							current_year = datetime.date.today().year
							current_month = datetime.date.today().month
							current_day = datetime.date.today().day
							age_year = abs(current_year - birth_year)
							age_month = abs(current_month - birth_month)
							age_day = abs(current_day - birth_day)
							print("Your age is " , age_year , " Years," , age_month , " Months and" , age_day , " Days")
						elif command == "programver":
							print(" Calculator Suite: 2.00 ")
							print("  Calc+ 1.00")
							print("  Calc- 1.00")
							print("  Calc* 1.00")
							print("  Calc/ 2.00")
							print("  CalcSQRT 1.00")
							print(" RandomNumber 1.00")
							print(" Chat 3.01")
							print(" PY Browser 1.00")
							print(" Table 1.00")
							print(" Calendar 1.00")
							print(" Date and Time Manager 1.00")
							print(" NeoCommand 7.00")
						elif command == "py-dos":
							print(" PY-DOS Version Version History")
							print("   PY-DOS 1")
							print("   PY-DOS 2")
							print("   PY-DOS 2.5")
							print("   PY-DOS 3")
							print("   PY-DOS 3.1")
							print("   PY-DOS 4")
							print("   PY-DOS 5")
							print("   PY-DOS 6")
							print("   PY-DOS 7 ---> Current version")
						elif command == "microsoft":
							print("Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.")
						elif command == "google":
							print("Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple.")
						elif command == "apple":
							print("Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five companies in the U.S. information technology industry, along with Amazon, Google, Microsoft, and Facebook. It is one of the most popular smartphone and tablet companies in the world.")
						elif command == "facebook":
							print("Facebook is a for-profit corporation and online social networking service based in Menlo Park, California, United States. The Facebook website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.")
						elif command == "amazon":
							print("Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as one of the most influential economic and cultural forces in the world, as well as the world's most valuable brand.")
						elif command == "newupdates":
							print(" Expected changes to come in next version of PY-DOS")
							print("   An updated new calculator in PY-DOS 7 --> Under Developent")
							print("   New Easter-Egg command --> May Come")
						elif command == "table":
							print("This program is written in Python!!!")
							num = int(input("Enter the number : "))
							i = 1
							print("Here you go!!!") 
							while i<=10:
								num = num * 1
								print(num,'x',i,'=',num*i)
								i += 1
						                        
						elif command == "who made you":
							print("Gautham Nair!!!")
						elif command == "who made you?":
							print("Gautham Nair!!!")
						elif command == "do you know gautham":
							print("Oh, yeah, he created me!!")
						elif command == "do you know gautham?":
							print("Oh, yeah, he created me!!")
						elif command == "do you know gautham nair":
							print("Oh, yeah, he created me!!")
						elif command == "do you know gautham nair?":
							print("Oh, yeah, he created me!!")
						elif command == "do you know zanvok corporation":
							print("Sure, I do!!...A great company...!!!")
						elif command == "do you know zanvok corporation?":
							print("Sure, I do!!...A great company...!!!")
						elif command == "do you know zanvok":
							print("Sure!! Zanvok Corporation is awesome!!")
						elif command == "do you know zanvok?":
							print("Sure!! Zanvok Corporation is awesome!!")
						elif command == "neofetch":
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("**********     **********")
							print(" **********   **********")
							print("  ********** **********")
							print(" **********   **********")
							print("**********     **********")
							print("            7")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("PY-DOS ")
							print("-----------------")
							print("Version 7")
							print("Sleepy Sloth")
							print("------------------------------------")
							print("Written in Python")
							print("---------------------------------------")
							print("Zanvok Corporation")	
						elif command == "help":
							print("Commands for using PY-DOS")
							print(" calc+ - addition calculator")
							print(" calc- - subtraction calculator")
							print(" calc/ - division calculator")
							print(" calc* - multiplication calculator")
							print(" calcsqrt - square root calculator")
							print(" age calc - age calculator")
							print(" table - display table")
							print(" py-dos - PY-DOS Version History")
							print(" browser - starts PY Browser, a PyQt-Chromium based browser")
							print(" about - about PY-DOS")
							print(" status - PY-DOS Update and Base Version Details")
							print(" credits - display credits")
							print(" user - display user information")
							print(" change username - changes your username")
							print(" date - displays date")
							print(" time - display time")
							print(" date and time - display date and time")
							print(" chat - start a chat with PY-DOS")
							print(" clock - displays clock, inaccessible sometimes")
							print(" calendar - display calendar for the provided month and year")
							print(" randomnumber - generates a random number between 0 to 9")
							print(" programver - display version of all programs in PY-DOS")
						elif command == "about":
							print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
						elif command == "status":
							print(" PY-DOS Version & Update Status")
							print("  Version: 7 Sleepy Sloth")
							print("  About Update")
							print("   Update Name: 3JLY")
							print("   Update Version: 2021.7.7")
							print("   PY-DOS Base Version: 2.00")
						elif command == "calc+":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type the first number: ")
							second_number = input("Type the second number: ")
							sum = float(first_number) + float(second_number)
							print(sum)
						elif command == "change username":
							userInput = input("Type current UserName: ")
							if userInput == user_name:
								userInput = input("Password?\n")
								if userInput == password:
									print("Change UserName")
								else:
									print("That is the wrong password.")
									break
							else:
									print("That is the wrong username.")
									break

							user_name = input("Type user name: ")
							print("Username changed to " + user_name)	
						elif command == "user":
							print("Name: " + first_name + " " + last_name)
							print("UserName: " + user_name)	
						elif command == "calc-":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type first number: ")
							second_number = input("Type second number: ")
							diff = float(first_number) - float(second_number)
							print(diff)
						elif command == "calc/":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type first number: ")
							second_number = input("Type second number: ")
							div = float(first_number) / float(second_number)
							print("your answer is ")
							print(div)
						elif command == "calc*":
							print("This program is written in Python for PY-DOS!! ")
							first_number = input("Type first number: ")
							second_number = input("Type second number: ")
							mul = float(first_number) * float(second_number)
							print(mul)	
						elif command == "calcsqrt":
							sqrt = input("Type the number: ")
							import math
							print(math.sqrt(float(sqrt)))	
						elif command == "date":
							from datetime import datetime

							now = datetime.now()
							date = now.strftime("%d/%m/%Y ")
							print("Date =", date)
						elif command == "time":
							from datetime import datetime

							now = datetime.now()
							time = now.strftime("%H:%M:%S")
							print("Time =", time)	
						elif command == "date and time":
							from datetime import datetime

							now = datetime.now()
							datetime = now.strftime("%d/%m/%Y  %H:%M:%S ")
							print("Date and Time =", datetime)	
						elif command == "time and date":
							from datetime import datetime

							now = datetime.now()
							datetime = now.strftime("%H:%M:%S %d/%m/%Y   ")
							print("Time and Date =", datetime)
						elif command == "calendar":
							import calendar
							yy = int(input("Enter Year: "))
							mm = int(input("Enter Month: "))
							print(calendar.month(yy , mm))
						elif command == "neofire":
							print("PY-DOS")
							print("Written in Python")
							print("Version 7")
							print("Sleepy Sloth")
							print("Developed by Gautham Nair")
							print("Updated version of PY-DOS 6 Panicked Pig")
							print("Python ")
							print("Build number: 6000.98")
							print("Build version: Sleepy Sloth")
						elif command == "chat":
							print("Hello! " + first_name +  " " + last_name + "😀")
							print("Welcome to PY-DOS Chat  {Preview}")
							chat_1 = input("How are you? [sad/happy/frustrated/bored/angry/confused] ")
							sad_var = "sad"
							zc_var = "do you know Zanvok Corporation"
							creation_var = "Who created you"
							happy_var = "happy"
							angry_var = "angry"
							frustrated_var = "frustrated"
							confused_var = "confused"
							bored_var = "bored"
			
							if chat_1 == sad_var:
								print("😢!!! Sad?? ")
								sad_reason = input("Tell me the reason why you are sad??")
								print("OK, so that's the reason")
							elif chat_1 == zc_var:
								print("There is no better place than home")
							elif chat_1 == creation_var:
								print("Gautham Nair")
							elif chat_1 == happy_var:
								print("😄, I'am happy to hear that!!!")
							elif chat_1 == angry_var:
								print("😠, Angry??")
								angry_reason = input("Tell me the reason why are you angry??")
								print("OK")
							elif chat_1 == frustrated_var:
								print("Why are you frustrated? ")
								frustrated_reason = input("What!! happened??!!")
								print("OK!!!")
							elif chat_1 == bored_var:
								print("Well, I can recommend you a few things!!")
								print("You can play games, watch movies, or explore PY-DOS!!")
							elif chat_1 == creation_var:
								print("Gautham Nair!!")
							elif chat_1 == zc_var:
								print("There is no better place than home")	
							elif chat_1 == confused_var:
								print("Confused what to do???")
								confused_sol = input("Any addition , subtraction , division , multiplication , or square root??")
								yes_var = "yes"
								no_var = "no"
								if confused_sol == yes_var:
									print(" Type calc+ for + , calc- for - , calc/ for / , calc* for * , calcsqrt for square root")
									if command == "calc+":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type the first number: ")
										second_number = input("Type the second number: ")
										sum = float(first_number) + float(second_number)
										print(sum)
						
									elif command == "calc-":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type first number: ")
										second_number = input("Type second number: ")
										diff = float(first_number) - float(second_number)
										print(diff)
									elif command == "calc/":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type first number: ")
										second_number = input("Type second number: ")
										div = float(first_number) / float(second_number)
										print(div)
									elif command == "calc*":
										print("This program is written in Python for PY-DOS!! ")
										first_number = input("Type first number: ")
										second_number = input("Type second number: ")
										mul = float(first_number) * float(second_number)
										print(mul)	
									elif command == "calcsqrt":
										sqrt = input("Type the number: ")
										import math
										print(math.sqrt(float(sqrt)))
								elif confused_sol == no_var:
									print("Ok!!!")					  	 
							else:
								print("Sorry, I didn't understand that!!")	
				
						elif command == "exit":
							break
						else:
							print("Bad command...Command not found!!")
				else:
					print("Oops!! password didn't match!!")
					print("This program will terminate now")
else:
		last_name = input("Type your Last Name: ")
		print(first_name + " " + last_name + "," + " " + "I like That Name!!")
		user_name = input("Type your User Name: ")
		if user_name == "":
			user_name = input("Please type your username to proceed: ")
			password = input("Password: ")
			password_verify = input("Confirm Password: ")
			if password_verify == password:
				pc_name =  input("Name your PC: ")
				print("Welcome! " + first_name  + " " +  last_name)
				print("You are signed in as " + user_name)
				command = ""
				while command != "quit":
					command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(PTR)").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "version":
						print("PY-DOS version-6")
					elif command == "randomnumber":
						print("Generates a random number from 0 to 9")
						import random
						print(random.randint(0,9))
					elif command == "browser":
						import browser.py
					elif command == "age calc":
						import datetime
						print("This program is written in Python for PY-DOS!!!")
						birth_year = int(input("Enter your year of birth: "))
						birth_month = int(input("Enter your month of birth: "))
						birth_day = int(input("Enter your day of birth: "))
						current_year = datetime.date.today().year
						current_month = datetime.date.today().month
						current_day = datetime.date.today().day
						age_year = abs(current_year - birth_year)
						age_month = abs(current_month - birth_month)
						age_day = abs(current_day - birth_day)
						print("Your age is " , age_year , " Years," , age_month , " Months and" , age_day , " Days")
					elif command == "programver":
						print(" Calculator Suite: 2.00 ")
						print("  Calc+ 1.00")
						print("  Calc- 1.00")
						print("  Calc* 1.00")
						print("  Calc/ 2.00")
						print("  CalcSQRT 1.00")
						print(" RandomNumber 1.00")
						print(" Chat 3.01")
						print(" PY Browser ")
						print(" Table 1.00")
						print(" Calendar 1.00")
						print(" Date and Time Manager 1.00")
						print(" NeoCommand 7.00")
					elif command == "py-dos":
						print(" PY-DOS Version Version History")
						print("   PY-DOS 1")
						print("   PY-DOS 2")
						print("   PY-DOS 2.5")
						print("   PY-DOS 3")
						print("   PY-DOS 3.1")
						print("   PY-DOS 4")
						print("   PY-DOS 5")
						print("   PY-DOS 6")
						print("   PY-DOS 7 ---> Current Version")
					elif command == "microsoft":
						print("Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.")
					elif command == "google":
						print("Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple.")
					elif command == "apple":
						print("Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five companies in the U.S. information technology industry, along with Amazon, Google, Microsoft, and Facebook. It is one of the most popular smartphone and tablet companies in the world.")
					elif command == "facebook":
						print("Facebook is a for-profit corporation and online social networking service based in Menlo Park, California, United States. The Facebook website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.")
					elif command == "amazon":
						print("Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as one of the most influential economic and cultural forces in the world, as well as the world's most valuable brand.")
					elif command == "newupdates":
						print(" Expected changes to come in next version of PY-DOS")
						print("   An updated new calculator in PY-DOS 8 --> Under Developent")
						print("   New Easter-Egg command --> May Come")
					elif command == "table":
						print("This program is written in Python!!!")
						num = int(input("Enter the number : "))
						i = 1
						print("Here you go!!!") 
						while i<=10:
							num = num * 1
							print(num,'x',i,'=',num*i)
							i += 1
					elif command == "clock":
						from turtle import *
						from datetime import datetime

						def jump(distanz, winkel=0):
							penup()
							right(winkel)
							forward(distanz)
							left(winkel)
							pendown()

						def hand(laenge, spitze):
							fd(laenge*1.15)
							rt(90)
							fd(spitze/2.0)
							lt(120)
							fd(spitze)
							lt(120)
							fd(spitze)
							lt(120)
							fd(spitze/2.0)

						def make_hand_shape(name, laenge, spitze):
							reset()
							jump(-laenge*0.15)
							begin_poly()
							hand(laenge, spitze)
							end_poly()
							hand_form = get_poly()
							register_shape(name, hand_form)

						def clockface(radius):
							reset()
							pensize(7)
							for i in range(60):
								jump(radius)
								if i % 5 == 0:
									fd(25)
									jump(-radius-25)
								else:
									dot(3)
									jump(-radius)
								rt(6)

						def setup():
							global second_hand, minute_hand, hour_hand, writer
							mode("logo")
							make_hand_shape("second_hand", 125, 25)
							make_hand_shape("minute_hand",  130, 25)
							make_hand_shape("hour_hand", 90, 25)
							clockface(160)
							second_hand = Turtle()
							second_hand.shape("second_hand")
							second_hand.color("gray20", "gray80")
							minute_hand = Turtle()
							minute_hand.shape("minute_hand")
							minute_hand.color("blue1", "red1")
							hour_hand = Turtle()
							hour_hand.shape("hour_hand")
							hour_hand.color("blue3", "red3")
							for hand in second_hand, minute_hand, hour_hand:
								hand.resizemode("user")
								hand.shapesize(1, 1, 3)
								hand.speed(0)
							ht()
							writer = Turtle()
							#writer.mode("logo")
							writer.ht()
							writer.pu()
							writer.bk(85)

						def wochentag(t):
							wochentag = ["Monday", "Tuesday", "Wednesday",
								"Thursday", "Friday", "Saturday", "Sunday"]
							return wochentag[t.weekday()]

						def datum(z):
							monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
									 "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
							j = z.year
							m = monat[z.month - 1]
							t = z.day
							return "%s %d %d" % (m, t, j)

						def tick():
							t = datetime.today()
							sekunde = t.second + t.microsecond*0.000001
							minute = t.minute + sekunde/60.0
							stunde = t.hour + minute/60.0
							try:
								tracer(False)  # Terminator can occur here
								writer.clear()
								writer.home()
								writer.forward(65)
								writer.write(wochentag(t),
											 align="center", font=("Courier", 14, "bold"))
								writer.back(150)
								writer.write(datum(t),
											 align="center", font=("Courier", 14, "bold"))
								writer.forward(85)
								tracer(True)
								second_hand.setheading(6*sekunde)  # or here
								minute_hand.setheading(6*minute)
								hour_hand.setheading(30*stunde)
								tracer(True)
								ontimer(tick, 100)
							except Terminator:
								pass  # turtledemo user pressed STOP

						def main():
							tracer(False)
							setup()
							tracer(True)
							tick()
							return "EVENTLOOP"

						if __name__ == "__main__":
							mode("logo")
							msg = main()
							print(msg)
							mainloop()
					elif command == "who made you":
						print("Gautham Nair!!!")
					elif command == "who made you?":
						print("Gautham Nair!!!")
					elif command == "do you know gautham":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham?":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham nair":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham nair?":
						print("Oh, yeah, he created me!!")
					elif command == "do you know zanvok corporation":
						print("Sure, I do!!...A great company...!!!")
					elif command == "do you know zanvok corporation?":
						print("Sure, I do!!...A great company...!!!")
					elif command == "do you know zanvok":
						print("Sure!! Zanvok Corporation is awesome!!")
					elif command == "do you know zanvok?":
						print("Sure!! Zanvok Corporation is awesome!!")
					elif command == "neofetch":
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("**********     **********")
						print(" **********   **********")
						print("  ********** **********")
						print(" **********   **********")
						print("**********     **********")
						print("            7")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 7")
						print("Sleepy Sloth")
						print("------------------------------------")
						print("Written in Python")
						print("---------------------------------------")
						print("Zanvok Corporation")	
					elif command == "help":
						print("Commands for using PY-DOS")
						print(" calc+ - addition calculator")
						print(" calc- - subtraction calculator")
						print(" calc/ - division calculator")
						print(" calc* - multiplication calculator")
						print(" calcsqrt - square root calculator")
						print(" age calc - age calculator")
						print(" table - display table")
						print(" py-dos - PY-DOS Version History")
						print(" browser - starts PY Browser, a PyQt-Chromium based browser")
						print(" about - about PY-DOS")
						print(" status - PY-DOS Update and Base Version Details")
						print(" credits - display credits")
						print(" user - display user information")
						print(" change username - changes your username")
						print(" date - displays date")
						print(" time - display time")
						print(" date and time - display date and time")
						print(" chat - start a chat with PY-DOS")
						print(" clock - displays clock, inaccessible sometimes")
						print(" calendar - display calendar for the provided month and year")
						print(" randomnumber - generates a random number between 0 to 9")
						print(" programver - display version of all programs in PY-DOS")
					elif command == "about":
						print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
					elif command == "status":
						print(" PY-DOS Version & Update Status")
						print("  Version: 7 Sleepy Sloth")
						print("  About Update")
						print("   Update Name: 3JLY")
						print("   Update Version: 2021.7.7")
						print("   PY-DOS Base Version: 2.00")
						print("   Public Test Release 3")
					elif command == "calc+":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type the first number: ")
						second_number = input("Type the second number: ")
						sum = float(first_number) + float(second_number)
						print(sum)
					elif command == "change username":
						userInput = input("Type current UserName: ")
						if userInput == user_name:
							userInput = input("Password?\n")
							if userInput == password:
								print("Change UserName")
							else:
								print("That is the wrong password.")
								break
						else:
								print("That is the wrong username.")
								break

						user_name = input("Type user name: ")
						print("Username changed to " + user_name)	
					elif command == "user":
						print("Name: " + first_name + " " + last_name)
						print("UserName: " + user_name)	
					elif command == "calc-":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						diff = float(first_number) - float(second_number)
						print(diff)
					elif command == "calc/":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						div = float(first_number) / float(second_number)
						print("your answer is ")
						print(div)
					elif command == "calc*":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						mul = float(first_number) * float(second_number)
						print(mul)	
					elif command == "calcsqrt":
						sqrt = input("Type the number: ")
						import math
						print(math.sqrt(float(sqrt)))	
					elif command == "date":
						from datetime import datetime

						now = datetime.now()
						date = now.strftime("%d/%m/%Y ")
						print("Date =", date)
					elif command == "time":
						from datetime import datetime

						now = datetime.now()
						time = now.strftime("%H:%M:%S")
						print("Time =", time)	
					elif command == "date and time":
						from datetime import datetime

						now = datetime.now()
						datetime = now.strftime("%d/%m/%Y  %H:%M:%S ")
						print("Date and Time =", datetime)	
					elif command == "time and date":
						from datetime import datetime

						now = datetime.now()
						datetime = now.strftime("%H:%M:%S %d/%m/%Y   ")
						print("Time and Date =", datetime)
					elif command == "calendar":
						import calendar
						yy = int(input("Enter Year: "))
						mm = int(input("Enter Month: "))
						print(calendar.month(yy , mm))
					elif command == "neofire":
						print("PY-DOS")
						print("Written in Python")
						print("Version 7")
						print("Sleepy Sloth")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 6 Panicked Pig")
						print("Python ")
						print("Build number: 6000.98")
						print("Build version: Sleepy Sloth")
					elif command == "chat":
						print("Hello! " + first_name +  " " + last_name + "😀")
						print("Welcome to PY-DOS Chat  {Preview}")
						chat_1 = input("How are you? [sad/happy/frustrated/bored/angry/confused] ")
						sad_var = "sad"
						zc_var = "do you know Zanvok Corporation"
						creation_var = "Who created you"
						happy_var = "happy"
						angry_var = "angry"
						frustrated_var = "frustrated"
						confused_var = "confused"
						bored_var = "bored"
			
						if chat_1 == sad_var:
							print("😢!!! Sad?? ")
							sad_reason = input("Tell me the reason why you are sad??")
							print("OK, so that's the reason")
						elif chat_1 == zc_var:
							print("There is no better place than home")
						elif chat_1 == creation_var:
							print("Gautham Nair")
						elif chat_1 == happy_var:
							print("😄, I'am happy to hear that!!!")
						elif chat_1 == angry_var:
							print("😠, Angry??")
							angry_reason = input("Tell me the reason why are you angry??")
							print("OK")
						elif chat_1 == frustrated_var:
							print("Why are you frustrated? ")
							frustrated_reason = input("What!! happened??!!")
							print("OK!!!")
						elif chat_1 == bored_var:
							print("Well, I can recommend you a few things!!")
							print("You can play games, watch movies, or explore PY-DOS!!")
						elif chat_1 == creation_var:
							print("Gautham Nair!!")
						elif chat_1 == zc_var:
							print("There is no better place than home")	
						elif chat_1 == confused_var:
							print("Confused what to do???")
							confused_sol = input("Any addition , subtraction , division , multiplication , or square root??")
							yes_var = "yes"
							no_var = "no"
							if confused_sol == yes_var:
								print(" Type calc+ for + , calc- for - , calc/ for / , calc* for * , calcsqrt for square root")
								if command == "calc+":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type the first number: ")
									second_number = input("Type the second number: ")
									sum = float(first_number) + float(second_number)
									print(sum)
						
								elif command == "calc-":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									diff = float(first_number) - float(second_number)
									print(diff)
								elif command == "calc/":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									div = float(first_number) / float(second_number)
									print(div)
								elif command == "calc*":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									mul = float(first_number) * float(second_number)
									print(mul)	
								elif command == "calcsqrt":
									sqrt = input("Type the number: ")
									import math
									print(math.sqrt(float(sqrt)))
							elif confused_sol == no_var:
								print("Ok!!!")					  	 
						else:
							print("Sorry, I didn't understand that!!")	
				
					elif command == "exit":
						break
					else:
						print("Bad command...Command not found!!")
			else:
				print("Oops!! password didn't match!!")
				print("This program will terminate now")
		else:
			password = input("Password: ")
			password_verify = input("Confirm Password: ")
			if password_verify == password:
				pc_name =  input("Name your PC: ")
				print("Welcome! " + first_name  + " " +  last_name)
				print("You are signed in as " + user_name)
				command = ""
				while command != "quit":
					command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(PTR)").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "version":
						print("PY-DOS version-7")
					elif command == "randomnumber":
						print("generates a random number from 0 to 9")
						import random
						print(random.randint(0,9))
					elif command == "browser":
						import browser.py
					elif command == "age calc":
						import datetime
						print("This program is written in Python for PY-DOS!!!")
						birth_year = int(input("Enter your year of birth: "))
						birth_month = int(input("Enter your month of birth: "))
						birth_day = int(input("Enter your day of birth: "))
						current_year = datetime.date.today().year
						current_month = datetime.date.today().month
						current_day = datetime.date.today().day
						age_year = abs(current_year - birth_year)
						age_month = abs(current_month - birth_month)
						age_day = abs(current_day - birth_day)
						print("Your age is " , age_year , " Years," , age_month , " Months and" , age_day , " Days")
					elif command == "programver":
						print(" Calculator Suite: 2.00 ")
						print("  Calc+ 1.00")
						print("  Calc- 1.00")
						print("  Calc* 1.00")
						print("  Calc/ 2.00")
						print("  CalcSQRT 1.00")
						print(" RandomNumber 1.00")
						print(" Chat 3.01")
						print(" PY Browser ")
						print(" Table 1.00")
						print(" Calendar 1.00")
						print(" Date and Time Manager 1.00")
						print(" NeoCommand 7.00")
					elif command == "py-dos":
						print(" PY-DOS Version Version History")
						print("   PY-DOS 1")
						print("   PY-DOS 2")
						print("   PY-DOS 2.5")
						print("   PY-DOS 3")
						print("   PY-DOS 3.1")
						print("   PY-DOS 4")
						print("   PY-DOS 5")
						print("   PY-DOS 6")
						print("   PY-DOS 7 ---> Current Version")
					elif command == "microsoft":
						print("Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.")
					elif command == "google":
						print("Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple.")
					elif command == "apple":
						print("Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five companies in the U.S. information technology industry, along with Amazon, Google, Microsoft, and Facebook. It is one of the most popular smartphone and tablet companies in the world.")
					elif command == "facebook":
						print("Facebook is a for-profit corporation and online social networking service based in Menlo Park, California, United States. The Facebook website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.")
					elif command == "amazon":
						print("Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as one of the most influential economic and cultural forces in the world, as well as the world's most valuable brand.")
					elif command == "newupdates":
						print(" Expected changes to come in next version of PY-DOS")
						print("   An updated new calculator in PY-DOS 8 --> Under Developent")
						print("   New Easter-Egg command --> May Come")
					elif command == "table":
						print("This program is written in Python!!!")
						num = int(input("Enter the number : "))
						i = 1
						print("Here you go!!!") 
						while i<=10:
							num = num * 1
							print(num,'x',i,'=',num*i)
							i += 1
					elif command == "clock":
						from turtle import *
						from datetime import datetime

						def jump(distanz, winkel=0):
							penup()
							right(winkel)
							forward(distanz)
							left(winkel)
							pendown()

						def hand(laenge, spitze):
							fd(laenge*1.15)
							rt(90)
							fd(spitze/2.0)
							lt(120)
							fd(spitze)
							lt(120)
							fd(spitze)
							lt(120)
							fd(spitze/2.0)

						def make_hand_shape(name, laenge, spitze):
							reset()
							jump(-laenge*0.15)
							begin_poly()
							hand(laenge, spitze)
							end_poly()
							hand_form = get_poly()
							register_shape(name, hand_form)

						def clockface(radius):
							reset()
							pensize(7)
							for i in range(60):
								jump(radius)
								if i % 5 == 0:
									fd(25)
									jump(-radius-25)
								else:
									dot(3)
									jump(-radius)
								rt(6)

						def setup():
							global second_hand, minute_hand, hour_hand, writer
							mode("logo")
							make_hand_shape("second_hand", 125, 25)
							make_hand_shape("minute_hand",  130, 25)
							make_hand_shape("hour_hand", 90, 25)
							clockface(160)
							second_hand = Turtle()
							second_hand.shape("second_hand")
							second_hand.color("gray20", "gray80")
							minute_hand = Turtle()
							minute_hand.shape("minute_hand")
							minute_hand.color("blue1", "red1")
							hour_hand = Turtle()
							hour_hand.shape("hour_hand")
							hour_hand.color("blue3", "red3")
							for hand in second_hand, minute_hand, hour_hand:
								hand.resizemode("user")
								hand.shapesize(1, 1, 3)
								hand.speed(0)
							ht()
							writer = Turtle()
							#writer.mode("logo")
							writer.ht()
							writer.pu()
							writer.bk(85)

						def wochentag(t):
							wochentag = ["Monday", "Tuesday", "Wednesday",
								"Thursday", "Friday", "Saturday", "Sunday"]
							return wochentag[t.weekday()]

						def datum(z):
							monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
									 "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
							j = z.year
							m = monat[z.month - 1]
							t = z.day
							return "%s %d %d" % (m, t, j)

						def tick():
							t = datetime.today()
							sekunde = t.second + t.microsecond*0.000001
							minute = t.minute + sekunde/60.0
							stunde = t.hour + minute/60.0
							try:
								tracer(False)  # Terminator can occur here
								writer.clear()
								writer.home()
								writer.forward(65)
								writer.write(wochentag(t),
											 align="center", font=("Courier", 14, "bold"))
								writer.back(150)
								writer.write(datum(t),
											 align="center", font=("Courier", 14, "bold"))
								writer.forward(85)
								tracer(True)
								second_hand.setheading(6*sekunde)  # or here
								minute_hand.setheading(6*minute)
								hour_hand.setheading(30*stunde)
								tracer(True)
								ontimer(tick, 100)
							except Terminator:
								pass  # turtledemo user pressed STOP

						def main():
							tracer(False)
							setup()
							tracer(True)
							tick()
							return "EVENTLOOP"

						if __name__ == "__main__":
							mode("logo")
							msg = main()
							print(msg)
							mainloop()
					elif command == "who made you":
						print("Gautham Nair!!!")
					elif command == "who made you?":
						print("Gautham Nair!!!")
					elif command == "do you know gautham":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham?":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham nair":
						print("Oh, yeah, he created me!!")
					elif command == "do you know gautham nair?":
						print("Oh, yeah, he created me!!")
					elif command == "do you know zanvok corporation":
						print("Sure, I do!!...A great company...!!!")
					elif command == "do you know zanvok corporation?":
						print("Sure, I do!!...A great company...!!!")
					elif command == "do you know zanvok":
						print("Sure!! Zanvok Corporation is awesome!!")
					elif command == "do you know zanvok?":
						print("Sure!! Zanvok Corporation is awesome!!")
					elif command == "neofetch":
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("**********     **********")
						print(" **********   **********")
						print("  ********** **********")
						print(" **********   **********")
						print("**********     **********")
						print("            7")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 7")
						print("Sleepy Sloth")
						print("------------------------------------")
						print("Written in Python")
						print("---------------------------------------")
						print("Zanvok Corporation")	
					elif command == "help":
						print("Commands for using PY-DOS")
						print(" calc+ - addition calculator")
						print(" calc- - subtraction calculator")
						print(" calc/ - division calculator")
						print(" calc* - multiplication calculator")
						print(" calcsqrt - square root calculator")
						print(" age calc - age calculator")
						print(" table - display table")
						print(" py-dos - PY-DOS Version History")
						print(" browser - starts PY Browser, a PyQt-Chromium based browser")
						print(" about - about PY-DOS")
						print(" status - PY-DOS Update and Base Version Details")
						print(" credits - display credits")
						print(" user - display user information")
						print(" change username - changes your username")
						print(" date - displays date")
						print(" time - display time")
						print(" date and time - display date and time")
						print(" chat - start a chat with PY-DOS")
						print(" clock - displays clock, inaccessible sometimes")
						print(" calendar - display calendar for the provided month and year")
						print(" randomnumber - generates a random number between 0 to 9")
						print(" programver - display version of all programs in PY-DOS")
					elif command == "about":
						print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
					elif command == "status":
						print(" PY-DOS Version & Update Status")
						print("  Version: 7 Sleepy Sleepy")
						print("  About Update")
						print("   Update Name: 3JLY")
						print("   Update Version: 2021.7.7")
						print("   PY-DOS Base Version: 2.00")
					elif command == "calc+":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type the first number: ")
						second_number = input("Type the second number: ")
						sum = float(first_number) + float(second_number)
						print(sum)
					elif command == "change username":
						userInput = input("Type current UserName: ")
						if userInput == user_name:
							userInput = input("Password?\n")
							if userInput == password:
								print("Change UserName")
							else:
								print("That is the wrong password.")
								break
						else:
								print("That is the wrong username.")
								break

						user_name = input("Type user name: ")
						print("Username changed to " + user_name)	
					elif command == "user":
						print("Name: " + first_name + " " + last_name)
						print("UserName: " + user_name)	
					elif command == "calc-":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						diff = float(first_number) - float(second_number)
						print(diff)
					elif command == "calc/":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						div = float(first_number) / float(second_number)
						print("your answer is ")
						print(div)
					elif command == "calc*":
						print("This program is written in Python for PY-DOS!! ")
						first_number = input("Type first number: ")
						second_number = input("Type second number: ")
						mul = float(first_number) * float(second_number)
						print(mul)	
					elif command == "calcsqrt":
						sqrt = input("Type the number: ")
						import math
						print(math.sqrt(float(sqrt)))	
					elif command == "date":
						from datetime import datetime

						now = datetime.now()
						date = now.strftime("%d/%m/%Y ")
						print("Date =", date)
					elif command == "time":
						from datetime import datetime

						now = datetime.now()
						time = now.strftime("%H:%M:%S")
						print("Time =", time)	
					elif command == "date and time":
						from datetime import datetime

						now = datetime.now()
						datetime = now.strftime("%d/%m/%Y  %H:%M:%S ")
						print("Date and Time =", datetime)	
					elif command == "time and date":
						from datetime import datetime

						now = datetime.now()
						datetime = now.strftime("%H:%M:%S %d/%m/%Y   ")
						print("Time and Date =", datetime)
					elif command == "calendar":
						import calendar
						yy = int(input("Enter Year: "))
						mm = int(input("Enter Month: "))
						print(calendar.month(yy , mm))
					elif command == "neofire":
						print("PY-DOS")
						print("Written in Python")
						print("Version 7")
						print("Sleepy Sloth")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 6 Panicked Pig")
						print("Python ")
						print("Build number: 6000.98")
						print("Build version: Sleepy Sloth")
					elif command == "chat":
						print("Hello! " + first_name +  " " + last_name + "😀")
						print("Welcome to PY-DOS Chat  {Preview}")
						chat_1 = input("How are you? [sad/happy/frustrated/bored/angry/confused] ")
						sad_var = "sad"
						zc_var = "do you know Zanvok Corporation"
						creation_var = "Who created you"
						happy_var = "happy"
						angry_var = "angry"
						frustrated_var = "frustrated"
						confused_var = "confused"
						bored_var = "bored"
			
						if chat_1 == sad_var:
							print("😢!!! Sad?? ")
							sad_reason = input("Tell me the reason why you are sad??")
							print("OK, so that's the reason")
						elif chat_1 == zc_var:
							print("There is no better place than home")
						elif chat_1 == creation_var:
							print("Gautham Nair")
						elif chat_1 == happy_var:
							print("😄, I'am happy to hear that!!!")
						elif chat_1 == angry_var:
							print("😠, Angry??")
							angry_reason = input("Tell me the reason why are you angry??")
							print("OK")
						elif chat_1 == frustrated_var:
							print("Why are you frustrated? ")
							frustrated_reason = input("What!! happened??!!")
							print("OK!!!")
						elif chat_1 == bored_var:
							print("Well, I can recommend you a few things!!")
							print("You can play games, watch movies, or explore PY-DOS!!")
						elif chat_1 == creation_var:
							print("Gautham Nair!!")
						elif chat_1 == zc_var:
							print("There is no better place than home")	
						elif chat_1 == confused_var:
							print("Confused what to do???")
							confused_sol = input("Any addition , subtraction , division , multiplication , or square root??")
							yes_var = "yes"
							no_var = "no"
							if confused_sol == yes_var:
								print(" Type calc+ for + , calc- for - , calc/ for / , calc* for * , calcsqrt for square root")
								if command == "calc+":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type the first number: ")
									second_number = input("Type the second number: ")
									sum = float(first_number) + float(second_number)
									print(sum)
						
								elif command == "calc-":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									diff = float(first_number) - float(second_number)
									print(diff)
								elif command == "calc/":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									div = float(first_number) / float(second_number)
									print(div)
								elif command == "calc*":
									print("This program is written in Python for PY-DOS!! ")
									first_number = input("Type first number: ")
									second_number = input("Type second number: ")
									mul = float(first_number) * float(second_number)
									print(mul)	
								elif command == "calcsqrt":
									sqrt = input("Type the number: ")
									import math
									print(math.sqrt(float(sqrt)))
							elif confused_sol == no_var:
								print("Ok!!!")					  	 
						else:
							print("Sorry, I didn't understand that!!")	
				
					elif command == "exit":
						break
					else:
						print("Bad command...Command not found!!")
			else:
				print("Oops!! password didn't match!!")
				print("This program will terminate now")
