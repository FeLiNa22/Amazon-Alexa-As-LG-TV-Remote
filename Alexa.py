import websocket
import thread
import time
import base64
import lgtv
import json

def on_message(ws, msg):

    print ('messy : '+ msg)
    
    json_data=json.loads(msg)
    action =  json_data['action']

    if(action == "setPowerState") :
        power = json_data["value"]
	if (power == "OFF"):
	    lgtv.LGparser(['off'])
	else:
	    lgtv.LGparser(['on'])
                
    elif(action == "SetMute") :
        mute = json_data["value"]["mute"]
        lgtv.LGparser(['mute',str(mute)])

    elif(action == "AdjustVolume") : 
        volume = json_data["value"]["volume"]
        if (volume<0): 
            lgtv.LGparser(['volumeDown'])
        else :
            lgtv.LGparser(['volumeUp'])

    elif(action == "SetVolume") : 
        volume = json_data["value"]["volume"]
        lgtv.LGparser(['setVolume', str(volume)])
    
    elif(action == "ChangeChannel") :
        channel = json_data["value"]["channel"]["number"]
        lgtv.LGparser(['setTVChannel',channel])
    
    elif(action == "SkipChannels") :
        channel = json_data["value"]["channelCount"]
        if (channel<0):
            lgtv.LGparser(['inputChannelDown'])
        else:
            lgtv.LGparser(['inputChannelUp'])
    
    elif(action == "Pause"):
        lgtv.LGparser(['inputMediaPause'])
        
    elif(action == "Play"):
        lgtv.LGparser(['inputMediaPause'])
        
    elif(action == "FastForward"):
        lgtv.LGparser(['inputMediaPause'])
        
    elif(action == "Rewind"):
        lgtv.LGparser(['inputMediaPause'])
        
    elif(action == "Stop"):
        lgtv.LGparser(['inputMediaPause'])
    
    elif(action == "SelectInput") :
        input_value = (json_data["value"]["input"]).replace(' ', '_')
        lgtv.LGparser(['setInput',input_value])
    

        
def on_error(ws, error):
    print ('ERROR LOL : ' + str(error))

def on_close(ws):
    print "### closed ###"
    # Attemp to reconnect with 2 seconds interval
    time.sleep(2)
    initiate()

def on_open(ws):
    print "### Initiating new websocket connection ###"
    

def initiate():
    #websocket.enableTrace(True)
    api = ' enter-api-here  '
    ws = websocket.WebSocketApp("ws://iot.sinric.com/",header={'Authorization:' +  base64.b64encode('apikey:   '+ api +'      ')},on_message = on_message,on_error = on_error, on_close = on_close)
    ws.on_open = on_open
	
    ws.run_forever()

if __name__ == "__main__":
    initiate()
