import pygame
import threading
import time
import random
import os

pygame.mixer.init()
MUSIC_DIR="music"
playlist=[
    (os.path.join(MUSIC_DIR, "bliss.mp3"), "Bliss", "Kevin MacLeod"),
    (os.path.join(MUSIC_DIR, "onhold.mp3"), "On Hold", "Kevin MacLeod"),
    (os.path.join(MUSIC_DIR, "arms.mp3"), "In Your Arms", "Kevin MacLeod")]
def _music_loop():
    remaining=playlist.copy()
    random.shuffle(remaining)
    while True:
        if not remaining:
            remaining=playlist.copy()
            random.shuffle(remaining)
        filename,title,artist=remaining.pop()
        print(f"Now playing: {title}")
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
def start_music():
    thread=threading.Thread(target=_music_loop,daemon=True)
    thread.start()
