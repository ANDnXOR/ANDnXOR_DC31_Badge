# AND!XOR DC31 Badge #

This is a partial dump of source for the badge. The rest will come later. Full documentation is in `RTFM.md`.

## Troubleshooting ##

### My USB doesn't work ###

1. Check your USB-C cable is not a charge-only. This is sadly quite common. Or test with a different cable as quality varies.
2. Check the slide switch on the back is set to "USB" - we learned this the hard way __a-lot__

### My badge stopped doing bling ###

1. Plug into USB-C, check for a `SNACKEYJR` or `CIRCUITPY` is mounted
2. If only a single file remains, you will need to copy new python files to the badge
3. Copy the contents of the `src/` folder from this report recursively onto the badge, you should have `code.py` and `boot.py` in the root folder of the badge
4. Wait patiently
5. Your badge should bling again