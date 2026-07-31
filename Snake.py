import pygame
import random

pygame.init()


# config
WINDOW_SIZE = WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
SPEED = 10

# colour
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(title="Snake")
pygame.display.set_icon(pygame.image.load("images/icon.png"))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans", 25)


def random_food_position(snake):
    while True:
        pos = random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT)
        if pos not in snake: # if falls within the bounds of the snake, find new position
            return pos

def draw_cell(pos, colour):
    cell = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE) # creates cell
    pygame.draw.rect(screen, colour, cell) # draws cells

def reset_game():
    snake = [(10, 10), (9, 10), (8, 10)] # snake is 3 cells long at start
    direction = (1, 0) # facing forwards
    food = random_food_position(snake)
    return snake, direction, food, 0, False # resets snake, starting direction, food, score, and 'game_over'


def main():
    snake, direction, food, score, game_over = reset_game() # reset everything upon new game
    running = True # start game loop

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT: # quit game when asked / stop game loop
                running = False

            elif event.type == pygame.KEYDOWN: # key-pressing options

                if game_over:
                    if event.key == pygame.K_SPACE: # if game over, press SPACE to restart
                        snake, direction, food, score, game_over = reset_game()
                    continue # continue running game loop

                if event.key == pygame.K_UP and direction != (0, 1): # unless facing down
                    direction = (0, -1) # face up
                elif event.key == pygame.K_DOWN and direction != (0, -1): # unless facing up
                    direction = (0, 1) # face down
                elif event.key == pygame.K_LEFT and direction != (1, 0): # unless facing right
                    direction = (-1, 0) # face left
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): # unless facing left
                    direction = (1, 0) # face right

        if not game_over: # while in-game
            head_x, head_y = snake[0] # head is at the front of the snake's "list" of cells
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy) # head is updated with direction changes

            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or # snake hits game boundary
                    new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or # snake hits game boundary
                    new_head in snake): # snake hits itself
                game_over = True # game over conditions
            else:
                snake.insert(0, new_head) # update head
                if new_head == food: # snake finds food
                    score += 1
                    food = random_food_position(snake)
                else:
                    snake.pop() # keeps snake the same length ('pops' out last tail cell as new head is created)

        # draw
        screen.fill(BLACK) # background is black. Replaces the screen every frame.

        for segment in snake:
            draw_cell(segment, GREEN) # snake is green
        draw_cell(food, RED) # food is red

        score_surface = font.render(f"Score: {score}", True, WHITE) # creates text
        screen.blit(score_surface, (10, 10)) # draws the text

        if game_over:
            msg = font.render("Game Over - press SPACE to restart", True, WHITE)
            msg_pos = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(msg, msg_pos) # draw message in the center of the screen

        pygame.display.flip() # show drawings
        clock.tick(SPEED) # speed of snake


    pygame.quit()


if __name__ == "__main__":
    main()