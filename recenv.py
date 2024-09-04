########################################################
# WARNING! do NOT modify this file unless you need to. #
########################################################
recover = input("Do you want to run recovery on system files? [y/n]")
if recover == "y":
  print("recovering main.py")
  with open("main.py", "w") as main:
    main.write("""
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
  print(\"\"\"
  1. run a Python file
  2. shutdown this operating system
  3. execute a raw instruction
  \"\"\")
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
  """)
  with open("insthandler.py", "w") as insthandler:
    insthandler.write("""
import systemcalls


def illegal_instruction(critical: bool, _instruction: int) -> None:
    instruction = hex(_instruction)
    if instruction != 0xffffffff:
      print(f"illegal instruction {instruction}")
      if critical:
        systemcalls.halt()
    else:
      print(f"illegal instruction 0x0UNKNOWN")
      if critical:
        systemcalls.halt()
    
def run_instruction(_instruction: int, arguments: list) -> None:
    instruction = hex(_instruction)
    if instruction == 0x00000000:
      try:
        print(arguments[0])
      except:
        illegal_instruction(False, 0x00000000)
    elif instruction == 0x00000001:
      systemcalls.send_systemcall(arguments[0])
    else:
      illegal_instruction(False, _instruction)
    # rest coming soon
    """)
    print("recovered insthandler.py\nrecovering systemcalls.py")
  with open("systemcalls.py", "w") as systemcalls:
    systemcalls.write("""
from insthandler import illegal_instruction
from time import sleep as delay
from random import random as randomfloat


def halt() -> None:
  while True:
    delay(30)

def shutdown() -> None:
  print("Shutting down!")
  delay(randomfloat()*1.5)
  print("Please wait for the User Profile Service")
  delay(randomfloat()/3)
  print("Please wait for the Local Instruction Manager")
  delay(randomfloat()/12)
  print("Stopping services")
  delay(randomfloat()*1.25)
  print("Shutting down")
  delay(randomfloat()*3.5)
  try:
    print("It is now safe to close this program. (Press Ctrl + C to exit)")
    halt()
  except KeyboardInterrupt:
    print("^C")
    quit(0)
  

def send_systemcall(_call_id: int) -> None:
  call_id = hex(_call_id)
  if call_id == 0x00:
    shutdown()
  elif call_id == 0x01:
    halt()
  else:
    illegal_instruction(True, 0x00000001)
    """)
    print("recovered systemcalls.py")
    