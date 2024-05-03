import os
import random
import pygame

# Initialize Pygame
pygame.init()

# Set display dimensions
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Get the path to the directory containing the GIFs
current_directory = os.path.dirname(__file__)
gif_directory = os.path.join(current_directory, "gifs")

# List of medical terms and corresponding GIFs
medical_terms_and_gifs = {
    "neurology": "neurology.gif",
    "cardiology": "cardiology.gif",
    "orthopedics": "orthopedics.gif",
    "ophthalmology": "ophthalmology.gif",
    "pediatrics": "pediatrics.gif",
}

# Function to choose a random medical term
def choose_word():
    return random.choice(list(medical_terms_and_gifs.keys()))

# Function to display a GIF associated with a medical term
def display_gif(word):
    gif_file = medical_terms_and_gifs.get(word)
    if gif_file:
        # Construct the full path to the GIF
        gif_path = os.path.join(gif_directory, gif_file)
        # Load GIF image
        gif = pygame.image.load(gif_path)
        return gif
    else:
        print("No GIF found for the medical term:", word)
        return None

# Main game loop
def main():
    word = choose_word()
    print("Medical Term:", word)
    gif = display_gif(word)
    if gif:
        # Set up the display
        game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        game_display.fill(WHITE)
        # Set position of GIF
        gif_rect = gif.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        # Display GIF
        game_display.blit(gif, gif_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # Display GIF for 3 seconds
    pygame.quit()

if __name__ == "__main__":
    main()
