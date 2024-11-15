import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 1200, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Zoro's Adventure - A One Piece Story")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define different font sizes for headings and regular text
title_font = pygame.font.Font(None, 60)  # Larger for headings
regular_font = pygame.font.Font(None, 40)  # Smaller for regular text
zoro_font = pygame.font.Font(None, 50)


background_1= pygame.image.load("background_1.png").convert_alpha()
background_2 = pygame.image.load("background_2.png").convert_alpha()
background_3 = pygame.image.load("background_3.webp").convert_alpha()
background_4 = pygame.image.load("background_4.png").convert_alpha()


# Resize background images to fit the screen
forest_background = pygame.transform.scale(background_1, (WIDTH, HEIGHT))
village_background = pygame.transform.scale(background_2, (WIDTH, HEIGHT))
mihawk_background = pygame.transform.scale(background_3, (WIDTH, HEIGHT))
rest_background = pygame.transform.scale(background_4, (WIDTH, HEIGHT))
intro_background = pygame.transform.scale( pygame.image.load("background_0.png").convert_alpha(), (WIDTH, HEIGHT))

def draw_text(text, x, y, font=regular_font):
    """Draw text on the screen with specified font size."""
    rendered_text = font.render(text, True, WHITE)
    screen.blit(rendered_text, (x, y))

def intro():
    screen.blit(intro_background, (0, 0))  # Set the background image for intro
    draw_text("Zoro is a strong swordsman who wants to the strongest swordsman in the world", 100, 100, zoro_font)
    draw_text("He was famous throughout the land as Pirate Hunter Zoro.", 100, 200, zoro_font)
    draw_text("Press 1 to start Zoro's journey", 100, 400)
    draw_text("Press 2 to exit", 100, 500)
    pygame.display.flip()

def game_loop():
    screen.blit(forest_background, (0, 0))  # Set the background image for the game crossroads
    draw_text("Zoro finds himself lost (again) in an unfamiliar land.", 100, 100)
    draw_text("1. Head towards the mysterious forest.", 100, 200)
    draw_text("2. Walk towards a nearby village for information.", 100, 300)
    draw_text("3. Sit down and rest for a while.", 100, 400)
    pygame.display.flip()

def forest_scene():
    screen.blit(forest_background, (0, 0))  # Set the background image for forest
    draw_text("Zoro ventures deep into the forest, hearing strange noises.", 100, 100)
    draw_text("Suddenly, a map falls from a tree, leading to hidden treasure.", 100, 200)
    draw_text("1. Follow the map to the treasure.", 100, 300)
    draw_text("2. Ignore the map and keep going.", 100, 400)
    draw_text("Press ESC to return to the crossroads.", 100, 500)
    pygame.display.flip()

def treasure_scene():
    screen.fill(BLACK)
    draw_text("Zoro follows the map to a hidden cave.", 100, 100)
    draw_text("Inside, he finds the legendary treasure of Wano!", 100, 200)
    draw_text("But suddenly, a powerful enemy appears to guard it!", 100, 300)
    draw_text("Press ESC to return to the crossroads.", 100, 400)
    pygame.display.flip()

def village_scene():
    screen.blit(village_background, (0, 0))  # Set the background image for the village
    draw_text("Zoro arrives at the village and finds a tavern.", 100, 100)
    draw_text("Inside, he meets Luffy and Sanji who offer him help.", 100, 200)
    draw_text("1. Accept their help and travel to fight Mihawk.", 100, 300)
    draw_text("2. Refuse their help and continue solo.", 100, 400)
    draw_text("Press ESC to return to the crossroads.", 100, 500)
    pygame.display.flip()

def rest_scene():
    screen.blit(rest_background, (0, 0))  # Set the background image for rest
    draw_text("Zoro decides to take a nap under a tree.", 100, 100)
    draw_text("He dreams of becoming the world's greatest swordsman.", 100, 150)
    draw_text("Press ESC to return to the crossroads.", 100, 200)
    pygame.display.flip()

def mihawk_battle_scene():
    screen.blit(mihawk_background, (0, 0))  # Set the background image for Mihawk battle
    draw_text("Zoro faces Dracule Mihawk, the world's greatest swordsman!", 100, 100)
    draw_text("This is the ultimate test for Zoro.", 100, 200)
    draw_text("1. Attack with all your strength.", 100, 300)
    draw_text("2. Defend and look for an opening.", 100, 400)
    pygame.display.flip()

def mihawk_outcome_scene(choice):
    screen.blit(mihawk_background, (0, 0))  # Set the background image for Mihawk outcome
    if choice == "attack":
        draw_text("Zoro's attack is strong, but Mihawk easily counters.", 100, 100)
        draw_text("Zoro is knocked down, but not defeated. He vows to train harder.", 100, 150)
    elif choice == "defend":
        draw_text("Zoro defends and finds an opening.", 100, 100)
        draw_text("Though he doesn't win, Mihawk respects his growth.", 100, 150)
    draw_text("Zoro promises to surpass Mihawk one day.", 100, 200)
    pygame.display.flip()

def handle_input(current_scene):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "game", None  # Return to the game loop
            if current_scene == "intro":
                if event.key == pygame.K_1:
                    return "game", None  # Move to game scene
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()
            elif current_scene == "game":
                if event.key == pygame.K_1:
                    return "forest", None
                elif event.key == pygame.K_2:
                    return "village", None
                elif event.key == pygame.K_3:
                    return "rest", None
            elif current_scene == "forest":
                if event.key == pygame.K_1:
                    return "treasure", None
                elif event.key == pygame.K_2:
                    return "game", None  # Return to crossroads
            elif current_scene == "village":
                if event.key == pygame.K_1:
                    return "mihawk_battle", None
                elif event.key == pygame.K_2:
                    return "game", None  # Continue solo
            elif current_scene == "mihawk_battle":
                if event.key == pygame.K_1:
                    return "mihawk_outcome", "attack"
                elif event.key == pygame.K_2:
                    return "mihawk_outcome", "defend"
    return current_scene, None  # No change if no valid input

# Main game loop
current_scene = "intro"
battle_choice = None
while True:
    if current_scene == "intro":
        intro()
    elif current_scene == "game":
        game_loop()
    elif current_scene == "forest":
        forest_scene()
    elif current_scene == "treasure":
        treasure_scene()
    elif current_scene == "village":
        village_scene()
    elif current_scene == "rest":
        rest_scene()
    elif current_scene == "mihawk_battle":
        mihawk_battle_scene()
    elif current_scene == "mihawk_outcome":
        mihawk_outcome_scene(battle_choice)
    current_scene, battle_choice = handle_input(current_scene)
    pygame.display.update()
