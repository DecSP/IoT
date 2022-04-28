print("Xin chào ThingsBoard")
import paho.mqtt.client as mqttclient
import time
import json
import random
import serial.tools.list_ports

mess = ""
bbc_port = ""

if len(bbc_port) > 0:
    ser = serial.Serial(port=bbc_port, baudrate=115200)

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if len(splitData)==3:
        t,dev,val=splitData
        if dev=='TEMP':
            client.publish('v1/devices/me/telemetry',json.dumps({'temperature':int(val)}),1)
        if dev=='LIGHT':
            client.publish('v1/devices/me/telemetry',json.dumps({'light':int(val)}),1)

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "AfKNmj5wuSyVnUC68wxB"


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


def recv_message(client, userdata, message):
    print("Received: ", message.payload.decode("utf-8"))
    cmd=0
    temp_data = {}
    try:
        jsonobj = json.loads(message.payload)
        if "setValue" in jsonobj['method']:
            dev=jsonobj['method'][len('setValue'):]
            temp_data['value'+dev] = jsonobj['params']
            client.publish('v1/devices/me/attributes', json.dumps(temp_data), 1)

            cmd=jsonobj['params']
            cmd|=(dev=='PUMP')<<1
    except:
        pass
    
    if len(bbc_port) > 0:
        ser.write((str(cmd) + "#").encode())


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/rpc/request/+")
    else:
        print("Connection is failed")


client = mqttclient.Client("Gateway_Thingsboard")
client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message

while True:
    if len(bbc_port)>0:
        readSerial()
    time.sleep(1)