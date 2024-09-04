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
  
