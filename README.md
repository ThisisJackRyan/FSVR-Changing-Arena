# FSVR-Changing-Arena
I made some python code for my work to make changing arenas more efficient. 


## How it works
  At FSVR we use a software called Haze, which host our games and beams it out to the other headsets. The goal of this program was to move the Players and their repsective machineGuids to the other arena. 
  
  Fist I close Haze using the "subprocess" library. Then using the config.txt file, I load the json data and find the machines and the participants and copy their respective arrays and move it to the other play space. Once this is done I reopen Haze and it is now ready for the Game Host to continue the rest of the setup for their group.
  
  The part I enjoy about this simple but functional code is that it is my first "Real Life" example of how you can optimaze your life with code. While this only saves the host 30 seconds, this is able to run over and over for years to come.
