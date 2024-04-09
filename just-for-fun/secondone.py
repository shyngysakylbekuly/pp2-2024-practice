import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load('drift.mp3')

# Play the loaded MP3 file
pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Adjust the tick rate if needed

# Clean up when finished
pygame.mixer.quit()
pygame.quit()
sys.quit()
