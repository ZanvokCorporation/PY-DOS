#!/usr/bin/env python3
print("Welcome to PY-DOS")
print("Version 8 Mutated Monkey Developer Preview")
print("Developed by Gautham Nair")
first_name = input("Type your First Name: ")
pydos_ver = "8"
dev = "Developer Preview and Development , Build 7000.98 , PY-DOS 8 , Mutated Monkey"
calc_ver = "2.5 Unicorn"
calendar_ver = "1.00"
randomnumber_ver = "1.00"
chat_ver = "3.01"
table_ver = "1.00"
dtm_ver = "1.00"
neocommand_ver = "8"
#Major Update (2AUG)
#PY-DOS Base Version 2.5 Unicorn
#Non-Loop Program....
#Only If and Else commands...
#Developer Preview and Development
#Released on 02-08-2021 10:00 AM IST
#Gautham Nair
#Suraj Varma
#Adithya Vijayan
#Zanvok Corporation
#Browser now integrated with PY-DOS 8
#Recommended to keep in the directory: C:\\Py
#Also create another directoy in C: drive as My Websites
#C:\\My Websites
#C:\\Py
#Python
#Python Software Foundation
#Guido Van Rossum
#Created using Visual Studio 2022 Preview Community, Python 3.10 IDLE and Visual Studio Code in a Windows 11 System
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
					command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(DEV)" + "$ ").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "games":
						print("Welcome to PY Game Center")
						print("Available Games")
						print(" PY Snake")
						print(" PY Pong")
						game = ""
						while game != "quit":
							game = input("Enter 1 to play Snake, enter 2 to play Pong \n")
							if game == "1":
								import turtle
								import random
								
								w = 500
								h = 500
								food_size = 10
								delay = 100
								
								offsets = {
									"up": (0, 20),
									"down": (0, -20),
									"left": (-20, 0),
									"right": (20, 0)
								}
								
								def reset():
									global snake, snake_dir, food_position, pen
									snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
									snake_dir = "up"
									food_position = get_random_food_position()
									food.goto(food_position)
									move_snake()
									
								def move_snake():
									global snake_dir
								
									new_head = snake[-1].copy()
									new_head[0] = snake[-1][0] + offsets[snake_dir][0]
									new_head[1] = snake[-1][1] + offsets[snake_dir][1]
								
									
									if new_head in snake[:-1]:
										reset()
									else:
										snake.append(new_head)
								
									
										if not food_collision():
											snake.pop(0)
								
								
										if snake[-1][0] > w / 2:
											snake[-1][0] -= w
										elif snake[-1][0] < - w / 2:
											snake[-1][0] += w
										elif snake[-1][1] > h / 2:
											snake[-1][1] -= h
										elif snake[-1][1] < -h / 2:
											snake[-1][1] += h
								
								
										pen.clearstamps()
								
										
										for segment in snake:
											pen.goto(segment[0], segment[1])
											pen.stamp()
								
										
										screen.update()
								
										turtle.ontimer(move_snake, delay)
								
								def food_collision():
									global food_position
									if get_distance(snake[-1], food_position) < 20:
										food_position = get_random_food_position()
										food.goto(food_position)
										return True
									return False
								
								def get_random_food_position():
									x = random.randint(- w / 2 + food_size, w / 2 - food_size)
									y = random.randint(- h / 2 + food_size, h / 2 - food_size)
									return (x, y)
								
								def get_distance(pos1, pos2):
									x1, y1 = pos1
									x2, y2 = pos2
									distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
									return distance
								def go_up():
									global snake_dir
									if snake_dir != "down":
										snake_dir = "up"
								
								def go_right():
									global snake_dir
									if snake_dir != "left":
										snake_dir = "right"
								
								def go_down():
									global snake_dir
									if snake_dir!= "up":
										snake_dir = "down"
								
								def go_left():
									global snake_dir
									if snake_dir != "right":
										snake_dir = "left"
								
								
								screen = turtle.Screen()
								screen.setup(w, h)
								screen.title("Snake")
								screen.bgcolor("blue")
								screen.setup(500, 500)
								screen.tracer(0)
								
								
								pen = turtle.Turtle("square")
								pen.penup()
								
								
								food = turtle.Turtle()
								food.shape("square")
								food.color("yellow")
								food.shapesize(food_size / 20)
								food.penup()
								
								
								screen.listen()
								screen.onkey(go_up, "Up")
								screen.onkey(go_right, "Right")
								screen.onkey(go_down, "Down")
								screen.onkey(go_left, "Left")
								
								
								reset()
								turtle.done()
							elif game == "2":
								from random import choice, random
								from turtle import *

								from freegames import vector


								def value():
									"Randomly generate value between (-5, -3) or (3, 5)."
									return (3 + random() * 2) * choice([1, -1])


								ball = vector(0, 0)
								aim = vector(value(), value())
								state = {1: 0, 2: 0}


								def move(player, change):
									"Move player position by change."
									state[player] += change


								def rectangle(x, y, width, height):
									"Draw rectangle at (x, y) with given width and height."
									up()
									goto(x, y)
									down()
									begin_fill()
									for count in range(2):
										forward(width)
										left(90)
										forward(height)
										left(90)
									end_fill()


								def draw():
									"Draw game and move pong ball."
									clear()
									rectangle(-200, state[1], 10, 50)
									rectangle(190, state[2], 10, 50)

									ball.move(aim)
									x = ball.x
									y = ball.y

									up()
									goto(x, y)
									dot(10)
									update()

									if y < -200 or y > 200:
										aim.y = -aim.y

									if x < -185:
										low = state[1]
										high = state[1] + 50

										if low <= y <= high:
											aim.x = -aim.x
										else:
											return

									if x > 185:
										low = state[2]
										high = state[2] + 50

										if low <= y <= high:
											aim.x = -aim.x
										else:
											return

									ontimer(draw, 50)

								setup(420, 420, 370, 0)
								hideturtle()
								tracer(False)
								listen()
								onkey(lambda: move(1, 40), 'w')
								onkey(lambda: move(1, -40), 's')
								onkey(lambda: move(2, 40), 'Up')
								onkey(lambda: move(2, -40), 'Down')
								draw()
								done()

					elif command == "spinner":
						from turtle import *
						state = {'turn': 0}
						val = float(input("Enter speed (in number): "))
						def spinner():
							clear()
							angle = state['turn']/10
							right(angle)
							forward(100)
							dot(120, 'red')
							back(100)
							right(120)
							forward(100)
							dot(120, 'purple')
							back(100)
							right(120)
							forward(100)
							dot(120, 'blue')
							back(100)
							right(120)
							update()
						def animate():
							if state['turn']>0:
								state['turn']-=1

							spinner()
							ontimer(animate, 20)
						def flick():
							state['turn']+=val

						setup(420, 420, 370, 0)
						hideturtle()
						tracer(False)
						width(20)
						onkey(flick, 'Right')
						onkey(flick, 'Left')
						onkey(flick, 'Up')
						onkey(flick, 'Down')
						onkey(flick, 'space')
						onkey(flick, 'w')
						onkey(flick, 'a')
						onkey(flick, 's')
						onkey(flick, 'd')
						listen()
						animate()
						done()

					elif command == "version":
						print("PY-DOS version-8")
					elif command == "randomnumber":
						print("Generates random number from 0 to 9")
						import random
						print(random.randint(0,9))
					elif command == "browser":
						print("PY-Browser for PY-DOS")
						# importing required libraries
						from PyQt5.QtCore import *
						from PyQt5.QtWidgets import *
						from PyQt5.QtGui import *
						from PyQt5.QtWebEngineWidgets import *
						from PyQt5.QtPrintSupport import *
						import os
						import sys

						# creating main window class
						class MainWindow(QMainWindow):

							# constructor
							def __init__(self, *args, **kwargs):
								super(MainWindow, self).__init__(*args, **kwargs)


								# creating a QWebEngineView
								self.browser = QWebEngineView()

								# setting default browser url as google
								self.browser.setUrl(QUrl("file:///C://My Websites/browser.html"))

								# adding action when url get changed
								self.browser.urlChanged.connect(self.update_urlbar)

								# adding action when loading is finished
								self.browser.loadFinished.connect(self.update_title)

								# set this browser as central widget or main window
								self.setCentralWidget(self.browser)

								# creating a status bar object
								self.status = QStatusBar()

								# adding status bar to the main window
								self.setStatusBar(self.status)

								# creating QToolBar for navigation
								navtb = QToolBar("Navigation")

								# adding this tool bar tot he main window
								self.addToolBar(navtb)

								# adding actions to the tool bar
								# creating a action for back
								back_btn = QAction("Back", self)

								# setting status tip
								back_btn.setStatusTip("Back to previous page")

								# adding action to the back button
								# making browser go back
								back_btn.triggered.connect(self.browser.back)

								# adding this action to tool bar
								navtb.addAction(back_btn)

								# similarly for forward action
								next_btn = QAction("Forward", self)
								next_btn.setStatusTip("Forward to next page")

								# adding action to the next button
								# making browser go forward
								next_btn.triggered.connect(self.browser.forward)
								navtb.addAction(next_btn)

								# similarly for reload action
								reload_btn = QAction("Reload", self)
								reload_btn.setStatusTip("Reload page")

								# adding action to the reload button
								# making browser to reload
								reload_btn.triggered.connect(self.browser.reload)
								navtb.addAction(reload_btn)

								# similarly for home action
								home_btn = QAction("Home", self)
								home_btn.setStatusTip("Go home")
								home_btn.triggered.connect(self.navigate_home)
								navtb.addAction(home_btn)

								# adding a separator in the tool bar
								navtb.addSeparator()

								# creating a line edit for the url
								self.urlbar = QLineEdit()

								# adding action when return key is pressed
								self.urlbar.returnPressed.connect(self.navigate_to_url)

								# adding this to the tool bar
								navtb.addWidget(self.urlbar)

								# adding stop action to the tool bar
								stop_btn = QAction("Stop", self)
								stop_btn.setStatusTip("Stop loading current page")

								# adding action to the stop button
								# making browser to stop
								stop_btn.triggered.connect(self.browser.stop)
								navtb.addAction(stop_btn)

								# showing all the components
								self.show()


							# method for updating the title of the window
							def update_title(self):
								title = self.browser.page().title()
								self.setWindowTitle("% s - PY Browser" % title)


							# method called by the home action
							def navigate_home(self):

								# open the google
								self.browser.setUrl(QUrl("file:///C://My Websites/browser.html"))

							# method called by the line edit when return key is pressed
							def navigate_to_url(self):

								# getting url and converting it to QUrl objetc
								q = QUrl(self.urlbar.text())

								# if url is scheme is blank
								if q.scheme() == "":
									# set url scheme to html
									q.setScheme("http")

								# set the url to the browser
								self.browser.setUrl(q)

							# method for updating url
							# this method is called by the QWebEngineView object
							def update_urlbar(self, q):

								# setting text to the url bar
								self.urlbar.setText(q.toString())

								# setting cursor position of the url bar
								self.urlbar.setCursorPosition(0)


						# creating a pyQt5 application
						app = QApplication(sys.argv)

						# setting name to the application
						app.setApplicationName("PY-Browser")

						# creating a main window object
						window = MainWindow()

						# loop
						app.exec_()

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
						print("  Calc/ 2.5 Unicorn")
						print("  CalcSQRT 1.00")
						print("  AgeCalc 1.00(BETA)")
						print(" RandomNumber " + randomnumber_ver)
						print(" Chat " + chat_ver)
						print(" PY Browser MM8.1 ")
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
						print("   PY-DOS 7")
						print("   PY-DOS 8 ---> Current version")
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
						print(" Expected changes to come in this version of PY-DOS")
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
						print("            8")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 8")
						print("Mutated Monkey")
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
						print("  Version: 8 Mutated Monkey")
						print("  About Update")
						print("   Update Name: 2AUG")
						print("   Update Version: 2021.8.2")
						print("   PY-DOS Base Version: 2.5 Unicorn")
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
						print("Version 8")
						print("Mutated Monkey")
						print("Type: Developer Preview and Development ")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 7 Sleepy Sloth")
						print("Python ")
						print("Build number: 7000.98")
						print("Build version: Mutated Monkey")
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
						command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(DEV)").lower()
						if command == "credits":
							print("________________________")
							print("Gautham Nair")
							print("------------------------")
							print("Zanvok Corporation")
						elif command == "games":
							print("Welcome to PY Game Center")
							print("Available Games")
							print(" PY Snake")
							print(" PY Pong")
							game = ""
							while game != "quit":
								game = input("Enter 1 to play Snake, enter 2 to play Pong \n")
								if game == "1":
									import turtle
									import random
									
									w = 500
									h = 500
									food_size = 10
									delay = 100
									
									offsets = {
										"up": (0, 20),
										"down": (0, -20),
										"left": (-20, 0),
										"right": (20, 0)
									}
									
									def reset():
										global snake, snake_dir, food_position, pen
										snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
										snake_dir = "up"
										food_position = get_random_food_position()
										food.goto(food_position)
										move_snake()
										
									def move_snake():
										global snake_dir
									
										new_head = snake[-1].copy()
										new_head[0] = snake[-1][0] + offsets[snake_dir][0]
										new_head[1] = snake[-1][1] + offsets[snake_dir][1]
									
										
										if new_head in snake[:-1]:
											reset()
										else:
											snake.append(new_head)
									
										
											if not food_collision():
												snake.pop(0)
									
									
											if snake[-1][0] > w / 2:
												snake[-1][0] -= w
											elif snake[-1][0] < - w / 2:
												snake[-1][0] += w
											elif snake[-1][1] > h / 2:
												snake[-1][1] -= h
											elif snake[-1][1] < -h / 2:
												snake[-1][1] += h
									
									
											pen.clearstamps()
									
											
											for segment in snake:
												pen.goto(segment[0], segment[1])
												pen.stamp()
									
											
											screen.update()
									
											turtle.ontimer(move_snake, delay)
									
									def food_collision():
										global food_position
										if get_distance(snake[-1], food_position) < 20:
											food_position = get_random_food_position()
											food.goto(food_position)
											return True
										return False
									
									def get_random_food_position():
										x = random.randint(- w / 2 + food_size, w / 2 - food_size)
										y = random.randint(- h / 2 + food_size, h / 2 - food_size)
										return (x, y)
									
									def get_distance(pos1, pos2):
										x1, y1 = pos1
										x2, y2 = pos2
										distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
										return distance
									def go_up():
										global snake_dir
										if snake_dir != "down":
											snake_dir = "up"
									
									def go_right():
										global snake_dir
										if snake_dir != "left":
											snake_dir = "right"
									
									def go_down():
										global snake_dir
										if snake_dir!= "up":
											snake_dir = "down"
									
									def go_left():
										global snake_dir
										if snake_dir != "right":
											snake_dir = "left"
									
									
									screen = turtle.Screen()
									screen.setup(w, h)
									screen.title("Snake")
									screen.bgcolor("blue")
									screen.setup(500, 500)
									screen.tracer(0)
									
									
									pen = turtle.Turtle("square")
									pen.penup()
									
									
									food = turtle.Turtle()
									food.shape("square")
									food.color("yellow")
									food.shapesize(food_size / 20)
									food.penup()
									
									
									screen.listen()
									screen.onkey(go_up, "Up")
									screen.onkey(go_right, "Right")
									screen.onkey(go_down, "Down")
									screen.onkey(go_left, "Left")
									
									
									reset()
									turtle.done()
								elif game == "2":
									from random import choice, random
									from turtle import *

									from freegames import vector


									def value():
										"Randomly generate value between (-5, -3) or (3, 5)."
										return (3 + random() * 2) * choice([1, -1])


									ball = vector(0, 0)
									aim = vector(value(), value())
									state = {1: 0, 2: 0}


									def move(player, change):
										"Move player position by change."
										state[player] += change


									def rectangle(x, y, width, height):
										"Draw rectangle at (x, y) with given width and height."
										up()
										goto(x, y)
										down()
										begin_fill()
										for count in range(2):
											forward(width)
											left(90)
											forward(height)
											left(90)
										end_fill()


									def draw():
										"Draw game and move pong ball."
										clear()
										rectangle(-200, state[1], 10, 50)
										rectangle(190, state[2], 10, 50)

										ball.move(aim)
										x = ball.x
										y = ball.y

										up()
										goto(x, y)
										dot(10)
										update()

										if y < -200 or y > 200:
											aim.y = -aim.y

										if x < -185:
											low = state[1]
											high = state[1] + 50

											if low <= y <= high:
												aim.x = -aim.x
											else:
												return

										if x > 185:
											low = state[2]
											high = state[2] + 50

											if low <= y <= high:
												aim.x = -aim.x
											else:
												return

										ontimer(draw, 50)


									setup(420, 420, 370, 0)
									hideturtle()
									tracer(False)
									listen()
									onkey(lambda: move(1, 40), 'w')
									onkey(lambda: move(1, -40), 's')
									onkey(lambda: move(2, 40), 'Up')
									onkey(lambda: move(2, -40), 'Down')
									draw()
									done()

						elif command == "spinner":
							from turtle import *
							state = {'turn': 0}
							val = float(input("Enter speed (in number): "))
							def spinner():
								clear()
								angle = state['turn']/10
								right(angle)
								forward(100)
								dot(120, 'red')
								back(100)
								right(120)
								forward(100)
								dot(120, 'purple')
								back(100)
								right(120)
								forward(100)
								dot(120, 'blue')
								back(100)
								right(120)
								update()
							def animate():
								if state['turn']>0:
									state['turn']-=1

								spinner()
								ontimer(animate, 20)
							def flick():
								state['turn']+=val

							setup(420, 420, 370, 0)
							hideturtle()
							tracer(False)
							width(20)
							onkey(flick, 'Right')
							onkey(flick, 'Left')
							onkey(flick, 'Up')
							onkey(flick, 'Down')
							onkey(flick, 'space')
							onkey(flick, 'w')
							onkey(flick, 'a')
							onkey(flick, 's')
							onkey(flick, 'd')
							listen()
							animate()
							done()

						elif command == "version":
							print("PY-DOS version-8")
						elif command == "randomnumber":
							print("Generates a random number from 0 to 9")
							import random
							print(random.randint(0,9))
						elif command == "browser":
							# importing required libraries
							from PyQt5.QtCore import *
							from PyQt5.QtWidgets import *
							from PyQt5.QtGui import *
							from PyQt5.QtWebEngineWidgets import *
							from PyQt5.QtPrintSupport import *
							import os
							import sys

							# creating main window class
							class MainWindow(QMainWindow):

								# constructor
								def __init__(self, *args, **kwargs):
									super(MainWindow, self).__init__(*args, **kwargs)


									# creating a QWebEngineView
									self.browser = QWebEngineView()

									# setting default browser url as google
									self.browser.setUrl(QUrl("file:///C://My Websites/browser.html"))

									# adding action when url get changed
									self.browser.urlChanged.connect(self.update_urlbar)

									# adding action when loading is finished
									self.browser.loadFinished.connect(self.update_title)

									# set this browser as central widget or main window
									self.setCentralWidget(self.browser)

									# creating a status bar object
									self.status = QStatusBar()

									# adding status bar to the main window
									self.setStatusBar(self.status)

									# creating QToolBar for navigation
									navtb = QToolBar("Navigation")

									# adding this tool bar tot he main window
									self.addToolBar(navtb)

									# adding actions to the tool bar
									# creating a action for back
									back_btn = QAction("Back", self)

									# setting status tip
									back_btn.setStatusTip("Back to previous page")

									# adding action to the back button
									# making browser go back
									back_btn.triggered.connect(self.browser.back)

									# adding this action to tool bar
									navtb.addAction(back_btn)

									# similarly for forward action
									next_btn = QAction("Forward", self)
									next_btn.setStatusTip("Forward to next page")

									# adding action to the next button
									# making browser go forward
									next_btn.triggered.connect(self.browser.forward)
									navtb.addAction(next_btn)

									# similarly for reload action
									reload_btn = QAction("Reload", self)
									reload_btn.setStatusTip("Reload page")

									# adding action to the reload button
									# making browser to reload
									reload_btn.triggered.connect(self.browser.reload)
									navtb.addAction(reload_btn)

									# similarly for home action
									home_btn = QAction("Home", self)
									home_btn.setStatusTip("Go home")
									home_btn.triggered.connect(self.navigate_home)
									navtb.addAction(home_btn)

									# adding a separator in the tool bar
									navtb.addSeparator()

									# creating a line edit for the url
									self.urlbar = QLineEdit()

									# adding action when return key is pressed
									self.urlbar.returnPressed.connect(self.navigate_to_url)

									# adding this to the tool bar
									navtb.addWidget(self.urlbar)

									# adding stop action to the tool bar
									stop_btn = QAction("Stop", self)
									stop_btn.setStatusTip("Stop loading current page")

									# adding action to the stop button
									# making browser to stop
									stop_btn.triggered.connect(self.browser.stop)
									navtb.addAction(stop_btn)

									# showing all the components
									self.show()


								# method for updating the title of the window
								def update_title(self):
									title = self.browser.page().title()
									self.setWindowTitle("% s - PY Browser" % title)


								# method called by the home action
								def navigate_home(self):

									# open the google
									self.browser.setUrl(QUrl("msn.com"))

								# method called by the line edit when return key is pressed
								def navigate_to_url(self):

									# getting url and converting it to QUrl objetc
									q = QUrl(self.urlbar.text())

									# if url is scheme is blank
									if q.scheme() == "":
										# set url scheme to html
										q.setScheme("http")

									# set the url to the browser
									self.browser.setUrl(q)

								# method for updating url
								# this method is called by the QWebEngineView object
								def update_urlbar(self, q):

									# setting text to the url bar
									self.urlbar.setText(q.toString())

									# setting cursor position of the url bar
									self.urlbar.setCursorPosition(0)


							# creating a pyQt5 application
							app = QApplication(sys.argv)

							# setting name to the application
							app.setApplicationName("PY Browser")

							# creating a main window object
							window = MainWindow()

							# loop
							app.exec_()

							exit_browser = input("Press enter to exit")

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
							print(" Calculator Suite: 2.5 Unicorn ")
							print("  Calc+ 1.00")
							print("  Calc- 1.00")
							print("  Calc* 1.00")
							print("  Calc/ 2.5 Unicorn")
							print("  CalcSQRT 1.00")
							print(" RandomNumber 1.00")
							print(" Chat 3.01")
							print(" PY Browser ")
							print(" Table 1.00")
							print(" Calendar 1.00")
							print(" Date and Time Manager 1.00")
							print(" NeoCommand 8.00")
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
							print("   PY-DOS 7")
							print("   PY-DOS 8 --->Current Version")
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
							print("            8")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("PY-DOS ")
							print("-----------------")
							print("Version 8")
							print("Mutated Monkey")
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
							print("  Version: 8 Mutated Monkey")
							print("  About Update")
							print("   Update Name: 2AUG")
							print("   Update Version: 2021.8.2")
							print("   PY-DOS Base Version: 2.5 Unicorn")
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
							print("Mutated Monkey")
							print("Developed by Gautham Nair")
							print("Updated version of PY-DOS 7 Sleepy Sloth")
							print("Python ")
							print("Build number: 7000.98")
							print("Build version: Mutated Monkey")
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
						command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(DEV)").lower()
						if command == "credits":
							print("________________________")
							print("Gautham Nair")
							print("------------------------")
							print("Zanvok Corporation")
						elif command == "games":
							print("Welcome to PY Game Center")
							print("Available Games")
							print(" PY Snake")
							print(" PY Pong")
							game = ""
							while game != "quit":
								game = input("Enter 1 to play Snake, enter 2 to play Pong \n")
								if game == "1":
									import turtle
									import random
									
									w = 500
									h = 500
									food_size = 10
									delay = 100
									
									offsets = {
										"up": (0, 20),
										"down": (0, -20),
										"left": (-20, 0),
										"right": (20, 0)
									}
									
									def reset():
										global snake, snake_dir, food_position, pen
										snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
										snake_dir = "up"
										food_position = get_random_food_position()
										food.goto(food_position)
										move_snake()
										
									def move_snake():
										global snake_dir
									
										new_head = snake[-1].copy()
										new_head[0] = snake[-1][0] + offsets[snake_dir][0]
										new_head[1] = snake[-1][1] + offsets[snake_dir][1]
									
										
										if new_head in snake[:-1]:
											reset()
										else:
											snake.append(new_head)
									
										
											if not food_collision():
												snake.pop(0)
									
									
											if snake[-1][0] > w / 2:
												snake[-1][0] -= w
											elif snake[-1][0] < - w / 2:
												snake[-1][0] += w
											elif snake[-1][1] > h / 2:
												snake[-1][1] -= h
											elif snake[-1][1] < -h / 2:
												snake[-1][1] += h
									
									
											pen.clearstamps()
									
											
											for segment in snake:
												pen.goto(segment[0], segment[1])
												pen.stamp()
									
											
											screen.update()
									
											turtle.ontimer(move_snake, delay)
									
									def food_collision():
										global food_position
										if get_distance(snake[-1], food_position) < 20:
											food_position = get_random_food_position()
											food.goto(food_position)
											return True
										return False
									
									def get_random_food_position():
										x = random.randint(- w / 2 + food_size, w / 2 - food_size)
										y = random.randint(- h / 2 + food_size, h / 2 - food_size)
										return (x, y)
									
									def get_distance(pos1, pos2):
										x1, y1 = pos1
										x2, y2 = pos2
										distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
										return distance
									def go_up():
										global snake_dir
										if snake_dir != "down":
											snake_dir = "up"
									
									def go_right():
										global snake_dir
										if snake_dir != "left":
											snake_dir = "right"
									
									def go_down():
										global snake_dir
										if snake_dir!= "up":
											snake_dir = "down"
									
									def go_left():
										global snake_dir
										if snake_dir != "right":
											snake_dir = "left"
									
									
									screen = turtle.Screen()
									screen.setup(w, h)
									screen.title("Snake")
									screen.bgcolor("blue")
									screen.setup(500, 500)
									screen.tracer(0)
									
									
									pen = turtle.Turtle("square")
									pen.penup()
									
									
									food = turtle.Turtle()
									food.shape("square")
									food.color("yellow")
									food.shapesize(food_size / 20)
									food.penup()
									
									
									screen.listen()
									screen.onkey(go_up, "Up")
									screen.onkey(go_right, "Right")
									screen.onkey(go_down, "Down")
									screen.onkey(go_left, "Left")
									
									
									reset()
									turtle.done()
								elif game == "2":
									from random import choice, random
									from turtle import *

									from freegames import vector


									def value():
										"Randomly generate value between (-5, -3) or (3, 5)."
										return (3 + random() * 2) * choice([1, -1])


									ball = vector(0, 0)
									aim = vector(value(), value())
									state = {1: 0, 2: 0}


									def move(player, change):
										"Move player position by change."
										state[player] += change


									def rectangle(x, y, width, height):
										"Draw rectangle at (x, y) with given width and height."
										up()
										goto(x, y)
										down()
										begin_fill()
										for count in range(2):
											forward(width)
											left(90)
											forward(height)
											left(90)
										end_fill()


									def draw():
										"Draw game and move pong ball."
										clear()
										rectangle(-200, state[1], 10, 50)
										rectangle(190, state[2], 10, 50)

										ball.move(aim)
										x = ball.x
										y = ball.y

										up()
										goto(x, y)
										dot(10)
										update()

										if y < -200 or y > 200:
											aim.y = -aim.y

										if x < -185:
											low = state[1]
											high = state[1] + 50

											if low <= y <= high:
												aim.x = -aim.x
											else:
												return

										if x > 185:
											low = state[2]
											high = state[2] + 50

											if low <= y <= high:
												aim.x = -aim.x
											else:
												return

										ontimer(draw, 50)


									setup(420, 420, 370, 0)
									hideturtle()
									tracer(False)
									listen()
									onkey(lambda: move(1, 40), 'w')
									onkey(lambda: move(1, -40), 's')
									onkey(lambda: move(2, 40), 'Up')
									onkey(lambda: move(2, -40), 'Down')
									draw()
									done()

						elif command == "spinner":
							from turtle import *
							state = {'turn': 0}
							val = float(input("Enter speed (in number): "))
							def spinner():
								clear()
								angle = state['turn']/10
								right(angle)
								forward(100)
								dot(120, 'red')
								back(100)
								right(120)
								forward(100)
								dot(120, 'purple')
								back(100)
								right(120)
								forward(100)
								dot(120, 'blue')
								back(100)
								right(120)
								update()
							def animate():
								if state['turn']>0:
									state['turn']-=1

								spinner()
								ontimer(animate, 20)
							def flick():
								state['turn']+=val

							setup(420, 420, 370, 0)
							hideturtle()
							tracer(False)
							width(20)
							onkey(flick, 'Right')
							onkey(flick, 'Left')
							onkey(flick, 'Up')
							onkey(flick, 'Down')
							onkey(flick, 'space')
							onkey(flick, 'w')
							onkey(flick, 'a')
							onkey(flick, 's')
							onkey(flick, 'd')
							listen()
							animate()
							done()

						elif command == "version":
							print("PY-DOS version-8")
						elif command == "randomnumber":
							print("Generates a random number from 0 to 9")
							import random
							print(random.randint(0,9))
						elif command == "browser":
							# importing required libraries
							from PyQt5.QtCore import *
							from PyQt5.QtWidgets import *
							from PyQt5.QtGui import *
							from PyQt5.QtWebEngineWidgets import *
							from PyQt5.QtPrintSupport import *
							import os
							import sys

							# creating main window class
							class MainWindow(QMainWindow):

								# constructor
								def __init__(self, *args, **kwargs):
									super(MainWindow, self).__init__(*args, **kwargs)


									# creating a QWebEngineView
									self.browser = QWebEngineView()

									# setting default browser url as google
									self.browser.setUrl(QUrl("file:///C://My Websites/browser.html"))

									# adding action when url get changed
									self.browser.urlChanged.connect(self.update_urlbar)

									# adding action when loading is finished
									self.browser.loadFinished.connect(self.update_title)

									# set this browser as central widget or main window
									self.setCentralWidget(self.browser)

									# creating a status bar object
									self.status = QStatusBar()

									# adding status bar to the main window
									self.setStatusBar(self.status)

									# creating QToolBar for navigation
									navtb = QToolBar("Navigation")

									# adding this tool bar tot he main window
									self.addToolBar(navtb)

									# adding actions to the tool bar
									# creating a action for back
									back_btn = QAction("Back", self)

									# setting status tip
									back_btn.setStatusTip("Back to previous page")

									# adding action to the back button
									# making browser go back
									back_btn.triggered.connect(self.browser.back)

									# adding this action to tool bar
									navtb.addAction(back_btn)

									# similarly for forward action
									next_btn = QAction("Forward", self)
									next_btn.setStatusTip("Forward to next page")

									# adding action to the next button
									# making browser go forward
									next_btn.triggered.connect(self.browser.forward)
									navtb.addAction(next_btn)

									# similarly for reload action
									reload_btn = QAction("Reload", self)
									reload_btn.setStatusTip("Reload page")

									# adding action to the reload button
									# making browser to reload
									reload_btn.triggered.connect(self.browser.reload)
									navtb.addAction(reload_btn)

									# similarly for home action
									home_btn = QAction("Home", self)
									home_btn.setStatusTip("Go home")
									home_btn.triggered.connect(self.navigate_home)
									navtb.addAction(home_btn)

									# adding a separator in the tool bar
									navtb.addSeparator()

									# creating a line edit for the url
									self.urlbar = QLineEdit()

									# adding action when return key is pressed
									self.urlbar.returnPressed.connect(self.navigate_to_url)

									# adding this to the tool bar
									navtb.addWidget(self.urlbar)

									# adding stop action to the tool bar
									stop_btn = QAction("Stop", self)
									stop_btn.setStatusTip("Stop loading current page")

									# adding action to the stop button
									# making browser to stop
									stop_btn.triggered.connect(self.browser.stop)
									navtb.addAction(stop_btn)

									# showing all the components
									self.show()


								# method for updating the title of the window
								def update_title(self):
									title = self.browser.page().title()
									self.setWindowTitle("% s - PY Browser" % title)


								# method called by the home action
								def navigate_home(self):

									# open the google
									self.browser.setUrl(QUrl("msn.com"))

								# method called by the line edit when return key is pressed
								def navigate_to_url(self):

									# getting url and converting it to QUrl objetc
									q = QUrl(self.urlbar.text())

									# if url is scheme is blank
									if q.scheme() == "":
										# set url scheme to html
										q.setScheme("http")

									# set the url to the browser
									self.browser.setUrl(q)

								# method for updating url
								# this method is called by the QWebEngineView object
								def update_urlbar(self, q):

									# setting text to the url bar
									self.urlbar.setText(q.toString())

									# setting cursor position of the url bar
									self.urlbar.setCursorPosition(0)


							# creating a pyQt5 application
							app = QApplication(sys.argv)

							# setting name to the application
							app.setApplicationName("PY Browser")

							# creating a main window object
							window = MainWindow()

							# loop
							app.exec_()

							exit_browser = input("Press enter to exit")

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
							print(" Calculator Suite: 2.5 Unicorn ")
							print("  Calc+ 1.00")
							print("  Calc- 1.00")
							print("  Calc* 1.00")
							print("  Calc/ 2.5 Unicorn")
							print("  CalcSQRT 1.00")
							print(" RandomNumber 1.00")
							print(" Chat 3.01")
							print(" PY Browser 1.00")
							print(" Table 1.00")
							print(" Calendar 1.00")
							print(" Date and Time Manager 1.00")
							print(" NeoCommand 8.00")
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
							print("   PY-DOS 8 ---> Current version")
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
							print("            8")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("---------------------------------------------")
							print("PY-DOS ")
							print("-----------------")
							print("Version 8")
							print("Mutated Monkey")
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
							print("  Version: 8 Mutated Monkey")
							print("  About Update")
							print("   Update Name: 2AUG")
							print("   Update Version: 2021.8.2")
							print("   PY-DOS Base Version: 2.5 Unicorn")
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
							print("Version 8")
							print("Mutated Monkey")
							print("Developed by Gautham Nair")
							print("Updated version of PY-DOS 7 Sleepy Sloth")
							print("Python ")
							print("Build number: 7000.98")
							print("Build version: Mutated Monkey")
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
					command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(DEV)").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "games":
						print("Welcome to PY Game Center")
						print("Available Games")
						print(" PY Snake")
						print(" PY Pong")
						game = ""
						while game != "quit":
							game = input("Enter 1 to play Snake, enter 2 to play Pong \n")
							if game == "1":
								import turtle
								import random
								
								w = 500
								h = 500
								food_size = 10
								delay = 100
								
								offsets = {
									"up": (0, 20),
									"down": (0, -20),
									"left": (-20, 0),
									"right": (20, 0)
								}
								
								def reset():
									global snake, snake_dir, food_position, pen
									snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
									snake_dir = "up"
									food_position = get_random_food_position()
									food.goto(food_position)
									move_snake()
									
								def move_snake():
									global snake_dir
								
									new_head = snake[-1].copy()
									new_head[0] = snake[-1][0] + offsets[snake_dir][0]
									new_head[1] = snake[-1][1] + offsets[snake_dir][1]
								
									
									if new_head in snake[:-1]:
										reset()
									else:
										snake.append(new_head)
								
									
										if not food_collision():
											snake.pop(0)
								
								
										if snake[-1][0] > w / 2:
											snake[-1][0] -= w
										elif snake[-1][0] < - w / 2:
											snake[-1][0] += w
										elif snake[-1][1] > h / 2:
											snake[-1][1] -= h
										elif snake[-1][1] < -h / 2:
											snake[-1][1] += h
								
								
										pen.clearstamps()
								
										
										for segment in snake:
											pen.goto(segment[0], segment[1])
											pen.stamp()
								
										
										screen.update()
								
										turtle.ontimer(move_snake, delay)
								
								def food_collision():
									global food_position
									if get_distance(snake[-1], food_position) < 20:
										food_position = get_random_food_position()
										food.goto(food_position)
										return True
									return False
								
								def get_random_food_position():
									x = random.randint(- w / 2 + food_size, w / 2 - food_size)
									y = random.randint(- h / 2 + food_size, h / 2 - food_size)
									return (x, y)
								
								def get_distance(pos1, pos2):
									x1, y1 = pos1
									x2, y2 = pos2
									distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
									return distance
								def go_up():
									global snake_dir
									if snake_dir != "down":
										snake_dir = "up"
								
								def go_right():
									global snake_dir
									if snake_dir != "left":
										snake_dir = "right"
								
								def go_down():
									global snake_dir
									if snake_dir!= "up":
										snake_dir = "down"
								
								def go_left():
									global snake_dir
									if snake_dir != "right":
										snake_dir = "left"
								
								
								screen = turtle.Screen()
								screen.setup(w, h)
								screen.title("Snake")
								screen.bgcolor("blue")
								screen.setup(500, 500)
								screen.tracer(0)
								
								
								pen = turtle.Turtle("square")
								pen.penup()
								
								
								food = turtle.Turtle()
								food.shape("square")
								food.color("yellow")
								food.shapesize(food_size / 20)
								food.penup()
								
								
								screen.listen()
								screen.onkey(go_up, "Up")
								screen.onkey(go_right, "Right")
								screen.onkey(go_down, "Down")
								screen.onkey(go_left, "Left")
								
								
								reset()
								turtle.done()
							elif game == "2":
								from random import choice, random
								from turtle import *

								from freegames import vector


								def value():
									"Randomly generate value between (-5, -3) or (3, 5)."
									return (3 + random() * 2) * choice([1, -1])


								ball = vector(0, 0)
								aim = vector(value(), value())
								state = {1: 0, 2: 0}


								def move(player, change):
									"Move player position by change."
									state[player] += change


								def rectangle(x, y, width, height):
									"Draw rectangle at (x, y) with given width and height."
									up()
									goto(x, y)
									down()
									begin_fill()
									for count in range(2):
										forward(width)
										left(90)
										forward(height)
										left(90)
									end_fill()


								def draw():
									"Draw game and move pong ball."
									clear()
									rectangle(-200, state[1], 10, 50)
									rectangle(190, state[2], 10, 50)

									ball.move(aim)
									x = ball.x
									y = ball.y

									up()
									goto(x, y)
									dot(10)
									update()

									if y < -200 or y > 200:
										aim.y = -aim.y

									if x < -185:
										low = state[1]
										high = state[1] + 50

										if low <= y <= high:
											aim.x = -aim.x
										else:
											return

									if x > 185:
										low = state[2]
										high = state[2] + 50

										if low <= y <= high:
											aim.x = -aim.x
										else:
											return

									ontimer(draw, 50)


								setup(420, 420, 370, 0)
								hideturtle()
								tracer(False)
								listen()
								onkey(lambda: move(1, 40), 'w')
								onkey(lambda: move(1, -40), 's')
								onkey(lambda: move(2, 40), 'Up')
								onkey(lambda: move(2, -40), 'Down')
								draw()
								done()

					elif command == "spinner":
						from turtle import *
						state = {'turn': 0}
						val = float(input("Enter speed (in number): "))
						def spinner():
							clear()
							angle = state['turn']/10
							right(angle)
							forward(100)
							dot(120, 'red')
							back(100)
							right(120)
							forward(100)
							dot(120, 'purple')
							back(100)
							right(120)
							forward(100)
							dot(120, 'blue')
							back(100)
							right(120)
							update()
						def animate():
							if state['turn']>0:
								state['turn']-=1

							spinner()
							ontimer(animate, 20)
						def flick():
							state['turn']+=val

						setup(420, 420, 370, 0)
						hideturtle()
						tracer(False)
						width(20)
						onkey(flick, 'Right')
						onkey(flick, 'Left')
						onkey(flick, 'Up')
						onkey(flick, 'Down')
						onkey(flick, 'space')
						onkey(flick, 'w')
						onkey(flick, 'a')
						onkey(flick, 's')
						onkey(flick, 'd')
						listen()
						animate()
						done()

					elif command == "version":
						print("PY-DOS version-8")
					elif command == "randomnumber":
						print("Generates a random number from 0 to 9")
						import random
						print(random.randint(0,9))
					elif command == "browser":
						# importing required libraries
						from PyQt5.QtCore import *
						from PyQt5.QtWidgets import *
						from PyQt5.QtGui import *
						from PyQt5.QtWebEngineWidgets import *
						from PyQt5.QtPrintSupport import *
						import os
						import sys

						# creating main window class
						class MainWindow(QMainWindow):

							# constructor
							def __init__(self, *args, **kwargs):
								super(MainWindow, self).__init__(*args, **kwargs)


								# creating a QWebEngineView
								self.browser = QWebEngineView()

								# setting default browser url as google
								self.browser.setUrl(QUrl("file:///C://My Websites/browser.html"))

								# adding action when url get changed
								self.browser.urlChanged.connect(self.update_urlbar)

								# adding action when loading is finished
								self.browser.loadFinished.connect(self.update_title)

								# set this browser as central widget or main window
								self.setCentralWidget(self.browser)

								# creating a status bar object
								self.status = QStatusBar()

								# adding status bar to the main window
								self.setStatusBar(self.status)

								# creating QToolBar for navigation
								navtb = QToolBar("Navigation")

								# adding this tool bar tot he main window
								self.addToolBar(navtb)

								# adding actions to the tool bar
								# creating a action for back
								back_btn = QAction("Back", self)

								# setting status tip
								back_btn.setStatusTip("Back to previous page")

								# adding action to the back button
								# making browser go back
								back_btn.triggered.connect(self.browser.back)

								# adding this action to tool bar
								navtb.addAction(back_btn)

								# similarly for forward action
								next_btn = QAction("Forward", self)
								next_btn.setStatusTip("Forward to next page")

								# adding action to the next button
								# making browser go forward
								next_btn.triggered.connect(self.browser.forward)
								navtb.addAction(next_btn)

								# similarly for reload action
								reload_btn = QAction("Reload", self)
								reload_btn.setStatusTip("Reload page")

								# adding action to the reload button
								# making browser to reload
								reload_btn.triggered.connect(self.browser.reload)
								navtb.addAction(reload_btn)

								# similarly for home action
								home_btn = QAction("Home", self)
								home_btn.setStatusTip("Go home")
								home_btn.triggered.connect(self.navigate_home)
								navtb.addAction(home_btn)

								# adding a separator in the tool bar
								navtb.addSeparator()

								# creating a line edit for the url
								self.urlbar = QLineEdit()

								# adding action when return key is pressed
								self.urlbar.returnPressed.connect(self.navigate_to_url)

								# adding this to the tool bar
								navtb.addWidget(self.urlbar)

								# adding stop action to the tool bar
								stop_btn = QAction("Stop", self)
								stop_btn.setStatusTip("Stop loading current page")

								# adding action to the stop button
								# making browser to stop
								stop_btn.triggered.connect(self.browser.stop)
								navtb.addAction(stop_btn)

								# showing all the components
								self.show()


							# method for updating the title of the window
							def update_title(self):
								title = self.browser.page().title()
								self.setWindowTitle("% s - PY Browser" % title)


							# method called by the home action
							def navigate_home(self):

								# open the google
								self.browser.setUrl(QUrl("msn.com"))

							# method called by the line edit when return key is pressed
							def navigate_to_url(self):

								# getting url and converting it to QUrl objetc
								q = QUrl(self.urlbar.text())

								# if url is scheme is blank
								if q.scheme() == "":
									# set url scheme to html
									q.setScheme("http")

								# set the url to the browser
								self.browser.setUrl(q)

							# method for updating url
							# this method is called by the QWebEngineView object
							def update_urlbar(self, q):

								# setting text to the url bar
								self.urlbar.setText(q.toString())

								# setting cursor position of the url bar
								self.urlbar.setCursorPosition(0)


						# creating a pyQt5 application
						app = QApplication(sys.argv)

						# setting name to the application
						app.setApplicationName("PY Browser")

						# creating a main window object
						window = MainWindow()

						# loop
						app.exec_()

						exit_browser = input("Press enter to exit")

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
						print(" Calculator Suite: 2.5 Unicorn ")
						print("  Calc+ 1.00")
						print("  Calc- 1.00")
						print("  Calc* 1.00")
						print("  Calc/ 2.5 Unicorn")
						print("  CalcSQRT 1.00")
						print(" RandomNumber 1.00")
						print(" Chat 3.01")
						print(" PY Browser ")
						print(" Table 1.00")
						print(" Calendar 1.00")
						print(" Date and Time Manager 1.00")
						print(" NeoCommand 8.00")
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
						print("   PY-DOS 8 ---> Current Version")
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
						print("            8")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 8")
						print("Mutated Monkey")
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
						print("  Version: 7 Mutated Monkey")
						print("  About Update")
						print("   Update Name: 2AUG")
						print("   Update Version: 2021.8.2")
						print("   PY-DOS Base Version: 2.5 Unicorn")
						print("   Developer Preview and Development")
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
						print("Mutated Monkey")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 7 Sleepy Sloth")
						print("Python ")
						print("Build number: 7000.98")
						print("Build version: Mutated Monkey")
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
					command = input(user_name + "@" + pc_name + " :" + "~" + " >" + "(DEV)").lower()
					if command == "credits":
						print("________________________")
						print("Gautham Nair")
						print("------------------------")
						print("Zanvok Corporation")
					elif command == "games":
						print("Welcome to PY Game Center")
						print("Available Games")
						print(" PY Snake")
						print(" PY Pong")
						game = ""
						while game != "quit":
							game = input("Enter 1 to play Snake, enter 2 to play Pong \n")
							if game == "1":
								import turtle
								import random
								
								w = 500
								h = 500
								food_size = 10
								delay = 100
								
								offsets = {
									"up": (0, 20),
									"down": (0, -20),
									"left": (-20, 0),
									"right": (20, 0)
								}
								
								def reset():
									global snake, snake_dir, food_position, pen
									snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
									snake_dir = "up"
									food_position = get_random_food_position()
									food.goto(food_position)
									move_snake()
									
								def move_snake():
									global snake_dir
								
									new_head = snake[-1].copy()
									new_head[0] = snake[-1][0] + offsets[snake_dir][0]
									new_head[1] = snake[-1][1] + offsets[snake_dir][1]
								
									
									if new_head in snake[:-1]:
										reset()
									else:
										snake.append(new_head)
								
									
										if not food_collision():
											snake.pop(0)
								
								
										if snake[-1][0] > w / 2:
											snake[-1][0] -= w
										elif snake[-1][0] < - w / 2:
											snake[-1][0] += w
										elif snake[-1][1] > h / 2:
											snake[-1][1] -= h
										elif snake[-1][1] < -h / 2:
											snake[-1][1] += h
								
								
										pen.clearstamps()
								
										
										for segment in snake:
											pen.goto(segment[0], segment[1])
											pen.stamp()
								
										
										screen.update()
								
										turtle.ontimer(move_snake, delay)
								
								def food_collision():
									global food_position
									if get_distance(snake[-1], food_position) < 20:
										food_position = get_random_food_position()
										food.goto(food_position)
										return True
									return False
								
								def get_random_food_position():
									x = random.randint(- w / 2 + food_size, w / 2 - food_size)
									y = random.randint(- h / 2 + food_size, h / 2 - food_size)
									return (x, y)
								
								def get_distance(pos1, pos2):
									x1, y1 = pos1
									x2, y2 = pos2
									distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
									return distance
								def go_up():
									global snake_dir
									if snake_dir != "down":
										snake_dir = "up"
								
								def go_right():
									global snake_dir
									if snake_dir != "left":
										snake_dir = "right"
								
								def go_down():
									global snake_dir
									if snake_dir!= "up":
										snake_dir = "down"
								
								def go_left():
									global snake_dir
									if snake_dir != "right":
										snake_dir = "left"
								
								
								screen = turtle.Screen()
								screen.setup(w, h)
								screen.title("Snake")
								screen.bgcolor("blue")
								screen.setup(500, 500)
								screen.tracer(0)
								
								
								pen = turtle.Turtle("square")
								pen.penup()
								
								
								food = turtle.Turtle()
								food.shape("square")
								food.color("yellow")
								food.shapesize(food_size / 20)
								food.penup()
								
								
								screen.listen()
								screen.onkey(go_up, "Up")
								screen.onkey(go_right, "Right")
								screen.onkey(go_down, "Down")
								screen.onkey(go_left, "Left")
								
								
								reset()
								turtle.done()
							elif game == "2":
								from random import choice, random
								from turtle import *

								from freegames import vector


								def value():
									"Randomly generate value between (-5, -3) or (3, 5)."
									return (3 + random() * 2) * choice([1, -1])


								ball = vector(0, 0)
								aim = vector(value(), value())
								state = {1: 0, 2: 0}


								def move(player, change):
									"Move player position by change."
									state[player] += change


								def rectangle(x, y, width, height):
									"Draw rectangle at (x, y) with given width and height."
									up()
									goto(x, y)
									down()
									begin_fill()
									for count in range(2):
										forward(width)
										left(90)
										forward(height)
										left(90)
									end_fill()


								def draw():
									"Draw game and move pong ball."
									clear()
									rectangle(-200, state[1], 10, 50)
									rectangle(190, state[2], 10, 50)

									ball.move(aim)
									x = ball.x
									y = ball.y

									up()
									goto(x, y)
									dot(10)
									update()

									if y < -200 or y > 200:
										aim.y = -aim.y

									if x < -185:
										low = state[1]
										high = state[1] + 50

										if low <= y <= high:
											aim.x = -aim.x
										else:
											return

									if x > 185:
										low = state[2]
										high = state[2] + 50

										if low <= y <= high:
											aim.x = -aim.x
										else:
											return

									ontimer(draw, 50)


								setup(420, 420, 370, 0)
								hideturtle()
								tracer(False)
								listen()
								onkey(lambda: move(1, 40), 'w')
								onkey(lambda: move(1, -40), 's')
								onkey(lambda: move(2, 40), 'Up')
								onkey(lambda: move(2, -40), 'Down')
								draw()
								done()

					elif command == "spinner":
						from turtle import *
						state = {'turn': 0}
						val = float(input("Enter speed (in number): "))
						def spinner():
							clear()
							angle = state['turn']/10
							right(angle)
							forward(100)
							dot(120, 'red')
							back(100)
							right(120)
							forward(100)
							dot(120, 'purple')
							back(100)
							right(120)
							forward(100)
							dot(120, 'blue')
							back(100)
							right(120)
							update()
						def animate():
							if state['turn']>0:
								state['turn']-=1

							spinner()
							ontimer(animate, 20)
						def flick():
							state['turn']+=val

						setup(420, 420, 370, 0)
						hideturtle()
						tracer(False)
						width(20)
						onkey(flick, 'Right')
						onkey(flick, 'Left')
						onkey(flick, 'Up')
						onkey(flick, 'Down')
						onkey(flick, 'space')
						onkey(flick, 'w')
						onkey(flick, 'a')
						onkey(flick, 's')
						onkey(flick, 'd')
						listen()
						animate()
						done()

					elif command == "version":
						print("PY-DOS version-8")
					elif command == "randomnumber":
						print("generates a random number from 0 to 9")
						import random
						print(random.randint(0,9))
					elif command == "browser":
						# importing required libraries
						from PyQt5.QtCore import *
						from PyQt5.QtWidgets import *
						from PyQt5.QtGui import *
						from PyQt5.QtWebEngineWidgets import *
						from PyQt5.QtPrintSupport import *
						import os
						import sys

						# creating main window class
						class MainWindow(QMainWindow):

							# constructor
							def __init__(self, *args, **kwargs):
								super(MainWindow, self).__init__(*args, **kwargs)


								# creating a QWebEngineView
								self.browser = QWebEngineView()

								# setting default browser url as google
								self.browser.setUrl(QUrl("file:///C://My Websites/browser.html"))

								# adding action when url get changed
								self.browser.urlChanged.connect(self.update_urlbar)

								# adding action when loading is finished
								self.browser.loadFinished.connect(self.update_title)

								# set this browser as central widget or main window
								self.setCentralWidget(self.browser)

								# creating a status bar object
								self.status = QStatusBar()

								# adding status bar to the main window
								self.setStatusBar(self.status)

								# creating QToolBar for navigation
								navtb = QToolBar("Navigation")

								# adding this tool bar tot he main window
								self.addToolBar(navtb)

								# adding actions to the tool bar
								# creating a action for back
								back_btn = QAction("Back", self)

								# setting status tip
								back_btn.setStatusTip("Back to previous page")

								# adding action to the back button
								# making browser go back
								back_btn.triggered.connect(self.browser.back)

								# adding this action to tool bar
								navtb.addAction(back_btn)

								# similarly for forward action
								next_btn = QAction("Forward", self)
								next_btn.setStatusTip("Forward to next page")

								# adding action to the next button
								# making browser go forward
								next_btn.triggered.connect(self.browser.forward)
								navtb.addAction(next_btn)

								# similarly for reload action
								reload_btn = QAction("Reload", self)
								reload_btn.setStatusTip("Reload page")

								# adding action to the reload button
								# making browser to reload
								reload_btn.triggered.connect(self.browser.reload)
								navtb.addAction(reload_btn)

								# similarly for home action
								home_btn = QAction("Home", self)
								home_btn.setStatusTip("Go home")
								home_btn.triggered.connect(self.navigate_home)
								navtb.addAction(home_btn)

								# adding a separator in the tool bar
								navtb.addSeparator()

								# creating a line edit for the url
								self.urlbar = QLineEdit()

								# adding action when return key is pressed
								self.urlbar.returnPressed.connect(self.navigate_to_url)

								# adding this to the tool bar
								navtb.addWidget(self.urlbar)

								# adding stop action to the tool bar
								stop_btn = QAction("Stop", self)
								stop_btn.setStatusTip("Stop loading current page")

								# adding action to the stop button
								# making browser to stop
								stop_btn.triggered.connect(self.browser.stop)
								navtb.addAction(stop_btn)

								# showing all the components
								self.show()


							# method for updating the title of the window
							def update_title(self):
								title = self.browser.page().title()
								self.setWindowTitle("% s - PY Browser" % title)


							# method called by the home action
							def navigate_home(self):

								# open the google
								self.browser.setUrl(QUrl("msn.com"))

							# method called by the line edit when return key is pressed
							def navigate_to_url(self):

								# getting url and converting it to QUrl objetc
								q = QUrl(self.urlbar.text())

								# if url is scheme is blank
								if q.scheme() == "":
									# set url scheme to html
									q.setScheme("http")

								# set the url to the browser
								self.browser.setUrl(q)

							# method for updating url
							# this method is called by the QWebEngineView object
							def update_urlbar(self, q):

								# setting text to the url bar
								self.urlbar.setText(q.toString())

								# setting cursor position of the url bar
								self.urlbar.setCursorPosition(0)


						# creating a pyQt5 application
						app = QApplication(sys.argv)

						# setting name to the application
						app.setApplicationName("PY Browser")

						# creating a main window object
						window = MainWindow()

						# loop
						app.exec_()

						exit_browser = input("Press enter to exit")

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
						print(" Calculator Suite: 2.5 Unicorn ")
						print("  Calc+ 1.00")
						print("  Calc- 1.00")
						print("  Calc* 1.00")
						print("  Calc/ 2.5 Unicorn")
						print("  CalcSQRT 1.00")
						print(" RandomNumber 1.00")
						print(" Chat 3.01")
						print(" PY Browser ")
						print(" Table 1.00")
						print(" Calendar 1.00")
						print(" Date and Time Manager 1.00")
						print(" NeoCommand 8.00")
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
						print("   PY-DOS 7")
						print("   PY-DOS 8 ---> Current Version")
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
						print("            8")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("---------------------------------------------")
						print("PY-DOS ")
						print("-----------------")
						print("Version 8")
						print("Mutated Monkey")
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
						print("   PY-DOS Base Version: 2.5 Unicorn")
					elif command == "store":
						print("This command gives you the information about the source from where you have you have got this copy of PY-DOS 8")
						print("PY Store : 7.089")
						print("PY Store for Developers and Developer Preview")
						print("PY-DOS 8 obtained from GitHub")
						print("Repository information : ZanvokCorporation/ZChannel1")
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
						print("Version 8")
						print("Mutated Monkey")
						print("Developed by Gautham Nair")
						print("Updated version of PY-DOS 7 Sleepy Sloth")
						print("Python ")
						print("Build number: 7000.98")
						print("Build version: Mutated Monkey")
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
