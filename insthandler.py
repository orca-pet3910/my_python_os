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