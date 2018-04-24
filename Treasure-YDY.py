#YDY
#Treasure
#Yaxin Dong,Dian Lin,YanChit Lam
#You will be in a forest. You need to using the space bottom to jump to get point. 

from gamelib import*
#game object
game=Game(800,600,"Treasure",60)

#Start Screen Object
name=Image("name.png",game)#game name
name.y-= 200
storyB=Image("storyB.png",game)#story button
storyB.resizeBy(-40)
storyB.y+=10
howtoplayB=Image("howtoplayB.png",game)#how to play button
howtoplayB.resizeBy(-40)
howtoplayB.y+=110
start=Image("start.png",game)#start button
start.resizeBy(-40)
start.y+=210
bk1=Image("startscreenbk.jpg",game)#title screen
bk1.resizeTo(800,600)
story=Image("story.png",game)#game story
story.resizeTo(800,600)
howtoplay=Image("howtoplay.png",game)#how to play the game
howtoplay.resizeTo(800,600)

#Start Screen

while not game.over:
    game.processInput()
    bk1.draw()
    name.draw()
    storyB.draw()
    howtoplayB.draw()
    start.draw()

    if howtoplayB.collidedWith(mouse) and mouse.LeftButton:
        start.x+=200
        start.y+=220
        storyB.x+=100
        storyB.y+=220
        start.visible=True
        story.visible=True
        bk1.visible=False
        name.visible=False
        howtoplayB.visible=False
        howtoplay.draw()
        if start.collidedWith(mouse) and mouse.LeftButton:
            game.over = True
        '''if storyB.collidedWith(mouse) and mouse.LeftButton:
            start.x+=200
            start.y+=220
            howtoplayB.x+=100
            howtoplayB.y+=220
            howtoplay.visible=True
            bk1.visible=False
            name.visible=False
            storyB.visible=False
            story.draw()
            if start.collidedWith(mouse) and mouse.LeftButton:
                 game.over = True''' 
        
            
    if storyB.collidedWith(mouse) and mouse.LeftButton:
        start.x+=200
        start.y+=220
        howtoplayB.x+=100
        howtoplayB.y+=220
        start.visible=True
        howtoplay.visible=True
        bk1.visible=False
        name.visible=False
        storyB.visible=False
        story.draw()
        if start.collidedWith(mouse) and mouse.LeftButton:
            game.over = True
        '''if howtoplayB.collidedWith(mouse) and mouse.LeftButton:
            start.x+=200
            start.y+=220
            storyB.x+=100
            storyB.y+=220
            start.visible=True
            story.visible=True
            bk1.visible=False
            name.visible=False
            howtoplayB.visible=False
            howtoplay.draw()
            if start.collidedWith(mouse) and mouse.LeftButton:
                 game.over = True'''

    if start.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

    if keys.Pressed[K_q]:
        game.quit()
    
    if keys.Pressed[K_f]:
        game.over = True
       
    game.update(30)


game.over=False


#image object
bk=Image("forest.jpg",game)
game.setBackground(bk)
peppa=Animation("peppa.png",1,game,219,219,frate=6)
peppa.resizeBy(-50)
peppa.moveTo(peppa.width+10,game.height-180)
apple=Image("apple.png",game)
apple.resizeBy(-93)
apple.moveTo(apple.width+255,game.height-300)
apple.setSpeed(2,90)
treebranch=Image("treebranch.png",game)
treebranch.resizeBy(-93)
treebranch.moveTo(treebranch.width+500,game.height-160)
treebranch.setSpeed(2,90)
treasure=Image("treasure.png",game)
treasure.resizeBy(-97)
treasure.moveTo(treasure.width+500,game.height-185)
treasure.setSpeed(2,90)
gameover=Image("gameover.png",game)
youwin=Image("youwin.png",game)
replay=Image("replay.png",game)
replay.resizeBy(-35)
replay.moveTo(replay.width+140,game.height-190)
#Sound object
#jump=Sound("jump.wav",1)
#lose=Sound("lose.flac",2)
#win=Sound("win.wav",3)

jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping


