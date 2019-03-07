import string
from ctypes import windll
import time
import os


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in  string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


if __name__ == '__main__':
    before = set(get_drives())
    while True:
        after = set(get_drives())
        drives = after - before
        delta = len(drives)
        if (delta):
            for drive in drives:
                if os.system("cd " + drive + ":") == 0:
                    newly_mounted = drive
                    print("There were %d drives added: %s. Newly mounted drive letter is   %s" % (delta, drives, newly_mounted))
