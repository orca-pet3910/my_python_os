import systemcalls
import insthandler
from os import system
from time import sleep as delay
from random import random as randomfloat

print("Loading the system...")
delay(randomfloat())
print("Please wait for the User Profile Service")
delay(randomfloat()/3)
print("Please wait for the Local Instruction Manager")
delay(randomfloat()/9)
print("Logging in...")

with open("./data", "r+") as data:
  username = data.read()
  print(f"Welcome back, {username}!")
  delay(2)

def desktop() -> None:
  print("""
  1. run a Python file
  2. shutdown this operating system
  3. execute a raw instruction
  """)
  try:
    choice1 = int(input("[1/2/3]? "))
    if choice1 == 1:
      choice2 = input("What is the path to the Python file? ")
      system(f"python {choice2}")
    elif choice1 == 2:
      print("A system shutdown signal has been sent!")
      systemcalls.shutdown()
    elif choice1 == 3:
      try:
        choice2 = int(input("instruction [0/1]? "))
        choice3 = list(input("arguments (in the list format)? "))
        insthandler.run_instruction(choice2, choice3)
      except:
        insthandler.illegal_instruction(False, 0xFFFFFFFF)
  except ValueError:
    print("invalid value")

while True:
  # try:
  desktop()
  # except ValueError:
  #   print("invalid value")
  #   desktop()