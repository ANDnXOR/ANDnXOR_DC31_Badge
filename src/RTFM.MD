# RTFM #

![AND NOT EX-OR DEF CON 31 Logo](img/dc31_logo.png "AND!XOR DC31 Logo").

So you got an AND!XOR DEF CON 31 5n4ck3y-7r badge? Here's what you should know...

## TLDR ##

1. It is a hacker tool and functions as a Rubber Ducky (See Ducky section below)
2. It has hacker challenges accessible from the serial terminal (See B.E.N.D.E.R. section below)
3. It needs to be activated in order for the challenges to work (See 5n4ck3y section below)

# License #

Made with beer and late nights in California.

(C) Copyright 2017-2023 AND!XOR LLC (https://andnxor.com/).

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

**ADDITIONALLY:**

If you find this source code useful in any way, use it in another electronic
conference badge, or just think it's neat. Consider buying us a beer
(or two) and/or a badge (or two). We are just as obsessed with collecting
badges as we are in making them.

**Contributors:**

* @andnxor
* @zappbrandnxor
* @hyr0n1
* @Cr4bf04m
* @lacosteaef
* @f4nci3
* @ellwoodthewood
* @humanrevision
* @kur3us
* @mlaan
* @5n4ck3y

**Sponsors:**
* Urbane Security - https://urbanesecurity.com/
* CTFd - https://ctfd.io/
* w00w00 
* Philanthropists

# Hardware #
* MCU - Raspberry Pi Pico RPI2040
* Flash - Winbond 25Q128JVSM
* I2C Multiplexer - NXP PCA9615
* Power Multiplexer - TI TPS2114
* Ponoko Laser Cut Acrylic
* Zapp Laser Cut Pine Wood 
* Macrofab PCB Assembly
* Power - AAA batteries

# Firmware #

* Adafruit Circuitpython 8.0.5
* B.E.N.D.E.R. - Hacker Challenges
* Ducky - Scripted keyboard emulation when you plug in to USB ports
* Bling - Displays static & animated images to your screen
* Other hidden challenges and lulz

# 5n4ck3y (aka Snackey) #

The newest member of AND!XOR, fully responsible for handing out free badges. Intern 4 life. Look for them in the conference... 

If your summercamp-fam are jealous and want to earn a free badge through hacking challenges, go see 5n4ck3y in the DEF CON Contest Area.

Let's explain 5n4ck3y, the challenge, and how this all pulls together. 
* 5n4ck3y (aka Snackey) is the vending machine dispensing badges
* 5n4ck3y-7r (aka Snackey Jr) is this year's badge
* The challenge scoreboard for both 5n4ck3y & 5n4ck3y-7r are hosted on the CTFd 5n4ck3y Challenge site (see links below). Yes, you hack on challenges to earn a badge and it continues once you have a badge in your possession. It's a cumulative scoreboard.

The general process one will follow:

1. Register at 5n4ck3y Challenge with a REAL e-mail address.
2. The first challenge is IRL physical verification with 5n4ck3y, this will unlock badge dispensing challenges in CTFd.
3. Solve two of those and earn an SAO, solve three and earn badge.
4. Once you have a badge in your possession, there is further physical verification & activation with 5n4ck3y-7r; this will unlock the B.E.N.D.E.R. challenges. 
5. Solve those and earn street cred?

Instructions for physical verification(s) are on the specific challenge group of the CTFd site.

If you received a badge early due to being a Philanthropist, the CTFd site will go online 11 August 2023 at 10am Vegas Standard Time. If you happen to visit it before then it will be offline and/or password protected. This is NOT part of the challenge, wait patiently. Here you can get your challenge activation once registering. It will also be posted to our Github after DEF CON 31 ends. Just view the most recent version of RTFM.md and download the latest repository with the activation files.

# Badge Enabled Non Directive Enigma Routine (B.E.N.D.E.R) #

Our badge flavor of CTF. Every year is a different challenge. We hope you enjoy it!

THE BADGE CHALLENGES REQUIRE ACTIVATION AND WILL BE DONE USING THE 'REDACTED' COMMAND. 
INSTRUCTIONS ARE ON CTFd AND WILL BE POSTED TO GITHUB AFTER THE CON.

This requires use of a serial terminal, we HIGHLY recommend picocom because it supports extended character translation to... emojis. You're free to do what you want but if you choose to use a terminal that doesn't support the extended character set... gonna have a bad time. 

There are multiple serial UARTs on the badge, depending on your OS of choice and how many other serial devices you have plugged in, their device number will vary from system to system. What we can generally say is that the first terminal (X) is the badge's debug and maintenance view which AND!XOR uses for provisioning, the second one is B.E.N.D.E.R (X+1). You want the second one. Note we will save you time, the maintenance terminal is not part of the CTF, there are no flags there. This is not a wink wink there ARE no flags there, this us not wanting to waste your time and connect to the wrong terminal. Note the baud rate is 115200 but that is default so you do not need to explicitly put "-b 115200" as an argument.

Plug the badge in to a Linux computer via USB then...
```
$ picocom /dev/ttyACM(X+1)
```

Or Plug the badge in to a MacOS computer via USB then...
```
$ picocom /dev/tty.usbmodem1*3
```

**NOTE: If backspace is misbehaving add `--omap bsdel` option to picocom**

Or Plug the badge in to a Windows computer via USB then...

(we highly recommend just run an Ubuntu Virtual Machine at this point and not deal with COM devices)

Once you are logged in press the ANY key...follow the instructions for activation on CTFd (or Github)...then figure it out....and have fun!

# Ducky #

In case you do not know, a USB Rubber Ducky is a device which emulates a keyboard. You can write ducky scripts, plug the badge into a USB port, and the badge will automate typing, hotkeys, window pop ups...whatever you want! We've included the Adafruit Circuity Python Ducky library. Documentation is located at: https://docs.circuitpython.org/projects/ducky/en/latest/. This is not emulating a full Hak5 Rubber Ducky which can also act as non keyboard devices (storage, mouse, etc). This means "ATTACKMODE HID STORAGE" isn't a thing on this badge, and only Ducky 1.0 scripts are supported.


By default, *ducky1.txt* is the script ran every time. There is a command line interface as well. Connect the badge in the same way you access B.E.N.D.E.R. using picocom then...launch using the 🦆 command

```
BENDER $ 🦆
Usage: $ 🦆 run <file>
Usage: $ 🦆 set <file>
Default file: ducky1.txt
```
It's pretty self explanatory. 

The "run" argument will let you execute a different non default file. 

The "set" argument will change the default file.

The default file is run when both capacitive touch buttons are held on the back of the badge.

Finally you're probably asking, what's the syntax for ducky script and what does our badge support? 

Ducky on CircuitPython is a subset of the available Hak5 USB Ducky commands. What does our badge support?
* DELAY, STRING, REPEAT, DELETE, HOME, END, INSERT, PAGEUP, PAGEDOWN, ESC, ESCAPE, UP, DOWN, LEFT, RIGHT
* F1...F12, SPACE, TAB ENTER, BREAK, PAUSE, CAPSLOCK, NUMLOCK, SCROLLLOCK, FN, MENU, WINDOWS
* GUI, SHIFT, ALT, CTRL
* LED_R, LED_G, LED_B, LED_OFF

Note: We have extended the base adafruit library with LED controls for added compatibility with certain Hak5 scripts. One, because LED's are awesome... and two... well Hak5 didnt have LED_B so that makes our new command like 33% better right?

We have included some example, benign ducky scripts for lulz. Find them in "/ducky_scripts" and tailor for your own PoCs. Also be sure to check out the Hak5 ducky repository and command reference for inspiration:
* https://github.com/hak5/usbrubberducky-payloads
* https://docs.hak5.org/hak5-usb-rubber-ducky/ducky-script-basics/keystroke-injection

# Bling #
If you were sad that this year's badge is without screen, therefore lacking animations with your blinky lights, fret not.  

The 🌈 "bling" command lets you change the LED bling modes by passing an argument 0...5

The 🥜 "jiff" command walks you through the steps of displaying ANSI static or animated images stored on the badge. Based on the source provided by Balssh ASCIIArt project, it was modified to produce images limited by the height of the terminal, not the width. Without getting into details, the limiting factor on animation "framerate" of attempting to do an animated jiff over serial with ANSI... is the rows. Make it bigger, more resolution, but it's slower and choppier. Make it smaller, it's faster, and a smudge. We believe we found the sweet spot. Make your own and experiment! The modified source of the ascii art project along with a bash script for your lazy assess will be placed on our github.

# Troubleshooting #
Usually the main issue people have when they first try and connect to hardware over serial, is that the default permissions do not belong to them in the OS; e.g. you try and launch picocom (or any other serial program and DENIED). Add yourself to the dialout group. If you do not know what that means, visit: https://gprivate.com/65a4f

For a quick reset from BENDER CLI you can use the "💻" reboot command

Otherwise if you are having issues with the badge for any reason, try the #troubleshooting channel of our Discord. You could also swing by the contest area.

Given the structure of our discord channels, this is what is meant for what:

Channel -> Subchannel
* 5n4ck3y -> General banter and Q&A about 5n4ck3y
* Badge & CTF -> DC31 :: General collaborative non-spoiler discussion for people working on badge challenges and if there are any issues try crowdsourcing troubleshooting here if we cant get to you right away.

# Links #
* Twitter: https://twitter.com/ANDnXOR
* Github: https://github.com/ANDnXOR/ANDnXOR_DC31_Badge
* Discord: https://discord.gg/DeXNEydE2r
* 5n4ck3y Challenge: https://5n4ck3y.ctfd.io/
* ANSI Conversion Source: https://github.com/Balssh/asciiart
* Adafruit Ducky for CircuitPython Source: https://github.com/adafruit/Adafruit_CircuitPython_Ducky

![AND NOT EX-OR DEF CON 31 Footer Logo](img/dc31_logo_footer.png "AND!XOR DC31 Logo").