#Level One game loop

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    bk.draw()
    peppa.draw()
    apple.draw()
    treebranch.draw()
    apple.move()
    treebranch.move()
    #f=Font(white,5,"Comic Sans MC")
    #game.drawText("/15",-400,-600,f)
    if apple.isOffScreen("left"):
        y=randint(game.height-300,game.height-180)
        apple.moveTo(game.width+100,y)
        apple.visible=True
    if treebranch.isOffScreen("left"):
        treebranch.moveTo(treebranch.width+500,game.height-160)
        treebranch.visible=True
    if peppa.collidedWith(apple):          
        game.score+=1
        apple.speed+=1
        apple.visible=False
        
    if peppa.y< 400:
        landed = False#not landed
    else:
        landed = True
             
    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True
        #jump.play()

    if jumping:
        peppa.nextFrame()
        peppa.y -=32*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1 
            
    if not landed: #is jumping
        peppa.y +=11#adjust for the height of the jump - lower number h igher jump
        peppa.nextFrame() 

    if keys.Pressed[K_RIGHT]:
        peppa.nextFrame()
        peppa.x+=2
    if keys.Pressed[K_LEFT]:
        peppa.nextFrame()
        peppa.x-=2

    if peppa.collidedWith(treebranch):
        game.over=True
        gameover.draw()
        replay.draw()
        #lose.play()
         
    if game.score>=15:
        treasure.draw()
        treasure.visible=True
        if treasure.isOffScreen("left"):
            treasure.moveTo(treasure.width+500,game.height-180)
            treasure.visible=True
        if peppa.collidedWith(treasure):
            game.over=True
            youwin.draw()

        #win.play()
        
    if keys.Pressed[K_q]:
        game.quit()
       
    game.displayScore()
    game.update(60)


#Level 2: Image object
'''bk=Image("mountain.jpg",game)
game.setBackground(bk)
peppa=Animation("peppa.png",1,game,219,219,frate=6)
peppa.resizeBy(-50)
peppa.moveTo(peppa.width+10,game.height-193)
orange=Image("orange.png",game)
orange.resizeBy(-98)
orange.moveTo(orange.width+255,game.height-235)
orange.setSpeed(2,90)
snowball=Image("snowball.png",game)
snowball.resizeBy(-67)
snowball.moveTo(snowball.width+500,game.height-126)
snowball.setSpeed(2,90)
treasure=Image("treasure.png",game)
treasure.resizeBy(-97)
treasure.moveTo(treasure.width+500,game.height-185)
gameover=Image("gameover.png",game)
youwin=Image("youwin.png",game)
replay=Image("replay.png",game)
replay.resizeBy(-35)
replay.moveTo(replay.width+140,game.height-190)
#Sound object
#jump=Sound("jump.wav",1)
#lose=Sound("lose.flac",2)
#win=Sound("win.wav",3)

jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping
#Level Two game loop
game.over = False
while not game.over and game.score>2:
    game.processInput()
    while not game.over:
        game.processInput()
        game.scrollBackground("left",2)
        bk.draw()
        peppa.draw()
        orange.draw()
        snowball.draw()
        orange.move()
        snowball.move()
        #f=color("white)
        #game.drawText("/15",f,-400,-600)
        if orange.isOffScreen("left"):
            y=randint(game.height-300,game.height-180)
            orange.moveTo(game.width+100,y)
            orange.visible=True
        if snowball.isOffScreen("left"):
            snowball.moveTo(snowball.width+500,game.height-160)
            snowball.visible=True
        if peppa.collidedWith(orange):          
            game.score+=1
            orange.speed+=1
            orange.visible=False
        
        if peppa.y< 400:
            landed = False#not landed
        else:
            landed = True
             
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        #jump.play()
        if jumping:
            peppa.nextFrame()
            peppa.y -=32*factor#adjust for the drop
            #Make the character go up.  Factor creates a slowing effect to the jump
            factor*=.95#fall slowly
            landed = False        
            #Since you are jumping you are no longer staying on land
            if factor < .18:
                jumping = False
                #Stop jumping once the slowing effect finishes
                factor = 1 
            
        if not landed: #is jumping
            peppa.y +=11#adjust for the height of the jump - lower number h igher jump
            peppa.nextFrame() 

        if keys.Pressed[K_RIGHT]:
            peppa.nextFrame()
            peppa.x+=2
        if keys.Pressed[K_LEFT]:
            peppa.nextFrame()
            peppa.x-=2

        if peppa.collidedWith(snowball):
            game.over=True
            gameover.draw()
            replay.draw()
            #lose.play()
         
        if game.score>=8:
            treasure.draw()
            treasure.visible=True
            if treasure.isOffScreen("left"):
                treasure.moveTo(treasure.width+500,game.height-180)
                treasure.visible=True
            if peppa.collidedWith(treasure):
                game.over=True
                youwin.draw() 

                #win.play()
        
        if keys.Pressed[K_q]:
            game.quit()
       
        game.displayScore()
        game.update(60)'''
    

        
game.update()
game.wait(K_RETURN)
game.quit()
