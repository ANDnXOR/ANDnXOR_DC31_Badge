import random
import terminal as t
import usb_cdc
import time

GROUND = '💻'
PLAYER = '💩'
OBSTACLE1 = '💾'
POS = 5
MSG_HEIGHT = 14
HEIGHT = 10
WIDTH = 80
GRAVITY = 0.5
JUMP = -2
score = 0
delay = 0.2
velocity = 0
player_y = HEIGHT - 1
obstacles = []

def cmd_dino(args):
    # Start the game
    play_game()

def init():
    t.register('💩', cmd_dino)

def cursor(x, y):
    t.output_raw(f'\033[{y+1};{x+1}H\x1b[?25l') # \x1b[?25l Hides the cursor so it doesnt flicker during screen refresh

def clear_to_end(): 
    t.output_raw('\033[K')

def clear_game():
    # Clear game board
    for y in range(1, HEIGHT):
        cursor(0, y)
        clear_to_end()

def clear_message():
    # Clear game board
    for y in range(HEIGHT, MSG_HEIGHT+8):
        cursor(0, y)
        clear_to_end()

def draw_ground():
    # Draw ground
    cursor(0, HEIGHT)
    t.output_raw('\033[32m'f'{GROUND}'*int(WIDTH*0.5)) # Compensate for the fact that the ground emoji is 2x

def draw_message():
    # Draw message
    cursor(0, MSG_HEIGHT)
    t.output_raw('\033[0;36m*Press the (ANY) key to Jump & (Q) to Quit')
    cursor(0, MSG_HEIGHT+2)
    t.output_raw('\033[0;36m*If the minor flicker of an emoji bothers you, go fix the code yourself...')
    cursor(0, MSG_HEIGHT+4)
    t.output_raw('\033[0;36m*Its not like we\'re simulating a TFT draw buffer & SPI interface over serial,\n\r leveraging ANSI escape codes mapping to an emoji extended character set,\n\r with a 115200 baud to terminal emulator bottleneck or anything')
    #For debugging 
    #cursor(0, HEIGHT+11)
    #t.output_raw(f'\033[0;36mPLAYER-X: {POS}')
    #cursor(0, HEIGHT+12)
    #t.output_raw(f'\033[0;36mPLAYER-Y: {player_y}')

def draw_game():
    global score

    clear_game()

    # Draw player
    cursor(POS, int(player_y))
    t.output_raw(PLAYER)

    # Draw obstacles
    for o in obstacles:
        if o < WIDTH-1: # -1 to deal with the buffer overflow display that draws obstacles in Col 0
            for y in range(HEIGHT-3, HEIGHT):
                cursor(o, y)
                t.output_raw(OBSTACLE1)

    cursor(0, HEIGHT+1)

def detect_collision():
    global obstacles
    for o in obstacles:
        if o-1 <= POS <= o+1:
            if player_y > HEIGHT - 3:
                # collision
                return True
    return False

def update_score():
    global score
    cursor(0, 0)
    clear_to_end()
    t.output_raw(f'\033[0;36mScore: {score}')    

def update_game():
    global obstacles, velocity, player_y, score, delay
    for i in range(0, len(obstacles)):
        new_pos = obstacles[i] - 1
        if new_pos < 0:
            new_pos = random.randint(80,110)
            score += 1
            update_score()
            delay *= 0.9 #speed up game

        obstacles[i] = new_pos

    if velocity != 0 or player_y < HEIGHT: #💩
        player_y += velocity
        velocity += GRAVITY

        if player_y >= HEIGHT - 1:                  
           velocity = 0
           player_y = HEIGHT - 1

        if player_y <= 1: 
            # This keeps dino from overflowing to POS = 1
            # Dino is hovering right under score display
            player_y = 1
            usb_cdc.data.reset_input_buffer()

        if player_y == HEIGHT - 1: 
            # This clears any queued up jumps if dino has landed on ground
            usb_cdc.data.reset_input_buffer()

def play_game():
    global score, delay, obstacles, velocity, player_y
    score = 0
    delay = 0.2
    velocity = 0
    player_y = HEIGHT - 1
    obstacles = []
    obstacles.append(80)
    obstacles.append(random.randint(100, 130))
    obstacles.append(random.randint(150, 180))
    # Clear screen
    t.cmd_clear(None)
    update_score()
    draw_ground()
    draw_message()

    while True:
        if usb_cdc.data.in_waiting > 0:
            
            b = usb_cdc.data.read(1)
            if b == b'q':
                break
            else:
                if velocity == 0:
                    if player_y > 1:
                        velocity += JUMP
                        t.output_raw('\a') # NOW WITH SOUND!
                    else:
                        usb_cdc.data.reset_input_buffer()
                        
        draw_game()
        update_game()
        if detect_collision():
            break;
        time.sleep(delay)

    end_game()

def end_game():
    global score
    clear_game()
    clear_message()
    cursor(5,5)
    t.output('\033[31mGAME OVER!')
    cursor(5,7)
    t.output(f'\033[31mFINAL SCORE: {score}\r\n\r\n')