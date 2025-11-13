# services/audio.py
import os
import time
import platform

def play_beep():
    """Plays a beep sound (cross-platform)."""
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 500)  # frequency, duration
    elif system == "Darwin":
        os.system('say "beep"')
    else:
        os.system('play -nq -t alsa synth 0.5 sine 1000')
