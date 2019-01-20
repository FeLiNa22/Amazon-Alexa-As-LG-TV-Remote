import lgtv

LGparser(['scan'])

auth_ip = input('Enter IP of TV : ')
LGparser(['auth',auth_ip])

LGparser(['listChannels'])
LGparser(['listApps'])
