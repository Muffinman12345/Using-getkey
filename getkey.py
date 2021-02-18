#Import the getkey module
from getkey import getkey
import os
#Make the keydown variable

while True:
  key_down = getkey.getkey()
  #We use a while loop so it runs forever
  print(f"You pressed the {key_down} key.")
  #Clear the console
  os.system('clear')
