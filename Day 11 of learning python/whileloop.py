'''-----------------------------------------The while Loop in Action--------------------------------------------------------'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

'''--------------------------------------Letting the User Choose When to Quit---------------------------------------------'''

# define a quit value and then keep the program running as long as the user has not entered the quit value:
# define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit').
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = "" # set up a variable message to keep track of whatever value the user enters. We define message as an empty string, "", so Python has something to check the first time it reaches the while line
while message != 'quit':
   message = input(prompt)
   print(message)

'''This code represents a simple interactive program that repeatedly prompts the user for input and then repeats that input back to the user until the user enters the word 'quit' to end the program. Let's break down the code step by step:
prompt = "\nTell me something, and I will repeat it back to you:": This line initializes a string variable called prompt with the message that will be displayed to the user when they are prompted for input. The \n at the beginning of the string adds a newline to create a separation between the user's input and the program's message.
prompt += "\nEnter 'quit' to end the program. ": This line appends a second part to the prompt variable. It informs the user that they can enter 'quit' to end the program.
message = "": This line initializes an empty string variable called message. This variable will be used to store the user's input.
while message != 'quit':: This line starts a while loop. The loop will continue running as long as the value stored in the message variable is not equal to 'quit'. In other words, the loop will run until the user enters 'quit'.
message = input(prompt): Inside the loop, this line uses the input function to display the prompt message to the user and wait for their input. The user's input is then stored in the message variable.
print(message): After receiving the user's input, the program prints the value of the message variable, which is the user's input.
The loop continues back to the while statement, where it checks if the value of message is still not equal to 'quit'. If it's not 'quit', the loop continues, and the program prompts the user for input again. If the user enters 'quit', the condition becomes False, and the loop exits.
This program effectively creates an interactive conversation with the user. It continuously asks the user for input and echoes their input back to them until they decide to end the program by typing 'quit'.'''

# This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
   message = input(prompt)
   if message != 'quit':
      print(message)


'''----------------------------------Using a Flag---------------------------------------'''

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
   message = input(prompt)
   if message == 'quit':
      active = False
   else:
      print(message)

'''------------------------------------------------Using break to Exit a Loop-------------------------------------------------------'''

# consider a program that asks the user about places they’ve visited. We can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
   city = input(prompt)
   if city == 'quit':
      break
   else:
      print(f"I'd love to go to {city.title()}!")

'''---------------------------------------------------Using continue in a Loop-------------------------------------------------------'''

# consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:
current_number = 0 # set current_number to 0.

# Because it’s less than 10, Python enters the while loop
while current_number < 10:
   current_number += 1 # increment the count by 1
   if current_number % 2 == 0: # if statement then checks the modulo of current_number and 2
     continue # If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the rest of the loop and return to the beginning
   print(current_number) # If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number


'''-----------------------------------------------Avoiding Infinite Loops---------------------------------------------------------------'''

x = 1
while x <= 5:
  print(x)
  x += 1

# if you accidentally omit the line x += 1, the loop will run forever:
# This loop runs forever!
'''
x = 1
while x <= 5:
   print(x)
   
'''