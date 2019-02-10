# Alexa-LG-TV-Controller

Makes use of Klattimer's LGWebOSRemote module and Sinric's faux WEEMOS creator to control any smart LG TV with Alexa. This python script monitors Alexa's commands through Sinric, and then executes it using LG's nodejs API. It will allow you to turn on/off an LG tv and much more ... all from your Alexa device.

## Supported models

### Tested with

  * UF830V
  * UH650V
  * UJ635V
  * HU80KG.AEU (CineBeam 4K)
  * [please add more!]

  Tested with python 2.7 on linux. 
  
  ### Likely supports

  All devices with firmware major version 4, product name "webOSTV 2.0/3.0"
  
  ## Available Alexa Commands
   
    ChannelDown      
    ChannelUp        
    FastForward  
    Pause       
    Play        
    Rewind                             
    mute                  
    off                   
    on                    
    Set Input          input(HDMI 1,HDMI 2 ...)
    Set Channel        channel_number
    Set Volume         level                
    Volume Down            
    Volume Up
    
  ## Setup

  Requires wakeonlan, websocket and websocket-client for python and arp (in Debian/Ubuntu: apt-get install net-tools)

  There's a requirements.txt included

     1.)  Setup your sinric account at https://sinric.com/
     2.)  Login to your account and click add smart home device, give the device a name and choose TV as device type
     ----> it is good at this point to copy the api of the device 
     3.)  On the Alexa app go to 'skills & games' and install sinric's skill and login to your account
     4.)  The fake device you just created on the website should then be seen in the Alexa app under 'devices'
  
    # Now enter the directory with the files and type in command line 
    ------------------------------------->
    1.)  pip install -r requirements.txt
    2.)  sudo python setup.py
    ------------------------------------->
    ---> This will scan for your LG tv and will show the IP address of all LG tv's on the local network
    # Example :
    {
    "count": 1, 
    "list": [
        {
            "address": "192.168.0.158", 
            "model": "OLEDXXXXX", 
            "uuid": "0b6405648-ccc7-ab45f-967d-8gd47f21346"
        }
    ], 
    "result": "ok"
    }
    ---> You will then be prompted to enter the ip address of the TV you want to authorise on
    please enter  ip like "192.168.0.158" (make sure to use brackets)
    3.)  Enter IP address of TV, and a notification will pop up on the TV screen (click authorise on TV)

    4.)  Now open the Alexa.py file and edit line 80. Here you need to replace :
    # Example :
    line 80 | api = ' enter-api-here  ' 
    becomes 
    line 80 | api = '65a23cd9-2e5d-495c-b4bd-5abfgh3l60345'

    5.)  The final step is to start the Alexa.py file : 
              python Alexa.py
         or to run in the background once terminal closes. Use: 
              nohup python Alexa.py
  ## FeLiNa
 
  Once all the steps above have been completed, and the python script is running, try telling your Alexa device to change your tv volume
  by saying 
  
  ALEXA SET (Sinric Device Name) VOLUME TO (intended level)
  
  ## Caveats

  You need to run setup.py whilst the TV is on as it will need to pull the mac address of the device.
 
  ## CREDITS
  
  I want to give a big thanks to klattimer whose library I used in this project -> https://github.com/klattimer/LGWebOSRemote/ 
  
