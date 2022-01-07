print("Welcome to PY-DOS")
print("Version 6 Panicked Pig")
print("Developed by Gautham Nair")
first_name = input("Type your First Name: ")
#Non-Loop Program....
#Only If and While commands...
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
					command = input(user_name + "@" + pc_name + " :" + "~" + " >").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "version":
						print("PY-DOS version-6")
					elif command == "py-dos":
						print(" PY-DOS Version Version History")
						print("   PY-DOS 1")
						print("   PY-DOS 2")
						print("   PY-DOS 2.5")
						print("   PY-DOS 3")
						print("   PY-DOS 3.1")
						print("   PY-DOS 4")
						print("   PY-DOS 5")
						print("   PY-DOS 6  ---> Current Version")
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
						print("            6")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 6")
						print("Panicked Pig")
						print("------------------------------------")
						print("Written in Python")
						print("---------------------------------------")
						print("Zanvok Corporation")	
					elif command == "help":
						print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; change username - Changes the username ; chat - Start a chat with PY-DOS; table - this command starts a table program")
					elif command == "about":
						print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
					elif command == "status":
						print(" PY-DOS Version & Update Status")
						print("  Version: 6 Panicked Pig")
						print("  About Update")
						print("   Update Name: 2JLY")
						print("   Update Version: 2021.7.6")
						print("   PY-DOS Base Version: 1.00")
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
					elif command == "neofire":
						print("PY-DOS")
						print("Written in Python")
						print("Version 6")
						print("Panicked Pig")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 5 Wise Wolf")
						print("Python ")
						print("Build number: 5000.65")
						print("Build version: Panicked Pig")
					elif command == "chat":
						print("Hello! " + first_name +  " " + last_name + "😀")
						print("Welcome to PY-DOS Chat  {Alpha}")
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
							print("You can play games, watch movies, or find out  secret codes in PY-DOS!!")
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
						command = input(user_name + "@" + pc_name + " :" + "~" + " >").lower()
						if command == "credits":
							print("________________________")
							print("Gautham Nair")
							print("------------------------")
							print("Zanvok Corporation")
						elif command == "version":
							print("PY-DOS version-6")
						elif command == "py-dos":
							print(" PY-DOS Version Version History")
							print("   PY-DOS 1")
							print("   PY-DOS 2")
							print("   PY-DOS 2.5")
							print("   PY-DOS 3")
							print("   PY-DOS 3.1")
							print("   PY-DOS 4")
							print("   PY-DOS 5")
							print("   PY-DOS 6  ---> Current Version")
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
							print(" Expected changes to come in next versions of PY-DOS")
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
							print("            6")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("PY-DOS ")
							print("-----------------")
							print("Version 6")
							print("Panicked Pig")
							print("------------------------------------")
							print("Written in Python")
							print("---------------------------------------")
							print("Zanvok Corporation")	
						elif command == "help":
							print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; change username - Changes the username ; chat - Start a chat with PY-DOS; table - this command starts a table program")
						elif command == "about":
							print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
						elif command == "status":
							print(" PY-DOS Version & Update Status")
							print("  Version: 6 Panicked Pig")
							print("  About Update")
							print("   Update Name: 2JLY")
							print("   Update Version: 2021.7.6")
							print("   PY-DOS Base Version: 1.00")
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
						elif command == "neofire":
							print("PY-DOS")
							print("Written in Python")
							print("Version 6")
							print("Panicked Pig")
							print("Developed by Gautham Nair")
							print("Updated version of PY-DOS 5 Wise Wolf")
							print("Python ")
							print("Build number: 5000.65")
							print("Build version: Panicked Pig")
						elif command == "chat":
							print("Hello! " + first_name +  " " + last_name + "😀")
							print("Welcome to PY-DOS Chat  {Alpha}")
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
								print("You can play games, watch movies, or find out  secret codes in PY-DOS!!")
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
						command = input(user_name + "@" + pc_name + " :" + "~" + " >").lower()
						if command == "credits":
							print("________________________")
							print("Gautham Nair")
							print("------------------------")
							print("Zanvok Corporation")
						elif command == "version":
							print("PY-DOS version-6")
						elif command == "py-dos":
							print(" PY-DOS Version Version History")
							print("   PY-DOS 1")
							print("   PY-DOS 2")
							print("   PY-DOS 2.5")
							print("   PY-DOS 3")
							print("   PY-DOS 3.1")
							print("   PY-DOS 4")
							print("   PY-DOS 5")
							print("   PY-DOS 6  ---> Current Version")
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
							print(" Expected changes to come in next versions of PY-DOS")
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
							print("            6")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("PY-DOS ")
							print("-----------------")
							print("Version 6")
							print("Panicked Pig")
							print("------------------------------------")
							print("Written in Python")
							print("---------------------------------------")
							print("Zanvok Corporation")	
						elif command == "help":
							print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; change username - Changes the username ; chat - Start a chat with PY-DOS; table - this command starts a table program")
						elif command == "about":
							print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
						elif command == "status":
							print(" PY-DOS Version & Update Status")
							print("  Version: 6 Panicked Pig")
							print("  About Update")
							print("   Update Name: 2JLY")
							print("   Update Version: 2021.7.6")
							print("   PY-DOS Base Version: 1.00")
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
						elif command == "neofire":
							print("PY-DOS")
							print("Written in Python")
							print("Version 6")
							print("Panicked Pig")
							print("Developed by Gautham Nair")
							print("Updated version of PY-DOS 5 Wise Wolf")
							print("Python ")
							print("Build number: 5000.65")
							print("Build version: Panicked Pig")
						elif command == "chat":
							print("Hello! " + first_name +  " " + last_name + "😀")
							print("Welcome to PY-DOS Chat  {Alpha}")
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
								print("You can play games, watch movies, or find out  secret codes in PY-DOS!!")
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
					command = input(user_name + "@" + pc_name + " :" + "~" + " >").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "version":
						print("PY-DOS version-6")
					elif command == "py-dos":
						print(" PY-DOS Version Version History")
						print("   PY-DOS 1")
						print("   PY-DOS 2")
						print("   PY-DOS 2.5")
						print("   PY-DOS 3")
						print("   PY-DOS 3.1")
						print("   PY-DOS 4")
						print("   PY-DOS 5")
						print("   PY-DOS 6  ---> Current Version")
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
						print(" Expected changes to come in next versions of PY-DOS")
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
						print("            6")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 6")
						print("Panicked Pig")
						print("------------------------------------")
						print("Written in Python")
						print("---------------------------------------")
						print("Zanvok Corporation")	
					elif command == "help":
						print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; change username - Changes the username ; chat - Start a chat with PY-DOS; table - this command starts a table program")
					elif command == "about":
						print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
					elif command == "status":
						print(" PY-DOS Version & Update Status")
						print("  Version: 6 Panicked Pig")
						print("  About Update")
						print("   Update Name: 2JLY")
						print("   Update Version: 2021.7.6")
						print("   PY-DOS Base Version: 1.00")
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
					elif command == "neofire":
						print("PY-DOS")
						print("Written in Python")
						print("Version 6")
						print("Panicked Pig")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 5 Wise Wolf")
						print("Python ")
						print("Build number: 5000.65")
						print("Build version: Panicked Pig")
					elif command == "chat":
						print("Hello! " + first_name +  " " + last_name + "😀")
						print("Welcome to PY-DOS Chat  {Alpha}")
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
							print("You can play games, watch movies, or find out  secret codes in PY-DOS!!")
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
					command = input(user_name + "@" + pc_name + " :" + "~" + " >").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "version":
						print("PY-DOS version-6")
					elif command == "py-dos":
						print(" PY-DOS Version Version History")
						print("   PY-DOS 1")
						print("   PY-DOS 2")
						print("   PY-DOS 2.5")
						print("   PY-DOS 3")
						print("   PY-DOS 3.1")
						print("   PY-DOS 4")
						print("   PY-DOS 5")
						print("   PY-DOS 6  ---> Current Version")
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
						print(" Expected changes to come in next versions of PY-DOS")
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
						print("            6")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 6")
						print("Panicked Pig")
						print("------------------------------------")
						print("Written in Python")
						print("---------------------------------------")
						print("Zanvok Corporation")	
					elif command == "help":
						print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; change username - Changes the username ; chat - Start a chat with PY-DOS; table - this command starts a table program")
					elif command == "about":
						print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
					elif command == "status":
						print(" PY-DOS Version & Update Status")
						print("  Version: 6 Panicked Pig")
						print("  About Update")
						print("   Update Name: 2JLY")
						print("   Update Version: 2021.7.6")
						print("   PY-DOS Base Version: 1.00")
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
					elif command == "neofire":
						print("PY-DOS")
						print("Written in Python")
						print("Version 6")
						print("Panicked Pig")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 5 Wise Wolf")
						print("Python ")
						print("Build number: 5000.65")
						print("Build version: Panicked Pig")
					elif command == "chat":
						print("Hello! " + first_name +  " " + last_name + "😀")
						print("Welcome to PY-DOS Chat  {Alpha}")
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
							print("You can play games, watch movies, or find out  secret codes in PY-DOS!!")
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