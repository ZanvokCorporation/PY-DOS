print("Welcome to PY-DOS")
first_name = input("Type your First Name: ")
last_name = input("Type your Last Name: ")
user_name = input("Type your User Name: ")
password = input("Password: ")
print("Welcome! " + first_name  + " " +  last_name)
print("You are signed in as " + user_name)
command = ""
while command != "quit":
	command = input("> ").lower()
	if command == "credits":
		print("________________________")
		print("Gautham Nair")
		print("------------------------")
		print("Zanvok Corporation")
	elif command == "version":
		print("PY-DOS version-1.00 beta")
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
		print("---------------------------------------------")
		print("---------------------------------------------")
		print("---------------------------------------------")
		print("---------------------------------------------")
		print("PY-DOS ")
		print("-----------------")
		print("Version 1.00 BETA")
		print("------------------------------------")
		print("Made using Python")
		print("---------------------------------------")
		print("Zanvok Corporation")	
	elif command == "help":
		print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; replace username - Changes the username ; chat - Start a chat with PY-DOS")
	elif command == "about":
        	print("PY-DOS (Python-Disk Operating System) is made using Python!! ")
	elif command == "calc+":
		print("This program is written in Python for PY-DOS!! ")
		first_number = input("Type the first number: ")
		second_number = input("Type the second number: ")
		sum = float(first_number) + float(second_number)
		print(sum)
	elif command == "replace username":
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
		import turtle
		t = turtle.pen()
		colors = [ "blue","white","yellow","green","purple","red"]
		sketch = turtle.Pen()
		turtle.bgcolor("black")
		for i in range(200):
 		  sketch.pencolor(colors[i % 6])
 		  sketch.width(i/100 + 1)
 		  sketch.forward(i)
 		  sketch.left(59) 
		print("PY-DOS")
		print("Created using Python")
		print("214 lines of code")
		print("Developed by Gautham Nair")
		print("Took 5 days to complete")
		print("Version 1.00 Beta")
		print("Build version 2021.214")
	elif command == "chat":
		print("Hello! " + first_name +  " " + last_name + "😀")
		print("Welcome to PY-DOS Chat  {Beta}")
		chat_1 = input("How are you? [sad/happy/frustrated/bored/angry/confused] ")
		sad_var = "sad"
		happy_var = "happy"
		angry_var = "angry"
		frustrated_var = "frustrated"
		confused_var = "confused"
		bored_var = "bored"
		zc_var = "do you know Zanvok Corporation?"
		creation_var = "Who created you?"
		if chat_1 == sad_var:
			print("😢!!! Why are you sad?? ")
			sad_reason = input("Say me the reason why you are sad??")
			print("OK, so that's the reason")
		elif chat_1 == happy_var:
			print("😄, I'am happy to hear that!!!")
		elif chat_1 == angry_var:
			print("😠, Why are you angry??")
			angry_reason = input("Tell me the reason why are you angry??")
			print("OK")
		elif chat_1 == frustrated_var:
			print("Why are you frustrated? ")
			frustrated_reason = input("What!! happened??!!")
			print("OK!!!")
		elif chat_1 == bored_var:
			print("Well, I can recommend you a few things!!")
			bored_sol = input("Shall I ?? [yes/no]")
			yes_var = "yes"
			no_var = "no"
			if bored_sol == yes_var:
				print("Well, you can play games, watch movies, or find out  secret codes in PY-DOS!!")
		elif bored_sol == no_var:	 
			print("OK")
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
			print("Sorry, I can only understand a few things..!!..I'am still learning")	
			
	elif command == "exit":
		break
	else:
		print("Bad command!!")
