def on_received_string(receivedString):
    global list2, recvFromId, recvData
    list2 = receivedString.split("-")
    recvFromId = parse_float(list2[0])
    if recvFromId != 0:
        recvData = list2[1]
        serial.write_string("" + (recvData))
        basic.show_string("" + (recvData))
radio.on_received_string(on_received_string)

def on_data_received():
    global cmd
    cmd = serial.read_until(serial.delimiters(Delimiters.HASH))
    if cmd == "0":
        radio.send_string("0-1-0")
    elif cmd == "1":
        radio.send_string("0-1-1")
    elif cmd == "2":
        radio.send_string("0-2-0")
    elif cmd == "3":
        radio.send_string("0-2-1")
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

cmd = ""
recvData = ""
recvFromId = 0
list2: List[str] = []
radio.set_group(1)
id2 = 0