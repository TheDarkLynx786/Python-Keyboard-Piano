import pygame
import lists

pygame.init()
pygame.mixer.set_num_channels(50)


font = pygame.font.Font('assets/PlayfairDisplaySC-Regular.otf', 48)
medFont = pygame.font.Font('assets/PlayfairDisplaySC-Regular.otf', 28)
smlFont = pygame.font.Font('assets/PlayfairDisplaySC-Regular.otf', 16)
tnyfont = pygame.font.Font('assets/PlayfairDisplaySC-Regular.otf', 10)


fps = 60
timer = pygame.time.Clock()
width = 52*35
height = 400
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Murtaza Haque - Python Keyboard Piano")
activeWhites = []
activeBlacks = []


def drawPiano(whites, blacks):
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i * 35, height - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, height - 300, 35, 300], 2, 2)
        key_label = smlFont.render(lists.white_notes[i], True, 'black')
        screen.blit(key_label, (i * 35 + 3, height - 20))
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = tnyfont.render(lists.black_labels[i], True, 'white')
        screen.blit(key_label, (25 + (i * 35) + (skip_count * 35), height - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * 35, height - 100, 35, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks

run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    whiteKeys, blackKeys, activeBlacks, activeWhites = drawPiano(activeWhites, activeBlacks)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()