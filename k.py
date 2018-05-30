from gamelib import*
#game object
game=Game(800,600,"Treasure",60)

#Level 2: Image object
bk=Image("mountain.jpg",game)
bk.resizeTo(800,600)
game.setBackground(bk)
peppa=Animation("peppa.png",1,game,219,219,frate=6)
peppa.resizeBy(-50)
peppa.moveTo(peppa.width+10,game.height-163)
orange=Image("orange.png",game)
orange.resizeBy(-98)
orange.moveTo(orange.width+255,game.height-265)
orange.setSpeed(2,90)
snowball=Image("snowball.png",game)
snowball.resizeBy(-73)
snowball.moveTo(snowball.width+500,game.height-150)
snowball.setSpeed(2,90)
treasure=Image("treasure.png",game)
treasure.resizeBy(-97)
treasure.moveTo(treasure.width+500,game.height-153)
gameover=Image("gameover.png",game)
youwin=Image("youwin.png",game)
replay=Image("replay.png",game)
replay.resizeBy(-35)
replay.moveTo(replay.width+140,game.height-190)
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping
while not game.over:
    game.processInput()
    bk.draw()
    peppa.draw()
    orange.draw()
    snowball.draw()
    orange.move()
    snowball.move()
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
        
    if peppa.y<400:
        landed=False
    else:
        landed=True      
             
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
         
    if game.score>=4:
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
game.update(60)   
game.wait(K_RETURN)
game.quit()
