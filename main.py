from pygame import *

win_w = 700
win_h = 500
window = display.set_mode((win_w,win_h))
display.set_caption('Сны при температуре 67℃')
background = transform.scale(image.load('images.jpg'),(win_w,win_h))

game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()