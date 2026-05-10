from pygame import *

win_w = 700
win_h = 500
window = display.set_mode((win_w,win_h))
display.set_caption('Сны при температуре 67℃')
background = transform.scale(image.load('images.jpg'),(win_w,win_h))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_w,player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def upd_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
    def upd_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
racket1 = Player('67.png',20,20,5,100,200)
racket2 = Player('69.png',600,20,5,100,200)
ball = GameSprite('balls.png',50,50,2,75,75)
speed_x = 3
speed_y = 3
game = True
clock = time.Clock()
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('JEDI LOSE', True,(180,0,0))
lose2 = font1.render('SITH LOSE', True,(180,0,0))
finish = False
while game:
    window.blit(background,(0,0))

    if finish != True:
        window.blit(background, (0, 0))
        racket1.upd_l()
        racket1.reset()
        racket2.upd_r()
        racket2.reset()
        ball.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    if game == True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_h-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *=-1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(200,200))
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2,(200,200))
    display.update()
    clock.tick(200)