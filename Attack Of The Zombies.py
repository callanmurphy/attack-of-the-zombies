#Callan Murphy
'''NOTE: Spawn killing is a major issue which still needs to be fixed'''
#Notes of improvements to make...
#fix spawn killing
#fix zombie hit box
#pick up new bullets
#zombies spawn better (maybe based on total bullets ever shot)
#remove noShooting function by allowing a single shot to be fired at game initiation

import pygame, random, time #imports pygame and random modules
pygame.init() #initializes pygame with all its included components
pygame.font.init() #https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.mixer.init() #https://www.pygame.org/docs/ref/mixer.html

def startUp():
    '''
    This function is ran immediately after importing and initializing pygame.
    It defines all of the basic variables that need to be established at the
    beginning of the program for later use. Finally, the function calls the
    next function to be ran as this one ends.
    '''
    #pygame.mixer.music.load("Game Song 1.0.mp3") 
    #pygame.mixer.music.play(10,0.0)
    #Music ^ is currently not working (getting an error)
    teal = 32,178,170 #colour code for teal used to draw background colour
    score = 0 #number of player's zombie kills

    playerImage = pygame.image.load("PlayerRight.gif")
    bulletImage = pygame.image.load("Bullet.gif")
    zombieImage = pygame.image.load("Zombie.gif")
    healthImage = [pygame.image.load("Health0.gif"), pygame.image.load("Health1.gif"), pygame.image.load("Health2.gif"), pygame.image.load("Health3.gif"), pygame.image.load("Health4.gif"), pygame.image.load("Health5.gif")]
    health = healthImage[5].get_rect()
    player = playerImage.get_rect()
    # ^^ creates a rectangle around the image
    #https://www.pygame.org/docs/tut/PygameIntro.html
    player.centerx = 640 #spawn x location for the player
    player.centery = 352 #spawn y location for the player
    playerDirection = "Right"
    playerHealth = 5
    totalBullets = 0
    bulletsRemaining = 15
    font1 = pygame.font.SysFont('Calibri', 30)
    font2 = pygame.font.SysFont('Times New Roman', 200)
    font3 = pygame.font.SysFont('Calibri', 30)
    exitText = font3.render('Press "enter" to exit', False, (200, 0, 0))
    healthText = font1.render('Health', False, (0, 0, 0))
    scoreText = font1.render('Score: ' + str(score), False, (0, 0, 0))
    bulletsText = font1.render('Bullets Remaining: ' + str(bulletsRemaining), False, (0, 0, 0))
    gameOverText = font1.render('GAME OVER', False, (0, 0, 0))

    health.centerx = 120
    health.centery = 50
    endgame = 0 #allows game to end once dead
    enoughBullets = True

    exitNestedLoop = 0 #variable to exit the nested loop used later
    countBullets = 0
    clock = pygame.time.Clock()

    count = -1 #counter to keep track of bullets, set to -1 so that it begins at 0 (because of 'count += 1' at start of bullet function)
    bullets = [] #list to be used later for containing all bullets on-screen
    zombies = []
    bulletSpeed = [] #list to be used later for containing speeds of all bullets on-screen
    menu(teal, font1, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)

