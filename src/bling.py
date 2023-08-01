import asyncio
import adafruit_dotstar
import adafruit_fancyled.adafruit_fancyled as fancy
import math
from random import randint
import board
import roberto as r

# Define the number of LEDs and the pin connections
led_strip = None
num_pixels = 7
led_pin = board.GP24
clock_pin = board.GP25

MAX_LED = 5
LEFT = 5
RIGHT = 6

CLOCKWISE_ORDER = [0, 1, 2, 4, 3]
COL_ORDER = [[4],[2, 3],[0, 1]]

bling_hue = 0

eye_max_hue = 0
eye_hue_step = 0.01

override_mode = 0
OVERRIDE_MODE_UNLOCK = 1000

# Bling override flash state
flash_counter = 0
flash_color = 0

circle_index = 0
circle_hue = 0
circle_dir = 0.5

fade_hue = 0

defcon_hue = 0
defcon_palette = [fancy.CRGB(105, 110, 161), fancy.CRGB(131,200,190), fancy.CRGB(236,218,36), fancy.CRGB(247,162,139)]

def _hue_to_rgb(hue):
    hsv = fancy.CHSV(hue, 1.0, 1.0)  
    return fancy.CRGB(hsv).pack()

def cmd_bling(args):
    import terminal as t
    global bling_mode, bling_modes

    valid_modes = list(range(len(bling_modes)))  # Valid bling mode options

    if len(args) == 0:
        num_modes = len(bling_modes)
        t.output(f'Usage to change mode: $ 🌈 0..{num_modes-1}')
        t.output(f'Current bling mode: {bling_mode}\n')
        
    elif len(args) == 1:
        if args[0] == 'test':
            t.output('Testing bling override')
            override_start(OVERRIDE_MODE_UNLOCK)
            return
        try:
            mode = int(args[0])
            if mode in valid_modes:
                bling_mode = mode
                t.output(f'Bling mode set to: {bling_mode}\n')
            else:
                t.output('Invalid bling mode\n')
        except:
            t.output('Invalid argument\n')
    else:
        t.output('Invalid argument(s)\n')

def init():
    global led_strip
    led_strip = adafruit_dotstar.DotStar(clock_pin, led_pin, num_pixels, brightness=0.03, auto_write=False)
    update_eye_bling()

def init2():
    """
    2nd stage bling init
    """
    try:
        import terminal as t
        t.register('🌈', cmd_bling)
        r.set_badge_health('Bling', True)
    except Exception as e:
        r.set_badge_health('Bling', e)

def clear():
    for i in range(0, num_pixels):
        led_strip[i] = (0,0,0)
    led_strip.show()

def next():
    global bling_mode, bling_count_enabled
    bling_mode = (bling_mode + 1) % bling_count_enabled

def prev():
    global bling_mode, bling_count_enabled
    bling_mode -= 1
    if bling_mode < 0:
        bling_mode += bling_count_enabled

def override_start(mode):
    """
    Override current bling
    """
    global override_mode
    override_mode = mode

def override_stop():
    """
    Returns bling mode to normal
    """
    global override_mode
    override_mode = 0

def bling_mode_circle():
    global circle_index, circle_hue, MAX_LED
    if circle_index >= MAX_LED:
        circle_index = 0
    if circle_hue >= 1:
        circle_hue = 0
    rgb = _hue_to_rgb(circle_hue)
    led_strip[CLOCKWISE_ORDER[int(circle_index)]] = rgb

    circle_index += 1
    circle_hue += 0.03

def bling_mode_circle_white():
    global circle_index, circle_dir
    if circle_index >= MAX_LED - 1:
        circle_dir = -0.5
        circle_index = MAX_LED - 1
    elif circle_index <= 0:
        circle_dir = 0.5
        circle_index = 0
    for j in range(0, MAX_LED):
        led_strip[j] = (0, 0, 0)
    led_strip[CLOCKWISE_ORDER[int(math.floor(circle_index))]] = (255, 255, 255)
    circle_index += circle_dir

def bling_mode_fade():
    global fade_hue
    if fade_hue >= 1:
        fade_hue = 0
    set_all_hue(fade_hue)
    fade_hue += .03

def bling_mode_fade_stars():
    bling_mode_fade()
    i = randint(0, MAX_LED)
    led_strip[i] = (255, 255, 255)

def bling_mode_defcon_sweep():
    global defcon_hue, defcon_palette
    if defcon_hue >= 1:
        defcon_hue = 0

    hue_step = 0
    for col in COL_ORDER:
        for i in col:
            led_strip[i] = fancy.palette_lookup(defcon_palette, defcon_hue + hue_step).pack()
        hue_step += .1

    defcon_hue += .03

def bling_mode_rainbow():
    global bling_hue, MAX_LED
    for i in range(0, MAX_LED):
        led_strip[i] = _hue_to_rgb(bling_hue)
        bling_hue += 0.03
        if bling_hue > 1:
            bling_hue -= 1

async def bling_task():
    global led_strip, bling_modes, bling_mode, override_mode

    try:
        eh = 0
        eye_dir = 1
        while True:
            if override_mode == OVERRIDE_MODE_UNLOCK:
                override_flash()
            else:
                mode = bling_modes[bling_mode]
                mode()

            # eyes
            ec = _hue_to_rgb(eh)
            eh += eye_dir * eye_hue_step
            if eh > eye_max_hue:
                eye_dir = eye_dir * -1
                eh = eye_max_hue
            elif eh < 0:
                eye_dir = eye_dir * -1
                eh = 0
                
            led_strip[LEFT] = led_strip[RIGHT] = ec

            # update all LEDs
            led_strip.show()
            await asyncio.sleep(0.05)
    except Exception as e:
        r.set_badge_health_exception('Bling', e)

def set_all_all_hue(hue):
    global led_strip, num_pixels
    rgb = _hue_to_rgb(hue)
    for i in range(0, num_pixels):
        led_strip[i] = rgb
    led_strip.show()

def set_all_hue(hue):
    global led_strip
    rgb = _hue_to_rgb(hue)
    for i in range(0, MAX_LED):
        led_strip[i] = rgb
    led_strip.show()

def override_flash():
    global flash_counter, flash_color
    if flash_counter > 2:
        flash_counter = 0
        if flash_color == 255:
            flash_color = 0
        else:
            flash_color = 255
    flash_counter += 1

    for j in range(0, MAX_LED):
        led_strip[j] = (flash_color, flash_color, flash_color)

def set_eye_color(r, g, b):
    # temporarily set eye color during stages like boot
    led_strip[LEFT] = led_strip[RIGHT] = (r, g, b)
    led_strip.show()

def update_eye_bling():
    global eye_max_hue, eye_hue_step
    progress = r.get_badge_progress()
    # Start with limited hues
    eye_max_hue = 0.2
    max_hue_step = 0.8 / len(r.BADGE_PROGRESS_NON_BENDER)

    eye_hue_step = 0.01
    
    for mask in r.BADGE_PROGRESS_NON_BENDER:
        if (progress & mask) > 0:
            eye_max_hue += max_hue_step
    for mask in r.BADGE_PROGRESS_BENDER:
        if (progress & mask) > 0:
            eye_hue_step += .015

bling_modes = [
    bling_mode_circle_white,
    bling_mode_defcon_sweep,
    bling_mode_fade_stars, 
    bling_mode_fade, 
    bling_mode_circle, 
    bling_mode_rainbow, 
]
bling_mode = 0
bling_count_enabled = 6