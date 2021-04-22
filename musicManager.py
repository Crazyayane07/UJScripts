import pygame

class MusicManager:

    def __init__(self):
        self.defaultAssetPath = ""
        self.isMusicPlaying = False
        self.currentAsset = ""

    def playMusic(self, assetPath, newVolume):
        if self.currentAsset != assetPath:
            self.currentAsset = assetPath
            self.isMusicPlaying = True
            pygame.mixer.music.load(assetPath)
            pygame.mixer.music.set_volume(newVolume)
            pygame.mixer.music.play(-1)
