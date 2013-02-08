# Python helper to wrap strings in ansi color escape sequences
#
# See all codes at http://www.termsys.demon.co.uk/vtansi.htm

import sys
import logging
import time

colorCodes = {
        'black': '0;30',
        'gray': '0;37',
        'blue':  '0;34',
        'white': '0;37',
        'green': '0;32',
        'cyan':  '0;36',
        'red':  '0;31',
        'purple': '0;35',
        'yellow': '0;33',
        'bright gray': '1;30',
        'bright blue': '1;34',
        'bright green': '1;32',
        'bright cyan': '1;36',
        'bright red': '1;31',
        'bright purple':'1;35',
        'bright yellow':'1;33',
        'normal': '0',
        'shock': '7;31',
        'accent': '1;37'
        }

def color_wrap(text, color):
    """
    Wrap the text in ascii color codes
    """
    if color not in colorCodes:
        return text

    return "\033["+colorCodes[color]+"m"+text+"\033[0m"