def menu(teal, font1, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText):
    '''
    Main menu function to display the menu upon beginnning the game. Allows
    the player to navigate and choose either 'controls' or 'play game',
    running the corresponding function to display the menu item.
    '''
    menuSelectImage = pygame.image.load("MenuSelect.gif")
    select = menuSelectImage.get_rect()
    menuScreen = pygame.display.set_mode((1280, 705))
    font4 = pygame.font.SysFont('Calibri', 70)
    font5 = pygame.font.SysFont('Calibri', 45)
    menuText = font4.render('ATTACK OF THE ZOMBIES', False, (200, 0, 0))
    menuOption1Text = font5.render('Play Game', False, (0, 0, 0))
    menuOption2Text = font5.render('Controls', False, (0, 0, 0))
    instructionText = font1.render("Use the 'w' and 's' keys to scroll through the menu and 'enter' to select", False, (200,0,0))
    closeText = font1.render("Press 'ESC' to exit", False, (200,0,0))
    select.centerx = 485
    select.centery = 325
    option1 = True
    close = 0 #used to exit main loop
    while True:
        for event in pygame.event.get():     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit() #closes window
                    break
                if event.key == pygame.K_w:
                    option1 = True
                    select.centerx = 485
                    select.centery = 325
                if event.key == pygame.K_s:
                    option1 = False
                    select.centery = 425
                if event.key == pygame.K_RETURN:
                    if option1 == True:
                        close = 1
                        pygame.display.quit() #closes window
                        noShooting(teal, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)      
                        break
                    elif option1 == False:
                        close = 1
                        pygame.display.quit() #closes window
                        controls(teal, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)
                        break
        if close == 1:
            break
        else:
            menuScreen.fill(teal)
            menuScreen.blit(menuText,(290,130))
            menuScreen.blit(menuOption1Text,(540,300))
            menuScreen.blit(menuOption2Text,(540,400))
            menuScreen.blit(instructionText,(15,610))
            menuScreen.blit(closeText,(15,650))
            menuScreen.blit(menuSelectImage, select)
            pygame.display.flip() #allows colour/other graphics to be displayed

def controls(teal, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText):
    '''
    Displays a screen to show the controls for the game to the user. The user
    can return to the main menu at any time at which the menu function is
    called.
    '''
    controlsScreen = pygame.display.set_mode((1280, 705))
    wasdImage = pygame.image.load("WASD.gif")
    wasd = wasdImage.get_rect()
    spacebarImage = pygame.image.load("Spacebar.gif")
    spacebar = spacebarImage.get_rect()
    wasd.centerx = 350
    wasd.centery = 300
    spacebar.centerx = 900
    spacebar.centery = 261
    close = 0 #used to exit main loop
    font6 = pygame.font.SysFont('Calibri', 35)
    upText = font6.render('Move Up', False, (255, 255, 255))
    downText = font6.render('Move Down', False, (255, 255, 255))
    rightText = font6.render('Move Right', False, (255, 255, 255))
    leftText = font6.render('Move Left', False, (255, 255, 255))
    shootText = font6.render('Shoot', False, (255, 255, 255))
    exitScreenText = font6.render("Press 'enter' to return to the menu", False, (200, 0, 0))
    controlsScreen.fill(teal)
    controlsScreen.blit(upText,(420, 60))
    controlsScreen.blit(downText,(250, 500))
    controlsScreen.blit(rightText,(530, 470))
    controlsScreen.blit(leftText,(20, 487))
    controlsScreen.blit(shootText,(1000, 120))
    controlsScreen.blit(exitScreenText,(400, 610))
    controlsScreen.blit(wasdImage, wasd)
    controlsScreen.blit(spacebarImage, spacebar)
    pygame.display.flip() #allows colour/other graphics to be displayed
    while True:
        for event in pygame.event.get():     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    close = 1
                    pygame.display.quit() #closes window
                    menu(teal, font1, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)
                    break
        if close == 1:
            break
    
