from sinric import SinricPro
from credentials import appKey, secretKey, tvId, deviceIdArr
from sinric import SinricProUdp

def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE

        # client.event_handler.raiseEvent(tvId, 'setVolume',data={'volume': 0})
        # client.event_handler.raiseEvent(tvId, 'mediaControl',data={'control': 'FastForward'})
        # client.event_handler.raiseEvent(tvId, 'changeChannel',data={'name': 'HBO'})
        # client.event_handler.raiseEvent(tvId, 'selectInput',data={"input":"HDMI"})
        pass

event_callback = {
    'Events': Events
}


def onPowerState(deviceId, state):
    # Do Something
    return True, state


def onSetVolume(deviceId, volume):
    print('Volume : ', volume)

    # Do Somethign
    return True, volume


def onAdjustVolume(deviceId, volume):
    print('Volume : ', volume)
    # Do something with volume
    return True, volume


def onMediaControl(deviceId, control):
    # Do something with control
    return True, control


def onSelectInput(deviceId, input):
    # Do something with input
    return True, input


def onChangeChannel(deviceId, channelName):
    # Change Channel
    return True, channelName


def onSkipChannels(deviceId, channelCount):
    # Skip them
    return True, channelCount


callbacks = {
    'powerState': onPowerState,
    'setVolume': onSetVolume,
    'adjustVolume': onAdjustVolume,
    'mediaControl': onMediaControl,
    'selectInput': onSelectInput,
    'changeChannel': onChangeChannel,
    'skipChannels': onSkipChannels
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,
        event_callbacks=event_callback, enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)