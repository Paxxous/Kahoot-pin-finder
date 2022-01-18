
import requests, random, threading, pyautogui
# just to save it https://kahoot.it/reserve/session/351890/




def search():
  while True:

    pin = ""
    for _ in range(6):
      pin += str(random.randint(1, 9))


    link = requests.get("https://kahoot.it/reserve/session/" + pin)
    if str(link) == "<Response [200]>":
      print("yeah bois")
      open("foundpins.txt", "a").write(pin + "\n")
      pyautogui.typewrite(pin)
      pyautogui.press("enter")
      print(f"Quick my guy, join {pin}")


    else:
      print("Attempt failed.\n")


howManyThreads = int(input("How many threads would you like to use? "))

for i in range(howManyThreads):
  threading.Thread(target=search, args=()).start()

