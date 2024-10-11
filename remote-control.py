def my_function():
    global onoff
    onoff = not (onoff)
    if onoff:
        radio.send_number(mode + submode)
        basic.show_number(Math.round(mode / 100))
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        radio.send_number(0)
WSJoyStick.on_key(KEY.D, my_function)

onoff = False
submode = 0
mode = 0
WSJoyStick.joy_stick_init()
mode = 100
submode = 10
onoff = False
radio.set_group(61)
radio.set_transmit_power(7)
answer = 0
basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)

def on_forever():
    global mode, submode
    if onoff:
        if WSJoyStick.Listen_Dir(DIR.U):
            mode += 100
            if mode > 800:
                mode = 800
            radio.send_number(mode + submode)
            basic.show_number(Math.round(mode / 100))
        if WSJoyStick.Listen_Dir(DIR.D):
            mode += -100
            if mode < 100:
                mode = 100
            radio.send_number(mode + submode)
            basic.show_number(Math.round(mode / 100))
        if WSJoyStick.Listen_Dir(DIR.R):
            submode += 1
            if submode > 10:
                submode = 10
            radio.send_number(mode + submode)
            basic.show_number(Math.round(mode / 100))
        if WSJoyStick.Listen_Dir(DIR.L):
            submode += -1
            if submode < 1:
                submode = 1
            radio.send_number(mode + submode)
            basic.show_number(Math.round(mode / 100))
basic.forever(on_forever)
