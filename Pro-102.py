import pyautogui
import time


sleep1 = input("Enter time between each screenshot(in min) :- ")
sleep2 = int(sleep1)
sleep = sleep2 * 60

noOfScreenShot1 = input("No of Screenshot :- ")
noOfScreenShot = int(noOfScreenShot1) + 1

location = input("Location of file storage :- ")

currentScreenShot = 1
while (currentScreenShot <= noOfScreenShot) :
    locationF = location + "/" + "image" + str(currentScreenShot) + ".png"
    pyautogui.screenshot(locationF)
    currentScreenShot += 1
    time.sleep(sleep)