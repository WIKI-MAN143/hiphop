import os, sys

try:

    __import__("man").wm()

except Exception as e:

    exit(str(e))
