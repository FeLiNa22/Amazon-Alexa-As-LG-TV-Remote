from __future__ import print_function
import sys
import os
import json
from inspect import getargspec
from LGTV import LGTVScan, LGTVClient, getCommands


def usage(error=None):
    if error:
        print ("Error: " + error)
    print ("LGTV Controller")
    print ("Author: Karl Lattimer <karl@qdh.org.uk>")
    print ("Usage: lgtv <command> [parameter]\n")
    print ("Available Commands:")

    print ("  scan")
    print ("  auth                  Hostname/IP    Authenticate and exit, creates initial config ~/.lgtv.json")

    for c in getCommands(LGTVClient):
        print ("  " + c, end=" ")
        print (" " * (20 - len(c)), end=" ")
        args = getargspec(LGTVClient.__dict__[c])
        print (' '.join(args.args[1:-1]))


def parseargs(command, argv):
    args = getargspec(LGTVClient.__dict__[command])
    args = args.args[1:-1]

    if len(args) != len(argv):
        raise Exception("Argument lengths do not match")

    output = {}
    for (i, a) in enumerate(args):
        #
        # do some basic conversions for bools, ints and floats
        #
        if argv[i].lower() == "true":
            argv[i] = True
        elif argv[i].lower() == "false":
            argv[i] = False
        try:
            f = int(argv[i])
            argv[i] = f
        except:
            try:
                f = float(argv[i])
                argv[i] = f
            except:
                pass
        output[a] = argv[i]
    return output

def searchTVchannels(TV_Channel):
	with open('tvlists.json') as f:
		ChannelList = json.load(f)
	for channel in ChannelList:
		if channel['channelNumber'] == TV_Channel:
		    return channel['channelId']
	print('NO CHANNEL FOUND')
		    
def searchApps(App_Name):
	with open('applists.json') as f:
		AppList = json.load(f)
	for app in AppList:
		if (app['title'].lower() == App_Name.lower()):
		    return app['id']
		

def LGparser(AlexaCommand):
    if len(AlexaCommand) < 1:
        usage("Too few arguments")
    elif AlexaCommand[0] == "scan":
        results = LGTVScan()
        if len(results) > 0:
            print (json.dumps({
                "result": "ok",
                "count": len(results),
                "list": results
            }, sort_keys=True, indent=4))
        else:
            print (json.dumps({
                "result": "failed",
                "count": len(results)
            }, sort_keys=True, indent=4))

    elif AlexaCommand[0] == "on":
        ws = LGTVClient()
        ws.on()

    elif AlexaCommand[0] == "auth":
        if len(AlexaCommand) < 2:
            usage("Hostname or IP is required for auth")
        
        if os.path.exists("lgtv.json"):
            os.remove("lgtv.json")
            
        ws = LGTVClient(AlexaCommand[1])
        ws.connect()
        ws.run_forever()
    else:
        try:
            ws = LGTVClient()
            try:
	        if AlexaCommand[0] == "setTVChannel" :
		        AlexaCommand[1] = searchTVchannels(AlexaCommand[1])
		elif AlexaCommand[0] == "startApp" :
		        AlexaCommand[1] = searchApps(AlexaCommand[1])
                args = parseargs(AlexaCommand[0], AlexaCommand[1:])
            except Exception as e:
                usage(e.message)
            ws.connect()
            ws.exec_command(AlexaCommand[0], args)
            ws.run_forever()
        except KeyboardInterrupt:
            ws.close()