def noShooting(teal, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText):
    '''
    This function begins the gameplay, spawning 3 zombies and allowing the
    player to move around the screen. I am hoping to remove this function
    once I am able to combine it with the game function above. For now, it
    allows the player to move until the spacebar is pressed, at which time
    it calls the game function to be used for the remainder of the gameplay.
    '''
    screen = pygame.display.set_mode((1280, 705))
    exitSpawnNestedLoop = 0
    for i in range(0,3):
        zombies.append(zombieImage.get_rect()) #create a new zombie
        while True:
            randomSpawn= random.randint(1,4) #random integer to randomize zombie spawn location
            if randomSpawn == 1: #further randomization of zombie spawn location
                zombies[len(zombies)-1].centerx = player.centerx + random.randint (-500, -100)
            elif randomSpawn == 2: #further randomization of zombie spawn location
                zombies[len(zombies)-1].centerx = player.centerx + random.randint (100, 500)
            elif randomSpawn == 3: #further randomization of zombie spawn location
                zombies[len(zombies)-1].centery = player.centery + random.randint (-500, -100)
            elif randomSpawn == 4: #further randomization of zombie spawn location
                zombies[len(zombies)-1].centery = player.centery + random.randint (100, 500)
            if zombies[len(zombies)-1].centery >= 705 or zombies[len(zombies)-1].centery <= 0: #prevents zombie from spawning off of the screen (height)
                pass
            elif zombies[len(zombies)-1].centerx >= 1280 or zombies[len(zombies)-1].centerx <= 0: #prevents zombie from spawning off of the screen (width)
                pass
            elif zombies[len(zombies)-1].centerx > -100 and zombies[len(zombies)-1].centerx < 100: #ensures both an x and y coordinate are selected for zombie spawn
                pass
            elif zombies[len(zombies)-1].centery > -100 and zombies[len(zombies)-1].centery < 100: #ensures both an x and y coordinate are selected for zombie spawn
                pass
            else: #if there are no issues with the zombie spawn, the loop is broken to allow the zombie to spawn
                break
    while True:
        for event in pygame.event.get():     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.display.quit() #closes window
                    exitNestedLoop = 1
                    break
                if event.key == pygame.K_SPACE:
                    game(screen, playerDirection, player, bullets, teal, playerImage, bulletImage, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: player.centery -= 3
        if pressed[pygame.K_s]: player.centery += 3
        if pressed[pygame.K_a]:
            player.centerx -= 3
            playerImage = pygame.image.load("PlayerLeft.gif")
            playerDirection = "Left"
        if pressed[pygame.K_d]:
            player.centerx += 3
            playerImage = pygame.image.load("PlayerRight.gif")
            playerDirection = "Right"
        
        #player movement done with help from "nullege.com"
        #http://nullege.com/codes/search/pygame.key.get_pressed
            
        if player.centerx <= 50:
            player.centerx = 50
        if player.centerx >= 1230:
            player.centerx = 1230
        if player.centery <= 50:
            player.centery = 50
        if player.centery >= 655:
            player.centery = 655

        #code above prevents the player from going off of the screen

        zombieMove = random.randint (1,4) #helps to randomize zombie movements
        if zombieMove == 1: #only has a 1/4 chance of running
            numOfZombiesMoving = random.randint(0, len(zombies))
            for i in range(0, numOfZombiesMoving):
                zombieMoveChoice = random.randint(1,4)
                zombieMoveLengthChoice = random.randint (10, 13)
                if zombieMoveChoice == 1:
                    for x in range (0, zombieMoveLengthChoice):
                        zombies[i].centerx += 2
                elif zombieMoveChoice == 2:
                    for x in range (0, zombieMoveLengthChoice):
                        zombies[i].centerx -= 2
                elif zombieMoveChoice == 3:
                    for x in range (0, zombieMoveLengthChoice):
                        zombies[i].centery += 2
                elif zombieMoveChoice == 4:
                    for x in range (0, zombieMoveLengthChoice):
                       zombies[i].centery -= 2
                if zombies[i].centerx <= 50:
                    zombies[i].centerx = 50
                if zombies[i].centerx >= 1230:
                    zombies[i].centerx = 1230
                if zombies[i].centery <= 50:
                    zombies[i].centery = 50
                if zombies[i].centery >= 655:
                    zombies[i].centery = 655

        #code above allows zombies to move randomly and prevents them from going off of the screen

        if exitNestedLoop == 1: #exits the while loop
            break

        for i in range(0, len(zombies)):
            if player.colliderect(zombies[i]):
                if playerHealth >= 2:
                    playerHealth -= 1
                    health = healthImage[playerHealth].get_rect()
                else:
                    exitBulletNestedLoop = 1
                    endgame = 1
                    break
                while True:
                    player.centerx = random.randint(30, 1200)
                    player.centery = random. randint(30, 650)
                    for x in range(0, len(zombies)):
                        if zombies[x].centerx >= player.centerx - 300 and zombies[x].centerx <= player.centerx + 300:
                            pass
                        elif zombies[x].centery >= player.centery - 300 and zombies[x].centery <= player.centery + 300:
                            pass
                        else:
                            exitSpawnNestedLoop = 1
                            break
                    if exitSpawnNestedLoop == 1:
                        break
                health.centerx = 120 #health bar coordinates are reset to prevent glitch of the health bar moving
                health.centery = 50 #health bar coordinates are reset to prevent glitch of the health bar moving
            screen.blit(zombieImage, zombies[i]) #draws the zombies onscreen


        clock.tick(60)

        screen.fill(teal) #fills background colour
        screen.blit(playerImage, player) #draws player on screen
        screen.blit(healthImage[playerHealth], health)
        screen.blit(healthText,(50,0))
        screen.blit(zombieImage, zombies[0])
        screen.blit(zombieImage, zombies[1])
        screen.blit(zombieImage, zombies[2])
        screen.blit(scoreText,(50,70))
        screen.blit(bulletsText,(50,110))
        pygame.display.flip() #allows colour/other graphics to be displayed

def game(screen, playerDirection, player, bullets, teal, playerImage, bulletImage, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText):
    '''
    This is the main game function which contains the bulk of the code to run
    the game. It is ran for the remainder of the game after the other functions.
    It allows the player to move and shoot, zombies to spawn and be killed,
    and score and bullet counters to operate. It also ends the game once
    the user loses all of their health.
    '''
    newBullet = 0 #allows the bullet loop to be exited later to add a new bullet
    exitBulletNestedLoop = 0
    exitSpawnNestedLoop = 0
    count += 1 #used to select index of bullet list
    if enoughBullets == True: #checks if the player is out of bullets
        bullets.append(bulletImage.get_rect()) #adds a new bullet to the list
        totalBullets += 1
        bulletsRemaining = 15 - totalBullets
        bulletsText = font1.render('Bullets Remaining: ' + str(bulletsRemaining), False, (0, 0, 0))
        countBullets += 1
        if playerDirection == "Left":
            bulletSpeed.append([-10, 0])
            positionx = -48
        elif playerDirection == "Right":
            bulletSpeed.append([10, 0])
            positionx = 30
        bullets[count].centerx = player.centerx + positionx
        bullets[count].centery = player.centery - 11
    while True: #main game loop to continuously check for a variety of game events
        if bulletsRemaining == 0: #checks if the player is out of bullets
            enoughBullets = False #updates a varible to notify that no bullets exist (variable is being checked for later to prevent the player from shooting if no bullets remain)
        if len(bullets) == 0: #checks if all bullets have finished being fired
                if enoughBullets == False: #checks if the player is out of bullets
                    exitBulletNestedLoop = 1 #allows the main game loop to be exited
                    endgame = 1 #allows the game to be ended
                    break #allows the loop to exit
        for event in pygame.event.get(): #checks for game events
            if event.type == pygame.KEYDOWN: #checks if a key has been pressed
                if event.key == pygame.K_SPACE: #checks if the spacebar has been pressed
                    if enoughBullets == True: #checks if bullets remain
                         newBullet = 1 #lets the later code know that a new bullet must be created
                         exitBulletNestedLoop = 1 #allows the bullet loop to be exited later to add a new bullet
                         break #exits the loop to create a new bullet
                if event.key == pygame.K_ESCAPE: #checks if the return (enter) key has been pressed
                    pygame.display.quit() #closes window
                    exitNestedLoop = 1 #used to later exit the main game loop
                    break #exits the current loop so that game can be quit
        if exitBulletNestedLoop == 1: #checks if previous code wishes to exit game loop
            break #exits game loop
        
        pressed = pygame.key.get_pressed() #checks if a key has been pressed. Different way of checking than above since this method will recognize key holds (not just presses) which is better for player movement
        if pressed[pygame.K_w]: player.centery -= 4 #moves the player up by 4 units when 'w' key is pressed
        if pressed[pygame.K_s]: player.centery += 4 #moves the player down by 4 units when 's' key is pressed
        if pressed[pygame.K_a]:
            player.centerx -= 4 #moves the player left by 4 units when 'a' key is pressed
            playerImage = pygame.image.load("PlayerLeft.gif") #changes the player image to be facing left
            playerDirection = "Left" #used to notify the rest of the program that the player is facing left (for bullet firing)
        if pressed[pygame.K_d]:
            player.centerx += 4 #moves the player right by 4 units when 'd' key is pressed
            playerImage = pygame.image.load("PlayerRight.gif") #changes the player image to be facing right
            playerDirection = "Right" #used to notify the rest of the program that the player is facing right (for bullet firing)

        
        #player movement done with help from "nullege.com"
        #http://nullege.com/codes/search/pygame.key.get_pressed
            
        if player.centerx <= 50:
            player.centerx = 50
        if player.centerx >= 1230:
            player.centerx = 1230
        if player.centery <= 50:
            player.centery = 50
        if player.centery >= 655:
            player.centery = 655

        #above code prevents the player from travelling off the screen
            
        screen.fill(teal)
        screen.blit(playerImage, player)
        screen.blit(healthImage[playerHealth], health)
        screen.blit(healthText,(50,0))
        screen.blit(scoreText,(50,70))
        screen.blit(bulletsText,(50,110))

        #draws the graphics onto the screen
        
        killZombies = []
        for i in range (0, len(bullets)): #loop to perform actions on each existing bullet
            bullets[i] = bullets[i].move(bulletSpeed[i]) #bullet is moved
            screen.blit(bulletImage, bullets[i]) #bullet is drawn
            for x in range (0, len(zombies)):
                if bullets[i].colliderect(zombies[x]):
                    if x not in killZombies:
                        killZombies.append(x)
        for i in killZombies:
            del zombies[i]
            score += 1
        scoreText = font1.render('Score: ' + str(score), False, (0, 0, 0))
        pygame.display.flip() #display is updated
        for i in range (0, len(bullets)): #same loop statement but kept seperate to allow display update in between loops
            if bullets[i].centerx <= 0 or bullets[i].centerx >= 1280: #checks if bullet is off of the screen
                del bullets[i] #removes the bullet
                del bulletSpeed[i] #removes the corresponding bullet speed
                count -= 1 #the new list space can be re-assigned
                break
        if countBullets >= 1:
            for i in range(0,3):
                zombies.append(zombieImage.get_rect()) #create a new zombie
                while True:
                    randomSpawn= random.randint(1,4) #random integer to randomize zombie spawn location
                    if randomSpawn == 1: #further randomization of zombie spawn location
                        zombies[len(zombies)-1].centerx = player.centerx + random.randint (-500, -100)
                    elif randomSpawn == 2: #further randomization of zombie spawn location
                        zombies[len(zombies)-1].centerx = player.centerx + random.randint (100, 500)
                    elif randomSpawn == 3: #further randomization of zombie spawn location
                        zombies[len(zombies)-1].centery = player.centery + random.randint (-500, -100)
                    elif randomSpawn == 4: #further randomization of zombie spawn location
                        zombies[len(zombies)-1].centery = player.centery + random.randint (100, 500)
                    if zombies[len(zombies)-1].centery >= 705 or zombies[len(zombies)-1].centery <= 0: #prevents zombie from spawning off of the screen (height)
                        pass
                    elif zombies[len(zombies)-1].centerx >= 1280 or zombies[len(zombies)-1].centerx <= 0: #prevents zombie from spawning off of the screen (width)
                        pass
                    elif zombies[len(zombies)-1].centerx > -100 and zombies[len(zombies)-1].centerx < 100: #ensures both an x and y coordinate are selected for zombie spawn
                        pass
                    elif zombies[len(zombies)-1].centery > -100 and zombies[len(zombies)-1].centery < 100: #ensures both an x and y coordinate are selected for zombie spawn
                        pass
                    else: #if there are no issues with the zombie spawn, the loop is broken to allow the zombie to spawn
                        break
            countBullets = 0 #reset to allow a zombie to spawn every 3 bullets
        if len(zombies) >= 1: #checks if at least 1 zombie exists before attempting to move the existing zombies
            zombieMove = random.randint (1,4) #helps to randomize zombie movements
            if zombieMove == 1: #only has a 1/4 chance of running
                numOfZombiesMoving = random.randint(0, len(zombies))
                for i in range(0, numOfZombiesMoving):
                    zombieMoveChoice = random.randint(1,4)
                    zombieMoveLengthChoice = random.randint (10, 13)
                    if zombieMoveChoice == 1:
                        for x in range (0, zombieMoveLengthChoice):
                            zombies[i].centerx += 2
                    elif zombieMoveChoice == 2:
                        for x in range (0, zombieMoveLengthChoice):
                            zombies[i].centerx -= 2
                    elif zombieMoveChoice == 3:
                        for x in range (0, zombieMoveLengthChoice):
                            zombies[i].centery += 2
                    elif zombieMoveChoice == 4:
                        for x in range (0, zombieMoveLengthChoice):
                           zombies[i].centery -= 2
                    if zombies[i].centerx <= 50:
                        zombies[i].centerx = 50
                    if zombies[i].centerx >= 1230:
                        zombies[i].centerx = 1230
                    if zombies[i].centery <= 50:
                        zombies[i].centery = 50
                    if zombies[i].centery >= 655:
                        zombies[i].centery = 655
        for i in range(0, len(zombies)):
            if player.colliderect(zombies[i]):
                if playerHealth >= 2:
                    playerHealth -= 1
                    health = healthImage[playerHealth].get_rect()
                else:
                    exitBulletNestedLoop = 1
                    endgame = 1
                    break
                while True:
                    player.centerx = random.randint(30, 1200)
                    player.centery = random. randint(30, 650)
                    for x in range(0, len(zombies)):
                        if zombies[x].centerx >= player.centerx - 300 and zombies[x].centerx <= player.centerx + 300:
                            pass
                        elif zombies[x].centery >= player.centery - 300 and zombies[x].centery <= player.centery + 300:
                            pass
                        else:
                            exitSpawnNestedLoop = 1
                            break
                    if exitSpawnNestedLoop == 1:
                        break
                health.centerx = 120 #health bar coordinates are reset to prevent glitch of the health bar moving
                health.centery = 50 #health bar coordinates are reset to prevent glitch of the health bar moving
            screen.blit(zombieImage, zombies[i]) #draws the zombies onscreen
        pygame.display.flip() #display is updated
        clock.tick(60) #maintains a steady framerate by controlling the speed of the loop
        if exitBulletNestedLoop == 1: #used to exit main game loop
            break
    if endgame == 1: #used to escape the nest of game loops, so that the game can be ended
        pygame.display.quit #closes old game window
        endingScreen = pygame.display.set_mode((1280, 705)) #creates a new 'game over' screen
        endingScreen.fill(teal) #fills background colour
        endingScreen.blit(gameOverText,(562,220)) #prints "GAME OVER" to screen
        endingScreen.blit(scoreText,(586,280)) #prints the player's score to screen
        endingScreen.blit(exitText,(519,340)) #prints a message for exiting the game to screen
        pygame.display.flip() #display is updated
        while True: #loop to continuously check for the 'enter' key to be pressed
            for event in pygame.event.get(): #checking for event
                            if event.type == pygame.KEYDOWN: #checking if a key is pressed
                                if event.key == pygame.K_RETURN: #checking if the 'enter' key is pressed
                                    pygame.display.quit() #closes window
                                    exitNestedLoop = 0
                                    #menu(teal, font1, playerImage, bulletImage, player, bullets, exitNestedLoop, playerDirection, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)
                                    startUp()
            clock.tick(30) #slows loop to 30 times per second instead of a rapid rate causing unneccessary lag
                    
    elif newBullet == 1: #re-runs function to implement new bullet
       game(screen, playerDirection, player, bullets, teal, playerImage, bulletImage, count, bulletSpeed, zombieImage, zombies, countBullets, clock, healthImage, health, playerHealth, font1, scoreText, healthText, score, endgame, font2, gameOverText, totalBullets, bulletsRemaining, bulletsText, enoughBullets, font3, exitText)

startUp()
