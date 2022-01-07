print("Welcome to PY-DOS")
print("Version 3.1 Curious Cat")
first_name = input("Type your First Name: ")
last_name = input("Type your Last Name: ")
user_name = input("Type your User Name: ")
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
            print("PY-DOS version-3.1")
        elif command == "table":
        	print("This program is written in Python!!!")
        	num = int(input("Enter the number : "))
        	i = 1
        	print("Here you go!!!") 
        	while i<=10:
        		num = num * 1
        		print(num,'x',i,'=',num*i)
        		i += 1
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
            print("           3.1")
            print("---------------------------------------------")
            print("---------------------------------------------")
            print("---------------------------------------------")
            print("---------------------------------------------")
            print("PY-DOS ")
            print("-----------------")
            print("Version 3.1")
            print("------------------------------------")
            print("Written in Python")
            print("---------------------------------------")
            print("Zanvok Corporation")	
        elif command == "help":
            print("version - Displays the version of PY-DOS; help - Displays this help page; exit - Quits PY-DOS; about - Displays information about PY-DOS; calc+ - This command starts addition calculator; calc- - This command starts subtraction calculator; calc/ - This command starts division calculator; calc* - This starts multiplication calculator; calcsqrt - This starts square root calculator; user - Displays user info; replace username - Changes the username ; chat - Start a chat with PY-DOS; table - this command starts a table program")
        elif command == "about":
                print("PY-DOS (Python-Disk Operating System) is written in Python!! ")
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
            	sketch.left(90) 
            print("PY-DOS")
            print("Written in Python")
            print("Version 3.1")
            print("Developed by Gautham Nair")
            print("Updated version of PY-DOS 3.00")
            print("Added new Table feature!!, just use 'table' command to view tables")
            print("Build number: 2021.221x2")
            print("Build version: 21JN2")
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
