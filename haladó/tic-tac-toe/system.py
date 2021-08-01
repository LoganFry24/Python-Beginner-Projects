#this class check the operating system
import sys
import os
class System:
    def __init__(self):
        # windsows
        if sys.platform.startswith('win32'):
            os.system('cls')
        # linux and OS X
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            os.system('clear')