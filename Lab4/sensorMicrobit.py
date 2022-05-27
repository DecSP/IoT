def on_received_string(receivedString):
    global list2, recvFromId, recvId, recvData
    list2 = receivedString.split("-")
    recvFromId = parse_float(list2[0])
    if recvFromId == 0:
        recvId = parse_float(list2[1])
        recvData = list2[2]
        if recvId == id2:
            basic.show_string("" + (recvData))
        else:
            basic.show_string("" + (recvData))
radio.on_received_string(on_received_string)

recvData = ""
recvId = 0
recvFromId = 0
list2: List[str] = []
id2 = 0
radio.set_group(1)
id2 = 1

def on_forever():
    radio.send_string("" + str(id2) + "-" + "!" + str(id2) + ":TEMP:" + str(input.temperature()) + "#")
    basic.pause(5000)
    radio.send_string("" + str(id2) + "-" + "!" + str(id2) + ":LIGHT:" + str(input.light_level()) + "#")
    basic.pause(5000)
basic.forever(on_forever)
