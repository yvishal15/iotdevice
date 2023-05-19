import wiotp.sdk.device
import time
import random
import names
myConfig = { 
    "identity": {
        "orgId": "xxxxxx",
        "typeId": "xxxxx",
        "deviceId":"xxxxx"
    },
    "auth": {
        "token": "xxxxxxxxx"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

#while True:
id=random.randint(-20,125)
name=names.get_full_name()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

myData={'id':id, 'names':name, 'entrytime':current_time}
client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
print("Published data Successfully: %s", myData)
client.commandCallback = myCommandCallback
#time.sleep(2)
client.disconnect()
