import lgtv

lgtv.LGparser(['scan'])

auth_ip = input('Enter IP of TV : ')

lgtv.LGparser(['auth',auth_ip])


lgtv.LGparser(['listChannels'])
lgtv.LGparser(['listApps'])
