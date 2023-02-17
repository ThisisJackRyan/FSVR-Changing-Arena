import json
import time
import subprocess
from tkinter import *


config_path = r"C:\Program Files\Vertigo Arcades\Haze\Haze\config.txt"



root = Tk()
root.geometry("400x300")

def openTkinter():
    infoText = Label(root, text="Please press the Button to switch all players to other arena")
    infoText.pack()
    button = Button(root, text = "Swap arenas", width =12,command = ChangeLoc)
    button.pack()



def ChangeLoc():
    root.destroy()
    # Terminate the running application by name
    subprocess.run(['taskkill', '/IM', 'Haze.exe', '/F'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
    
    time.sleep(2)

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            txt = json.loads(file.read())

        
        loc = -1
        other = -1
        if len(txt['PlaySpaces'][1]["machineGuids"]) > 0:
            loc = 1
            other = 0
        elif len(txt['PlaySpaces'][0]["machineGuids"]) > 0:
            loc = 0
            other = 1
        array = txt['PlaySpaces'][loc]["machineGuids"]
        array2 = txt['PlaySpaces'][loc]["sessions"][0]["participants"]

        #print()

        txt["PlaySpaces"][other]["machineGuids"] = array
        txt["PlaySpaces"][loc]["machineGuids"] = []

        txt["PlaySpaces"][other]["sessions"][0]["participants"] = array2
        txt["PlaySpaces"][loc]["sessions"][0]["participants"] = []

        with open(config_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(txt, indent=4))
        #print("Successfully switched PlaySpaces...")
       
        time.sleep(2)
    except:
        #print("hmmm Something went wrong...")
        time.sleep(2)
    
    
    # Wait for a few seconds
    try:
        #print("Opening Haze...")
        time.sleep(5)
        subprocess.Popen(['C:\\Program Files\\Vertigo Arcades\\Haze\\Haze\\Haze.exe'])
    except:
        pass
        #print("Haze is already open")

            
 


openTkinter()
root.mainloop() 



#to make this a .exe file 
    #CHECK PATHING SO WE DONT BRAEK IT AND TEST WITH PRINTS BEFORE TURNIGN INTO .EXE FILE!!!!!!!
#first:
#   pip install pyinstaller
#Second:
#   then cd into the folder
#Third:
#   pyinstaller --onefile main.pyw
#Last:
#   follow instructions on how to make it run as admin: https://www.itpro.com/software/367829/how-to-make-programs-always-run-as-admin-on-windows
    


