import pygame
import sys

def check_events(on, q, sketcher, sett):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            on = 1

    while q.isEmpty() == False:
        v = q.front()
        if on == 0 : #Apagado
            break
        on = 0
        q.pop()
        sketcher.add_boar(v)
        sett.add(v)
        xd = v.gen_boar()
        for e in xd:
            if e not in sett:
                q.push(e)

def update_screen(settings, screen, sketcher):
    screen.fill(settings.bg_color)
    sketcher.draw()
    pygame.display.flip()
