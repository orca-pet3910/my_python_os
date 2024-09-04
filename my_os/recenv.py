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

print("Loading the system...")

with open("./data", "r+") as data:
  username = data.read()
  print(f"Welcome back, {username}!")

def desktop() -> None:
  print(\"\"\"
  1. run a Python file
  2. shutdown this operating system
  3. execute a raw instruction (hex format ONLY)
  \"\"\")
  try:
    choice1 = int(input("[1/2/3]? "))
    if choice1 == 1:
      choice2 = input("What is the path to the Python file? ")
      system(f"python {choice2}")
    elif choice1 == 2:
      print("A system shutdown signal has been sent!")
      insthandler.run_instruction(1, [0])
    elif choice1 == 3:
      try:
        choice2 = int(input("instruction [0x00/0x01]? "))
        choice3 = list(input("arguments (in the list format)? "))
        insthandler.run_instruction()
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
  print("recovered main.py\nrecovering insthandler.py")
  """)
  with open("insthandler.py", "w") as insthandler:
    insthandler.write("""
import systemcalls

def illegal_instruction(critical: bool, _instruction: int) -> None:
    instruction = hex(_instruction)
    print(f"illegal instruction {instruction}")
    if critical:
      systemcalls.halt()

def run_instructon(_instruction: int, arguments: list) -> None:
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


def shutdown():
  print("Shutting down!")
  delay(randomfloat()*1.5)
  print("Please wait for the User Profile Service")
  delay(randomfloat()/3)
  print("Please wait for the Local Instruction Manager")
  delay(randomfloat()/12)
  print("Stopping services")
  delay(randomfloat()*1.25)
  print("Shutting down")
  delay(1)
  quit(0)

def halt():
  print("System halted.", end="")
  while True:
    delay(30)


def send_systemcall(_call_id: int):
  call_id = hex(_call_id)
  if call_id == 0x00:
    shutdown()
  elif call_id == 0x01:
    halt()
  else:
    illegal_instruction(True, 0x00000001)
    """)
    print("recovered systemcalls.py")
    