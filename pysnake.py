import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game variables
snake_position = [250, 250]
snake_body = [[250, 250], [240, 250], [230, 250]]
food_position = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                 random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
food_spawned = True
direction = "RIGHT"
change_to = direction
score = 0

# Set up the game fonts
font = pygame.font.Font('freesansbold.ttf', 25)

# Set up the game over message
def game_over():
    over_font = pygame.font.Font('freesansbold.ttf', 50)
    over_text = over_font.render("GAME OVER", True, RED)
    window.blit(over_text, (WINDOW_WIDTH//2 - over_text.get_width()//2,
                            WINDOW_HEIGHT//2 - over_text.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(2000)

    # Restart the game
    global snake_position, snake_body, food_position, food_spawned, direction, change_to, score
    snake_position = [250, 250]
    snake_body = [[250, 250], [240, 250], [230, 250]]
    food_position = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                     random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
    food_spawned = True
    direction = "RIGHT"
    change_to = direction
    score = 0

# Set up the game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"

    # Change the snake direction if needed
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # Move the snake
    if direction == "RIGHT":
        snake_position[0] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10

    # Check if the snake hit the boundary
    if snake_position[0] < 0 or snake_position[0] > WINDOW_WIDTH-10 or snake_position[1] < 0 or snake_position[1] > WINDOW_HEIGHT-10:
        game_over()

    # Check if the snake hit itself
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Check if the snake ate the food
    if snake_position == food_position:
        food_spawned = False
        score += 10

    # Spawn new food if needed
    if not food_spawned:
        food_position = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                         random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
        food_spawned = True

    # Move the snake body
    snake_body.insert(0, list(snake_position))
    if snake_position == food_position:
        food_spawned = False
    else:
        snake_body.pop()

    # Set up the game window
    window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Set the game speed
    clock.tick(40)

# Quit Pygame
pygame.quit()

