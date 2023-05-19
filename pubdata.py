import wiotp.sdk.device
import time
import random

myConfig = { 
    "identity": {
        "orgId": "XXXXXXX",
        "typeId": "XXXXXXXXX",
        "deviceId":"XXXXXXX"
    },
    "auth": {
        "token": "XXXXXXXXXXXXXXXX"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(0,50)
    hum=random.randint(0,50)
    duration=random.randint(1,5)
   
    uSvh=round(random.uniform(0,1),2)
    cpm=round(random.uniform(1,5),2)
    myData={'temperature':temp, 'humidity':hum,'duration':duration, 'uSvh':uSvh, 'cpm':cpm}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
