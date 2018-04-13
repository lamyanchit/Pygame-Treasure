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
goback=Image("goback.png",game)#go back button
goback.resizeBy(-40)
goback.y+=220
goback.x+=300

#Start Screen

while not game.over:
    game.processInput()
    bk1.draw()
    name.draw()
    storyB.draw()
    howtoplayB.draw()
    start.draw()

    if howtoplayB.collidedWith(mouse) and mouse.LeftClick:
        bk1.visible=False
        name.visible=False
        storyB.visible=False
        howtoplayB.visible=False
        start.visible=False
        howtoplay.draw()
        goback.draw()
        
    if storyB.collidedWith(mouse) and mouse.LeftClick:
        bk1.visible=False
        name.visible=False
        storyB.visible=False
        howtoplayB.visible=False
        start.visible=False
        story.draw()
        goback.draw()

    if goback.collidedWith(mouse)and mouse.LeftClick:
        howtoplay.visible=False
        story.visible=False 
        bk1.draw()
        name.draw()
        storyB.draw()
        howtoplayB.draw()
        start.draw()
        
    if start.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    if keys.Pressed[K_q]:
        game.quit()
       
    game.update(30)

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
game.over=False
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    bk.draw()
    peppa.draw()
    apple.draw()
    treebranch.draw()
    apple.move()
    treebranch.move()
    treasure.draw()
    treasure.visible=False
    #game.drawText("/15",-400,-600)
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
        peppa.x+=100
    if keys.Pressed[K_LEFT]:
        peepa.nextFrame()
        peppa.x-=100

    if peppa.collidedWith(treebranch):
        game.over=True
        gameover.draw()
        replay.draw()
        #lose.play()
         
    if game.score>=15:
        if treasure.isOffScreen("left"):
                treasure.moveTo(treasure.width+500,game.height-160)
                treasure.visible=True
        #youwin.draw()
        #win.play()
    if keys.Pressed[K_q]:
        game.quit()
        
    game.displayScore()
    game.update(60)

    

        
game.update()
game.wait(K_RETURN)
game.quit()

                  
