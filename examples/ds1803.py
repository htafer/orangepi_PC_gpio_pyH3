#!/usr/bin/env python
from itertools import cycle
from time import sleep
"""Read from the EEPROM chip on A20-OLinuXino-MICRO

On the board there is small chip U3. This is 16kb eeprom memory AT24C16BN.
The i2c address can be different, but on this specific board is 0x50.

The text will be big mess if python3 is used.
"""

from pyA20 import i2c

__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"

eeprom_address = 0x28

"""Initialize i2c bus"""
i2c.init("/dev/i2c-1")
i2c.open(eeprom_address)

"""while loop between 0 and 255"""

n=255
li = range(1, 255+1) + range(n, 0, -1)
ti=cycle(li);

while True:
    sleep(0.01)
    i2c.write([0xAA,next(ti)])

i2c.close()
