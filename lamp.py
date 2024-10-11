def on_received_number(receivedNumber):
    global mode, submode, work
    mode = Math.round(receivedNumber / 100)
    submode = receivedNumber % 100
    if mode == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        work = False
    else:
        basic.show_number(mode)
        work = True
radio.on_received_number(on_received_number)

light2 = 0
submode = 0
work = False
mode = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 16, NeoPixelMode.RGB)
radio.set_group(61)
radio.set_transmit_power(7)
mode = 0
work = False
color = 0
onoff = True
basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)

def on_forever():
    global work, light2, color
    while work:
        if mode == 1:
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            work = False
        elif mode == 2:
            light2 = 5 + submode * 25
            strip.show_color(neopixel.rgb(light2, light2, light2))
            work = False
        elif mode == 3:
            light2 = 5 + submode * 25
            strip.show_color(neopixel.rgb(255, 255, light2))
            work = False
        elif mode == 4:
            strip.show_color(neopixel.hsl(color, 100, 50))
            color += 10
            work = False
        elif mode == 5:
            if input.light_level() <= 10:
                strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
            else:
                strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            basic.pause(200)
        elif mode == 6:
            if input.temperature() < 18:
                strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            elif input.temperature() < 21:
                strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
                if input.temperature() < 25:
                    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
                else:
                    strip.show_color(neopixel.colors(NeoPixelColors.RED))
                basic.show_number(input.temperature())
                work = False
                basic.show_number(mode)
        elif mode == 7:
            strip.show_color(neopixel.rgb(10, 10, 10))
            work = False
        else:
            strip.show_color(neopixel.hsl(color, 100, 50))
            color += 10
            basic.pause(500)
basic.forever(on_forever)
