def on_data_received():
    global cmd
    cmd = serial.read_until(serial.delimiters(Delimiters.HASH))
    basic.show_string(cmd)
    if cmd == "0":
        basic.show_leds("""
            . # # # .
                        . # . # .
                        . # . # .
                        . # . # .
                        . # # # .
        """)
    elif cmd == "1":
        basic.show_leds("""
            . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        . # # # .
        """)
    elif cmd == "2":
        basic.show_leds("""
            . # # # .
                        . . . # .
                        . # # # .
                        . # . . .
                        . # # # .
        """)
    elif cmd == "3":
        basic.show_leds("""
            . # # # .
                        . . . # .
                        . # # # .
                        . . . # .
                        . # # # .
        """)
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

typ = 0
cmd = ""
period = 0

def on_forever():
    global period, typ
    if period == 0:
        period = 5
        if typ == 0:
            serial.write_string("!1:TEMP:" + ("" + str(input.temperature())) + "#")
            typ = 1
        else:
            serial.write_string("!1:LIGHT:" + ("" + str(input.light_level())) + "#")
            typ = 0
    period = period - 1
    basic.pause(1000)
basic.forever(on_forever)
