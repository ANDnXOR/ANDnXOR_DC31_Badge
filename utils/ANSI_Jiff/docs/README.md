# ASCII art converter


Simple script to convert an image to an ANSI representation of it

Prerequisites
-
You need to have python installed and then run the following commands:

```bash
git clone https://github.com/Balssh/asciiart
cd asciiart
pip install -r requirements.txt
```

Usage
-
```
python3 art_andnxor_fork.py [-i] [-h] [-f]

- i     the path to the image
- w     the height of the ascii image
- f     whether or not the foreground of the characters is set (default is set to False)
```

Example
-
```bash
python3 art.py -i wave.jpg -w 100
```
Converts the image
![Wave](wave.jpg)

to the ASCII representation
![Wave_ascii](ascii_wave.jpg)
