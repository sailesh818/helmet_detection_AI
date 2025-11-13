import os
import time
import platform

def play_beep():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    elif system == "Darwin":
        os.system('say "beep"')
    else:
        os.system('play -nq -t alsa synth 0.5 sine 1000')
