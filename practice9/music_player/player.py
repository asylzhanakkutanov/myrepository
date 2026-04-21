import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        # 🔥 файл тұрған папканы дәл табамыз
        self.base_path = os.path.dirname(__file__)
        self.music_folder = os.path.join(self.base_path, "music")

        self.playlist = ["All Eyez On Me (feat. Big Syke) - 2Pac.wav", "Sheker - Darkhan Juzz.wav", "My Own Summer (Shove It) - Deftones (online-audio-converter.com).wav"]

        self.index = 0

    def load(self):
        path = os.path.join(self.music_folder, self.playlist[self.index])

        print("Loading:", path)  # 🔥 debug үшін (өте пайдалы)

        pygame.mixer.music.load(path)

    def play(self):
        self.load()
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def current(self):
        return self.playlist[self.index]