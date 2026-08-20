import pygame
import random
import time
import threading

class BackgroundMusicPlayer:
    def __init__(self, playlist, volume=0.5):
        """Initializes the background music thread. Volume accepts 0.0 to 1.0."""
        self.playlist = list(playlist)
        self.is_paused = False
        self.is_running = True
        
        # Ensure mixer is initialized
        if not pygame.mixer.get_init():
            raise RuntimeError("pygame.mixer must be initialized in the main thread before starting the music player.")
        pygame.mixer.music.set_volume(volume)
        
        # Build and start background thread
        self.thread = threading.Thread(target=self._play_music_forever, daemon=True)
        

    def _play_music_forever(self):
        """Internal background loop running on a separate thread."""
        while self.is_running:
            random.shuffle(self.playlist)
            for song in self.playlist:
                if not self.is_running:
                    break
                self.thread.start()
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                
                # Catch pauses that happened during track transitions
                if self.is_paused:
                    pygame.mixer.music.pause()

                # Loop while song is active, or if user explicitly paused it
                while (pygame.mixer.music.get_busy() or self.is_paused) and self.is_running:
                    time.sleep(0.5)

    def toggle_pause(self):
        """Toggles between pause and unpause."""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("Music unpaused.")
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("Music paused.")

    def change_volume(self, amount):
        """Adjusts volume relatively (e.g., -0.1 to lower, 0.1 to raise)."""
        current_volume = pygame.mixer.music.get_volume()
        new_volume = max(0.0, min(1.0, current_volume + amount))
        pygame.mixer.music.set_volume(new_volume)
        print(f"Volume set to: {int(new_volume * 100)}%")

    def skip_song(self):
        """Forces the current song to stop, triggering the next song in line."""
        pygame.mixer.music.stop()
        # If skipped while paused, unpause so the next song actually starts
        if self.is_paused:
            self.is_paused = False