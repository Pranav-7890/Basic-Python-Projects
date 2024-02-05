 
# The above code is a simple game called "Space Dodge" where the player controls a rectangle and tries
# to avoid falling stars for as long as possible.
    
# :param player: The `player` parameter is a `pygame.Rect` object that represents the player's
# character in the game. It is used to store the position and size of the player's character on the
# game window
# :param elapsed_time: The `elapsed_time` parameter represents the time in seconds that has passed
# since the game started. It is used to display the current time on the screen
# :param stars: The `stars` parameter is a list that stores the rectangles representing the stars in
# the game. Each star is represented by a `pygame.Rect` object, which is a rectangle with a position
# (x, y) and dimensions (width, height)

 
import pygame
import time
import random
pygame.font.init()

WIDTH,HEIGHT=1000,800
Win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Dodge")


BG = pygame.transform.scale(pygame.image.load("66315.jpg"), (WIDTH,HEIGHT))

P_WIDTH = 40
P_HEIGHT = 60

PLAYER_VELOCITY = 20

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 20)

def draw(player, elapsed_time, stars):
    Win.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s" , 1, "white")
    Win.blit(time_text, (10,10)) 

    pygame.draw.rect(Win,"red", player)

    for star in stars:
        pygame.draw.rect(Win,"White", star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT-P_HEIGHT,P_WIDTH,P_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count >star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH-STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >=0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("YOU LOST!",1,"red")
            Win.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    pygame.quit()

if __name__ == "__main__":
    main()
