import json
import time
import subprocess


config_path = r"C:\Program Files\Vertigo Arcades\Haze\Haze\config.txt"




def ChangeLoc():
    # Terminate the running application by name
    subprocess.run(['taskkill', '/IM', 'Haze.exe', '/F'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
    
   
    
    try:
        #find config file and load Json
        with open(config_path, "r", encoding="utf-8") as file:
            txt = json.loads(file.read())

        #logic to find which is the Current Play-Spaces Machines in it
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

       
        #Swapping MachineGuids array
        txt["PlaySpaces"][other]["machineGuids"] = array
        txt["PlaySpaces"][loc]["machineGuids"] = []

        #Swapping Participants array
        txt["PlaySpaces"][other]["sessions"][0]["participants"] = array2
        txt["PlaySpaces"][loc]["sessions"][0]["participants"] = []

        #write Json file
        with open(config_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(txt, indent=4))
    except:
        pass
       
    
    
    # Wait for a few seconds and open file
    try:
        time.sleep(2)
        subprocess.Popen(['C:\\Program Files\\Vertigo Arcades\\Haze\\Haze\\Haze.exe'])
    except:
        pass


ChangeLoc()





    


