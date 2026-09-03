import pygame
class CubeManager:
    def __init__(self, original_image):
        self.original_image = original_image
        self.current_angle = 0.0
        self.target_angle = 0.0
        # 180 degrees over 0.525 seconds means ~342.857 degrees per second
        self.rotation_speed = 180.0 / 0.525 

    def start_rotation(self):
        # Only start a new rotation if it finished the last one
        if self.current_angle == self.target_angle:
            self.target_angle += 180.0

    def update(self, dt):
        if self.current_angle < self.target_angle:
            # Negative because Geometry Dash cubes rotate clockwise
            self.current_angle += self.rotation_speed * dt
            if self.current_angle > self.target_angle:
                self.current_angle = self.target_angle
                

    def get_rotated_surface_and_rect(self, base_x, base_y):
        # We rotate negative current_angle to spin clockwise
        rotated_image = pygame.transform.rotate(self.original_image, -self.current_angle)
        # Snap the center of the expanded bounding box to the cube's resting spot
        default_rect = self.original_image.get_rect(topleft=(base_x, base_y))
        rotated_rect = rotated_image.get_rect(center=default_rect.center)
        return rotated_image, rotated_rect
