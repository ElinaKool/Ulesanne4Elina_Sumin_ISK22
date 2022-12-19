import pygame, sys  # pygame ja sys mooduli importimine programmi

pygame.init()

# ekraani seaded
screenX = 640  # ekraani pikkus, mööda x-telge loomine 640 pikslit
screenY = 480  # ekraani pikkus, mööda y-telge, loomine 480 pikslit

screen = pygame.display.set_mode([screenX, screenY])  # Paprameetrite ScreenX ja ScreenY kasutamine, millele on väärtus juba varasemalt määratud
pygame.display.set_caption("Ulesanne4")  # programmi aknale töönime lisamine

clock = pygame.time.Clock()  # kella mooduli lisamine mängu

# Lisame taustapildi
bg = pygame.image.load("bg_rally.jpg")  # taustapildi lisamine mängu

# Punase auto lisamine ja asukoha määramine
red_car = pygame.image.load("f1_red.png")  # punase auto pildi lisamine mängu
red_car = pygame.transform.scale(red_car, [50, 100])  # punasele autole mõõtmete määramine
red_car = pygame.transform.rotate(red_car, 180)  # punase auto keeramine 180 kraadi

score = 0  # algne skoor on võrdne 0 punktiga

font = pygame.font.Font(pygame.font.match_font('Fantasy'), 30)  # Fonti määramine
text = font.render("Skoor: " + str(score), True,
                   [255, 255, 255])  # Teksti "Skoor" tekitamine, värvi ja numbrite asukoha määramine

# Siniste autode lisamine
blue_car = pygame.image.load("f1_blue.png")  # siniseauto pildi lisamine mängu
blue_car = pygame.transform.scale(blue_car, [50, 75])  # sinisele autole mõõtmete määramine

# siniste autode keeramine 180 kraadi
blue_car1 = pygame.transform.rotate(blue_car, 180)
blue_car2 = pygame.transform.rotate(blue_car, 180)
blue_car3 = pygame.transform.rotate(blue_car, 180)

# Siniste autode kiirus ja asukoht
posX1, posY1 = 180, 100
posX2, posY2 = 400, 200
posX3, posY3 = 300, 75

gameover = False  # Mängu alustades, mängulõppevus ei ole tõene
while not gameover:  # Seni kuni mäng ei ole läbi

    # fps
    clock.tick(120)  # uuendatakse ekraani 120 korda sekundis

    screen.blit(bg, [0, 0])
    # Siniste autode kiiruste määramine
    posY1 += 2  # vasaku, sinise, auto kiirus
    posY2 += 4  # parema, sinise, auto kiirus
    posY3 += 0.5  # Keskmise, sinise, auto kiirus

    # Autode algus kordinaadi määramine
    screen.blit(red_car, [300, 380])  # Punase auto kordinaatide määramine
    screen.blit(blue_car1, (
    posX1, posY1))  # vasakule, sinisele, autole määratakse algkordinaadid, mis on juba üleval muutujatena kirjas
    screen.blit(blue_car2, (posX2, posY2))  # parema raja, sinine autole määratud kordinaadid.
    screen.blit(blue_car3, (posX3, posY3))  # keskmisele autole määratakse algkordinaadid

    screen.blit(text, [525, 20])  # skoori kuvamine
    text = font.render("Skoor: " + str(score), True, [255, 255, 255])  # skoori teksti parameetrid.

    # Määrame, et kui auto jõuab alla serva, siis auto kordinaadid muutuvad tagasi algkordinaatiteks ja autod hakkavad samat teekonda uuesti läbima
    if posY1 == 480:  # Kui auto jõuab alla
        posY1 = 0  # siis määratakse, et auto läheb tagasi ülesse
        score += 1  # ning skoorile/tulemusele lisatakse 1 punkt juurde

    if posY2 == 480:  # kui auto jõuab alla
        posY2 = 0  # siis määratakse, et auto läheb uuesti tagasi alguskordinaadile
        score += 1  # ja skoorile lisatakse 1 punkt juurde

    if posY3 == 320:  # kui keskmine, sinine, auto jüuab alla
        posY3 = 50  # samale kordinaagi lähedusse, mis on punane
        gameover = True  # ehk siis kui sinine auto "puudutab" punast autot, on mäng läbi

    # Mängu sulgemine ristist
    # events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()

pygame.quit()