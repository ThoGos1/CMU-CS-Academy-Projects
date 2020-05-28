#####We will be making a program that takes a different spin on the classic: Tetris
#In this game you have to build a tower using as many blocks as possible
#You can move the blocks with the right and left arrow keys, and rotate them 90
#degrees with the up button, and you can also make them fall faster by pressing the
#down key, and spacebar to return them to normal speed.
#If you need to take a break you can press the tab button to pause the game, and
#press it again or the resume button to resume.
#Out in the left side you can see your score and how many lines you have build up.
#When you hit the top the game will stop and your score will be shown, and to restart
#simply press the run button again and you can try to get a higher score :)


#The background is set here
app.background = 'black'

#Sets the app.stepsPerSecond to a very slow pace, like the actual game
app.stepsPerSecond = 10

#The way we see if the app should be paused
app.paused = True

#The grey sides, which is a group
sides = Group(Rect(0,0,99,400,fill='grey'),
Rect(302,0,99,400,fill='grey'))

#The shapes for when you finish the game
back = Rect(0,0,400,400,opacity=50,visible=False)
tetris2 = 'https://cdn.discordapp.com/attachments/554739370788257822/674478261480456202/tetris2.png'

#The shapes for the start menu
tetris = 'https://media.discordapp.net/attachments/554745868385910835/674469601635074069/tetrisnew.png'
#change this picture to something smaller and use align=center
startblack = Rect(0,0,400,400)
tetrisPic = Image(tetris,200,150,align='center')
start = Group(Rect(200,325,200,30,fill='white',align='center'), Label('Press here to start', 200,325,size=20))



#All of the block, including some 
###Groups
###Defining custom dx and dy properties
#The first batch of blocks
longB = Rect(200,0,20,100,fill='lightBlue',visible=False)
longB.dx = 10
longB.dy = 1

blueL = Group(Rect(200,0,20,20,fill='blue'), Rect(200,20,60,20,fill='blue'),align='center',visible=False)
blueL.dx = 10
blueL.dy = 1

orangeL = Group(Rect(200,0,20,20,fill='orange'),Rect(160,20,60,20,fill='orange'),visible=False)
orangeL.dx = 10
orangeL.dy = 1

block = Rect(200,0,40,40,fill='yellow',visible=False)
block.dx = 10
block.dy = 1

greenS = Group(Rect(200,0,40,20,fill='green'),Rect(180,20,40,20,fill='green'),visible=False)
greenS.dx = 10
greenS.dy = 1

redS = Group(Rect(180,0,40,20,fill='red'),Rect(200,20,40,20,fill='red'),visible=False)
redS.dx = 10
redS.dy = 1

t = Group(Rect(200,0,20,20,fill='purple'),Rect(180,20,60,20,fill='purple'),visible=False)
t.dx = 10
t.dy = 1

#The second batch of blocks
longB2 = Rect(200,0,20,100,fill='lightBlue',visible=False)
longB2.dx = 10
longB2.dy = 1

blueL2 = Group(Rect(200,0,20,20,fill='blue'), Rect(200,20,60,20,fill='blue'),align='center',visible=False)
blueL2.dx = 10
blueL2.dy = 1

orangeL2 = Group(Rect(200,0,20,20,fill='orange'),Rect(160,20,60,20,fill='orange'),visible=False)
orangeL2.dx = 10
orangeL2.dy = 1

block2 = Rect(200,0,40,40,fill='yellow',visible=False)
block2.dx = 10
block2.dy = 1

greenS2 = Group(Rect(200,0,40,20,fill='green'),Rect(180,20,40,20,fill='green'),visible=False)
greenS2.dx = 10
greenS2.dy = 1

redS2 = Group(Rect(180,0,40,20,fill='red'),Rect(200,20,40,20,fill='red'),visible=False)
redS2.dx = 10
redS2.dy = 1

t2 = Group(Rect(200,0,20,20,fill='purple'),Rect(180,20,60,20,fill='purple'),visible=False)
t2.dx = 10
t2.dy = 1


#The third batch of blocks
longB3 = Rect(200,0,20,100,fill='lightBlue',visible=False)
longB3.dx = 10
longB3.dy = 1

blueL3 = Group(Rect(200,0,20,20,fill='blue'), Rect(200,20,60,20,fill='blue'),align='center',visible=False)
blueL3.dx = 10
blueL3.dy = 1

orangeL3 = Group(Rect(200,0,20,20,fill='orange'),Rect(160,20,60,20,fill='orange'),visible=False)
orangeL3.dx = 10
orangeL3.dy = 1

block3 = Rect(200,0,40,40,fill='yellow',visible=False)
block3.dx = 10
block3.dy = 1

greenS3 = Group(Rect(200,0,40,20,fill='green'),Rect(180,20,40,20,fill='green'),visible=False)
greenS3.dx = 10
greenS3.dy = 1

redS3 = Group(Rect(180,0,40,20,fill='red'),Rect(200,20,40,20,fill='red'),visible=False)
redS3.dx = 10
redS3.dy = 1

t3 = Group(Rect(200,0,20,20,fill='purple'),Rect(180,20,60,20,fill='purple'),visible=False)
t3.dx = 10
t3.dy = 1

#The fourth batch of blocks
longB4 = Rect(200,0,20,100,fill='lightBlue',visible=False)
longB4.dx = 10
longB4.dy = 1

blueL4 = Group(Rect(200,0,20,20,fill='blue'), Rect(200,20,60,20,fill='blue'),align='center',visible=False)
blueL4.dx = 10
blueL4.dy = 1

orangeL4 = Group(Rect(200,0,20,20,fill='orange'),Rect(160,20,60,20,fill='orange'),visible=False)
orangeL4.dx = 10
orangeL4.dy = 1

block4 = Rect(200,0,40,40,fill='yellow',visible=False)
block4.dx = 10
block4.dy = 1

greenS4 = Group(Rect(200,0,40,20,fill='green'),Rect(180,20,40,20,fill='green'),visible=False)
greenS4.dx = 10
greenS4.dy = 1

redS4 = Group(Rect(180,0,40,20,fill='red'),Rect(200,20,40,20,fill='red'),visible=False)
redS4.dx = 10
redS4.dy = 1

t4 = Group(Rect(200,0,20,20,fill='purple'),Rect(180,20,60,20,fill='purple'),visible=False)
t4.dx = 10
t4.dy = 1

#An empty group that the blocks gets added to and cannot be moved with the arrow keys 
pile = Group()


#The score and scoreboard:
scoreboard = Group(
    Label('SCORE',50,160,fill='White'),
    Rect(10,170,80,20,fill='Black',border=gradient('red','orange','yellow',
    'green','blue','purple',start='left'))
    )
score = Label(0,50,180,fill='white')


#The lines in the side menu under the scoreboard
lines = Group(
    Label('LINES',50,210,fill='White'),
    Rect(10,220,80,20,fill='Black',border=gradient('red','orange','yellow',
    'green','blue','purple',start='left'))
    )

linesScore = Label(0, 50,230,fill='white')


#The Pause Menu
tetrisLogo = Group(
    Polygon(100,65,120,65,120,70,113,70,113,90,107,90,107,70,100,70,fill='red'),
    Polygon(125,65,125,90,145,90,145,85,130,85,130,80,145,80,145,75,130,75,130,70,145,70,145,65,125,65,fill='orange'),
    Polygon(150,65,170,65,170,70,163,70,163,90,157,90,157,70,150,70,fill='gold'),
    Arc(175,73,35,15,0,180,fill=None,border='forestGreen',borderWidth=5),
    Line(178,80,178,90,fill='forestGreen',lineWidth=5.5),
    Line(178,75,190,89,fill='forestGreen',lineWidth=5),
    Line(200,65,200,90,fill='lightSkyBlue',lineWidth=5.5),
    Polygon(212,65,228,65,228,70,219,70,228,85,228,90,212,90,212,85,221,85,212,70,fill='purple')
    ,Circle(212,67.5,2,fill='purple')
    ,Circle(228,87.5,2,fill='purple')
    )
tetrisS = Group(
    Polygon(100,65,120,65,120,70,113,70,113,90,107,90,107,70,100,70,fill='red'),
    Polygon(125,65,125,90,145,90,145,85,130,85,130,80,145,80,145,75,130,75,130,70,145,70,145,65,125,65,fill='orange'),
    Polygon(150,65,170,65,170,70,163,70,163,90,157,90,157,70,150,70,fill='gold'),
    Arc(175,73,35,15,0,180,fill=None,border='forestGreen',borderWidth=5),
    Line(178,80,178,90,fill='forestGreen',lineWidth=5.5),
    Line(178,75,190,89,fill='forestGreen',lineWidth=5),
    Line(200,65,200,90,fill='lightSkyBlue',lineWidth=5.5),
    Polygon(212,65,228,65,228,70,219,70,228,85,228,90,212,90,212,85,221,85,212,70,fill='purple')
    ,Circle(212,67.5,2,fill='purple')
    ,Circle(228,87.5,2,fill='purple')
    )
###Group position property
tetrisS.centerX=50
tetrisS.centerY=120
###Group non-position property
tetrisS.width=95
tetrisS.height=20
tetrisLogo.centerX=200
tetrisLogo.centerY=120

resume = Group(
    Rect(150,260,100,30,fill='white',border='black')
    )
quit = Group(
    Rect(150,300,100,30,fill='white',border='black')
    )

pauseMenu = Group(
    tetrisLogo,
    Rect(100,150,200,200,fill='grey'),
    Rect(120,200,160,50,fill='White'),
    Label('SCORE:',200,180,fill='white',size=35,bold=True),
    resume,
    quit,
    Label('QUIT',200,315,size=20),
    Label('RESUME',200,275,size=20), visible=False
    )
menuScore = Label(score.value,200,225,fill='black',size=40,visible=False)




#When you hover the mouse over then buttons they light up
def onMouseMove(mouseX,mouseY):
    if resume.contains(mouseX,mouseY):
        resume.fill='lightSkyBlue'
    else:
        ###A shape specific property
        resume.fill='white'
    if quit.contains(mouseX,mouseY):
        quit.fill='lightSkyBlue'
    else:
        quit.fill='white'

#Lets you use the mouse to resume, quit or start the game
def onMousePress(mouseX,mouseY):
    ###Nested Conditional
    if(resume.hits(mouseX,mouseY) and pauseMenu.visible==True):
        menuScore.value=score.value
        togglePause()
        if(app.paused==True):
            pauseMenu.visible=True
            menuScore.visible=True
        else:
            pauseMenu.visible=False
            menuScore.visible=False
    if(quit.hits(mouseX,mouseY) and pauseMenu.visible==True):
        app.stop()
        Rect(0,0,400,400)
        Label("Do you want to play again?",200,150,size=20,fill='white')
        Label("Press the Run Button to Restart",200,270,size=20,fill='white')
        Circle(200,300,15,fill='limeGreen')
        RegularPolygon(200,300,8,3,rotateAngle=90,fill='white')
        Image(tetris2,200,65,align='center')
    if(start.hits(mouseX,mouseY)):
        app.paused=False
        start.clear()
        startblack.visible=False
        tetrisPic.visible=False
        longB.visible=True




###onStep
def onStep():
    #First batch of blocks
    
    #Movement of the long blue block
    if(longB.bottom<=400 and longB.visible==True and not(longB.hitsShape(pile))):
        longB.visible = True
        longB.centerY += longB.dy
    elif(longB.bottom>=400 or longB.hitsShape(pile)):
        ###.add() method
        pile.add(longB)
        blueL.visible=True
        score.value=10
        checkWin()
        #Changes the line score in the left side
        linesScore.value=int(pile.height/20)
    
    
    #Movement of the blue L block
    ###Compounded Conditional
    if(blueL.bottom<=400 and blueL.visible==True and not(blueL.hitsShape(pile))):
        blueL.centerY += blueL.dy
    elif(blueL.bottom>=400 or pile.hitsShape(blueL)):
        pile.add(blueL)
        orangeL.visible=True
        score.value=20
        checkWin()
    
    #Movement of the orange L block
    if(orangeL.bottom<=400 and orangeL.visible==True and not(orangeL.hitsShape(pile))):
        ###Group position property
        orangeL.centerY += orangeL.dy
    elif(orangeL.bottom>=400 or orangeL.hitsShape(pile)):
        pile.add(orangeL)
        block.visible=True
        score.value=30
        checkWin()
    
    #Movement of the block
    if(block.bottom<=400 and block.visible==True and not(block.hitsShape(pile))):
        ###Changes the dy custom property
        block.centerY += block.dy
    elif(block.bottom>=400 or block.hitsShape(pile)):
        pile.add(block)
        greenS.visible=True
        score.value=40
        checkWin()
    
    #Movement of the green S block
    if(greenS.bottom<=400 and greenS.visible==True and not(greenS.hitsShape(pile))):
        greenS.centerY += greenS.dy
    elif(greenS.bottom>=400 or greenS.hitsShape(pile)):
        pile.add(greenS)
        redS.visible=True
        score.value=50
        checkWin()
    
    #Movement for red S block
    if(redS.bottom<=400 and redS.visible==True and not(redS.hitsShape(pile))):
        redS.centerY += redS.dy
    elif(redS.bottom>=400 or redS.hitsShape(pile)):
        pile.add(redS)
        t.visible=True
        score.value=60
        checkWin()
    
    #Movement for t block
    if(t.bottom<=400 and t.visible==True and not(t.hitsShape(pile))):
        t.centerY += t.dy
    elif(t.bottom>=400 or t.hitsShape(pile)):
        pile.add(t)
        score.value=70
        longB2.visible=True
        checkWin()
    
    
    #Second batch of blocks
    
    #Movement of the long blue 2 block
    if(longB2.bottom<=400 and longB2.visible==True and not(longB2.hitsShape(pile))):
        longB2.visible = True
        longB2.centerY += longB2.dy
    elif(longB2.bottom>=400 or longB2.hitsShape(pile)):
        pile.add(longB2)
        blueL2.visible=True
        score.value=80
        checkWin()
    
    
    #Movement of the blue L 2 block
    if(blueL2.bottom<=400 and blueL2.visible==True and not(blueL2.hitsShape(pile))):
        blueL2.centerY += blueL2.dy
    elif(blueL2.bottom>=400 or pile.hitsShape(blueL2)):
        pile.add(blueL2)
        orangeL2.visible=True
        score.value=90
        checkWin()
    
    #Movement of the orange L 2 block
    if(orangeL2.bottom<=400 and orangeL2.visible==True and not(orangeL2.hitsShape(pile))):
        orangeL2.centerY += orangeL2.dy
    elif(orangeL2.bottom>=400 or orangeL2.hitsShape(pile)):
        pile.add(orangeL2)
        block2.visible=True
        score.value=100
        checkWin()
    
    #Movement of the block 2
    if(block2.bottom<=400 and block2.visible==True and not(block2.hitsShape(pile))):
        block2.centerY += block2.dy
    elif(block2.bottom>=400 or block2.hitsShape(pile)):
        pile.add(block2)
        greenS2.visible=True
        score.value=110
        checkWin()
    
    #Movement of the green S 2 block 
    if(greenS2.bottom<=400 and greenS2.visible==True and not(greenS2.hitsShape(pile))):
        greenS2.centerY += greenS2.dy
    elif(greenS2.bottom>=400 or greenS2.hitsShape(pile)):
        pile.add(greenS2)
        redS2.visible=True
        score.value=120
        checkWin()
    
    #Movement for red S 2 block
    if(redS2.bottom<=400 and redS2.visible==True and not(redS2.hitsShape(pile))):
        redS2.centerY += redS2.dy
    elif(redS2.bottom>=400 or redS2.hitsShape(pile)):
        pile.add(redS2)
        t2.visible=True
        score.value=130
        checkWin()
    
    #Movement for t 2 block
    if(t2.bottom<=400 and t2.visible==True and not(t2.hitsShape(pile))):
        t2.centerY += t2.dy
    elif(t2.bottom>=400 or t2.hitsShape(pile)):
        pile.add(t2)
        score.value=140
        checkWin()
        longB3.visible=True
    
    
    #Third batch of blocks
    
    #Movement of the long blue 3 block
    if(longB3.bottom<=400 and longB3.visible==True and not(longB3.hitsShape(pile))):
        longB3.visible = True
        longB3.centerY += longB3.dy
    elif(longB3.bottom>=400 or longB3.hitsShape(pile)):
        pile.add(longB3)
        blueL3.visible=True
        score.value=150
        checkWin()
    
    
    #Movement of the blue L 3 block
    if(blueL3.bottom<=400 and blueL3.visible==True and not(blueL3.hitsShape(pile))):
        blueL3.centerY += blueL3.dy
    elif(blueL3.bottom>=400 or pile.hitsShape(blueL3)):
        pile.add(blueL3)
        orangeL3.visible=True
        score.value=160
        checkWin()
    
    #Movement of the orange L 3 block
    if(orangeL3.bottom<=400 and orangeL3.visible==True and not(orangeL3.hitsShape(pile))):
        orangeL3.centerY += orangeL3.dy
    elif(orangeL3.bottom>=400 or orangeL3.hitsShape(pile)):
        pile.add(orangeL3)
        block3.visible=True
        score.value=170
        checkWin()
    
    #Movement of the block 3
    if(block3.bottom<=400 and block3.visible==True and not(block3.hitsShape(pile))):
        block3.centerY += block3.dy
    elif(block3.bottom>=400 or block3.hitsShape(pile)):
        pile.add(block3)
        greenS3.visible=True
        score.value=180
        checkWin()
    
    #Movement of the green S 3 block 
    if(greenS3.bottom<=400 and greenS3.visible==True and not(greenS3.hitsShape(pile))):
        greenS3.centerY += greenS3.dy
    elif(greenS3.bottom>=400 or greenS3.hitsShape(pile)):
        pile.add(greenS3)
        redS3.visible=True
        score.value=190
        checkWin()
    
    #Movement for red S 3 block
    if(redS3.bottom<=400 and redS3.visible==True and not(redS3.hitsShape(pile))):
        redS3.centerY += redS3.dy
    elif(redS3.bottom>=400 or redS3.hitsShape(pile)):
        pile.add(redS3)
        t3.visible=True
        score.value=200
        checkWin()
    
    #Movement for t 3 block
    if(t3.bottom<=400 and t3.visible==True and not(t3.hitsShape(pile))):
        t3.centerY += t3.dy
    elif(t3.bottom>=400 or t3.hitsShape(pile)):
        pile.add(t3)
        longB4.visible=True
        score.value=210
        checkWin()
    
    
    #Fourth batch of blocks
    
    #Movement of the long blue 4 block
    if(longB4.bottom<=400 and longB4.visible==True and not(longB4.hitsShape(pile))):
        longB4.visible = True
        longB4.centerY += longB4.dy
    elif(longB4.bottom>=400 or longB4.hitsShape(pile)):
        pile.add(longB4)
        blueL4.visible=True
        score.value=220
        checkWin()
    
    
    #Movement of the blue L 4 block
    if(blueL4.bottom<=400 and blueL4.visible==True and not(blueL4.hitsShape(pile))):
        blueL4.centerY += blueL4.dy
    elif(blueL4.bottom>=400 or pile.hitsShape(blueL4)):
        pile.add(blueL4)
        orangeL4.visible=True
        score.value=230
        checkWin()
    
    #Movement of the orange L 4 block
    if(orangeL4.bottom<=400 and orangeL4.visible==True and not(orangeL4.hitsShape(pile))):
        orangeL4.centerY += orangeL4.dy
    elif(orangeL4.bottom>=400 or orangeL4.hitsShape(pile)):
        pile.add(orangeL4)
        block4.visible=True
        score.value=240
        checkWin()
    
    #Movement of the block 4
    if(block4.bottom<=400 and block4.visible==True and not(block4.hitsShape(pile))):
        block4.centerY += block4.dy
    elif(block4.bottom>=400 or block4.hitsShape(pile)):
        pile.add(block4)
        greenS4.visible=True
        score.value=250
        checkWin()
    
    #Movement of the green S 4 block 
    if(greenS4.bottom<=400 and greenS4.visible==True and not(greenS4.hitsShape(pile))):
        greenS4.centerY += greenS4.dy
    elif(greenS4.bottom>=400 or greenS4.hitsShape(pile)):
        pile.add(greenS4)
        redS4.visible=True
        score.value=260
        checkWin()
    
    #Movement for red S 4 block
    if(redS4.bottom<=400 and redS4.visible==True and not(redS4.hitsShape(pile))):
        redS4.centerY += redS4.dy
    elif(redS4.bottom>=400 or redS4.hitsShape(pile)):
        pile.add(redS4)
        t4.visible=True
        score.value=270
        checkWin()
    
    #Movement for t 4 block
    if(t4.bottom<=400 and t4.visible==True and not(t4.hitsShape(pile))):
        t4.centerY += t4.dy
    elif(t4.bottom>=400 or t4.hitsShape(pile)):
        pile.add(t4)
        score.value=280
        checkWin()

###onKeyHold
#Changes the speed of the blocks falling, the longer you hold the faster it goes
def onKeyHold(keys):
    if('down' in keys):
        ###Changing app.stepsPerSecond
        app.stepsPerSecond += 150
    if('space' in keys):
        app.stepsPerSecond = 10

#Toggles the app.paused custom property used for the pause screen
def togglePause():
    if app.paused==False:
        app.paused=True
    elif app.paused==True:
        app.paused=False

#Checks if the game finishes and shows you your score
def checkWin():
    if(pile.height>=400):
        app.stop()
        ###Remove method
        #Will make the end of game screen more aesthetically pleasing
        pile.remove(longB)
        pile.remove(blueL)
        pile.remove(orangeL)
        pile.remove(t)
        pile.remove(greenS)
        pile.remove(redS)
        pile.remove(block)
        pile.remove(longB2)
        Line(15,180,80,180,fill='white',arrowEnd=True)
        back.visible=True
        back.toFront()
        Rect(200,200,220,300,align='center',border='grey')
        Label("That's it",200,200,fill='white',size=20)
        Label("You got a score of:",200,230,fill='white',size=20)
        Label(score.value, 200,255,fill='white',size=20)
        Label('points',200,280,fill='white',size=20)
        Label('Great Job!',200,315,fill='white',size=20)
        Image(tetris2,200,125,align='center')
        ###Group non-position property
        #Will make the end of game screen more aesthetically pleasing
        pile.fill='grey'
        score.visible=False
        print('Your Score:', score.value)
        



#Movement of all of the blocks
def onKeyPress(key):
    #First batch of blocks
    
    #Movement of the long blue block
    ###Nested Conditonals
    if(longB.right<=300 and longB.left>=100 and longB.bottom<=400 and longB.visible==True and not(longB.hitsShape(pile))):
        if(key == 'left'):
            longB.left -= longB.dx
        if(key == 'right'):
            longB.right += longB.dx
        if(key == 'up'):
            longB.rotateAngle+=90
    ###Compounded Conditionals
    if(longB.hitsShape(sides) and longB.centerX<200):
        longB.left=100
    if(longB.hitsShape(sides) and longB.centerX>200):
        longB.right=300
    
    #Movement of the blue L block
    if(blueL.right<=300 and blueL.left>=100 and blueL.bottom<=400 and blueL.visible==True and not(blueL.hitsShape(pile))):
        if(key == 'left'):
            ###Group position property 
            blueL.left -= blueL.dx
        if(key == 'right'):
            blueL.right += blueL.dx
        if(key == 'up'):
            blueL.rotateAngle+=90
    if(blueL.hitsShape(sides) and blueL.centerX<200):
        blueL.left=100
    if(blueL.hitsShape(sides) and blueL.centerX>200):
        blueL.right=300
    
    #Movement of the orange L block
    if(orangeL.right<=300 and orangeL.left>=100 and orangeL.bottom<=400 and orangeL.visible==True and not(orangeL.hitsShape(pile))):
        if(key == 'left'):
            ###Changes the dx custom property
            orangeL.left -= orangeL.dx
        if(key == 'right'):
            orangeL.right += orangeL.dx
        if(key == 'up'):
            orangeL.rotateAngle+=90
    if(orangeL.hitsShape(sides) and orangeL.centerX<200):
        orangeL.left=100
    if(orangeL.hitsShape(sides) and orangeL.centerX>200):
        orangeL.right=300
    
    #Movement of the block
    if(block.right<=300 and block.left>=100 and block.bottom<=400 and block.visible==True and not(block.hitsShape(pile))):
        if(key == 'left'):
            block.left -= block.dx
        if(key == 'right'):
            block.right += block.dx
        if(key == 'up'):
            block.rotateAngle+=90
    if(block.hitsShape(sides) and block.centerX<200):
        block.left=100
    if(block.hitsShape(sides) and block.centerX>200):
        block.right=300
    
    #Movement of the green S block
    if(greenS.right<=300 and greenS.left>=100 and greenS.bottom<=400 and greenS.visible==True and not(greenS.hitsShape(pile))):
        if(key == 'left'):
            greenS.left -= greenS.dx
        if(key == 'right'):
            greenS.right += greenS.dx
        if(key == 'up'):
            greenS.rotateAngle+=90
    if(greenS.hitsShape(sides) and greenS.centerX<200):
        greenS.left=100
    if(greenS.hitsShape(sides) and greenS.centerX>200):
        greenS.right=300
    
    #Movement of the red S block
    if(redS.right<=300 and redS.left>=100 and redS.bottom<=400 and redS.visible==True and not(redS.hitsShape(pile))):
        if(key == 'left'):
            redS.left -= redS.dx
        if(key == 'right'):
            redS.right += redS.dx
        if(key == 'up'):
            redS.rotateAngle+=90
    if(redS.hitsShape(sides) and redS.centerX<200):
        redS.left=100
    if(redS.hitsShape(sides) and redS.centerX>200):
        redS.right=300
    
    #Movement of the T block
    if(t.right<=300 and t.left>=100 and t.bottom<=400 and t.visible==True and not(t.hitsShape(pile))):
        if(key == 'left'):
            t.left -= t.dx
        if(key == 'right'):
            t.right += t.dx
        if(key == 'up'):
            t.rotateAngle+=90
    if(t.hitsShape(sides) and t.centerX<200):
        t.left=100
    if(t.hitsShape(sides) and t.centerX>200):
        t.right=300
    
    #Second batch of blocks
    
    
    #Movement of the long blue 2 block
    if(longB2.right<=300 and longB2.left>=100 and longB2.bottom<=400 and longB2.visible==True and not(longB2.hitsShape(pile))):
        if(key == 'left'):
            longB2.left -= longB2.dx
        if(key == 'right'):
            longB2.right += longB2.dx
        if(key == 'up'):
            longB2.rotateAngle+=90
    if(longB2.hitsShape(sides) and longB2.centerX<200):
        longB2.left=100
    if(longB2.hitsShape(sides) and longB2.centerX>200):
        longB2.right=300
    
    #Movement of the blue L 2 block
    if(blueL2.right<=300 and blueL2.left>=100 and blueL2.bottom<=400 and blueL2.visible==True and not(blueL2.hitsShape(pile))):
        if(key == 'left'):
            blueL2.left -= blueL2.dx
        if(key == 'right'):
            blueL2.right += blueL2.dx
        if(key == 'up'):
            blueL2.rotateAngle+=90
    if(blueL2.hitsShape(sides) and blueL2.centerX<200):
        blueL2.left=100
    if(blueL2.hitsShape(sides) and blueL2.centerX>200):
        blueL2.right=300
    
    #Movement of the orange L 2 block
    if(orangeL2.right<=300 and orangeL2.left>=100 and orangeL2.bottom<=400 and orangeL2.visible==True and not(orangeL2.hitsShape(pile))):
        if(key == 'left'):
            orangeL2.left -= orangeL2.dx
        if(key == 'right'):
            orangeL2.right += orangeL2.dx
        if(key == 'up'):
            orangeL2.rotateAngle+=90
    if(orangeL2.hitsShape(sides) and orangeL2.centerX<200):
        orangeL2.left=100
    if(orangeL2.hitsShape(sides) and orangeL2.centerX>200):
        orangeL2.right=300
    
    #Movement of the block 2
    if(block2.right<=300 and block2.left>=100 and block2.bottom<=400 and block2.visible==True and not(block2.hitsShape(pile))):
        if(key == 'left'):
            block2.left -= block2.dx
        if(key == 'right'):
            block2.right += block2.dx
        if(key == 'up'):
            block2.rotateAngle+=90
    if(block2.hitsShape(sides) and block2.centerX<200):
        block2.left=100
    if(block2.hitsShape(sides) and block2.centerX>200):
        block2.right=300
    
    #Movement of the green S 2 block
    if(greenS2.right<=300 and greenS2.left>=100 and greenS2.bottom<=400 and greenS2.visible==True and not(greenS2.hitsShape(pile))):
        if(key == 'left'):
            greenS2.left -= greenS2.dx
        if(key == 'right'):
            greenS2.right += greenS2.dx
        if(key == 'up'):
            greenS2.rotateAngle+=90
    if(greenS2.hitsShape(sides) and greenS2.centerX<200):
        greenS2.left=100
    if(greenS2.hitsShape(sides) and greenS2.centerX>200):
        greenS2.right=300
    
    #Movement of the red S 2 block
    if(redS2.right<=300 and redS2.left>=100 and redS2.bottom<=400 and redS2.visible==True and not(redS2.hitsShape(pile))):
        if(key == 'left'):
            redS2.left -= redS2.dx
        if(key == 'right'):
            redS2.right += redS2.dx
        if(key == 'up'):
            redS2.rotateAngle+=90
    if(redS2.hitsShape(sides) and redS2.centerX<200):
        redS2.left=100
    if(redS2.hitsShape(sides) and redS2.centerX>200):
        redS2.right=300
    
    #Movement of the T 2 block
    if(t2.right<=300 and t2.left>=100 and t2.bottom<=400 and t2.visible==True and not(t2.hitsShape(pile))):
        if(key == 'left'):
            t2.left -= t2.dx
        if(key == 'right'):
            t2.right += t2.dx
        if(key == 'up'):
            t2.rotateAngle+=90
    if(t2.hitsShape(sides) and t2.centerX<200):
        t2.left=100
    if(t2.hitsShape(sides) and t2.centerX>200):
        t2.right=300
    
    
    #Third batch of blocks
    
    
    #Movement of the long blue 3 block
    if(longB3.right<=300 and longB3.left>=100 and longB3.bottom<=400 and longB3.visible==True and not(longB3.hitsShape(pile))):
        if(key == 'left'):
            longB3.left -= longB3.dx
        if(key == 'right'):
            longB3.right += longB3.dx
        if(key == 'up'):
            longB3.rotateAngle+=90
    if(longB3.hitsShape(sides) and longB3.centerX<200):
        longB3.left=100
    if(longB3.hitsShape(sides) and longB3.centerX>200):
        longB3.right=300
    
    #Movement of the blue L 3 block
    if(blueL3.right<=300 and blueL3.left>=100 and blueL3.bottom<=400 and blueL3.visible==True and not(blueL3.hitsShape(pile))):
        if(key == 'left'):
            blueL3.left -= blueL3.dx
        if(key == 'right'):
            blueL3.right += blueL3.dx
        if(key == 'up'):
            blueL3.rotateAngle+=90
    if(blueL3.hitsShape(sides) and blueL3.centerX<200):
        blueL3.left=100
    if(blueL3.hitsShape(sides) and blueL3.centerX>200):
        blueL3.right=300
    
    #Movement of the orange L 3 block
    if(orangeL3.right<=300 and orangeL3.left>=100 and orangeL3.bottom<=400 and orangeL3.visible==True and not(orangeL3.hitsShape(pile))):
        if(key == 'left'):
            orangeL3.left -= orangeL3.dx
        if(key == 'right'):
            orangeL3.right += orangeL3.dx
        if(key == 'up'):
            orangeL3.rotateAngle+=90
    if(orangeL3.hitsShape(sides) and orangeL3.centerX<200):
        orangeL3.left=100
    if(orangeL3.hitsShape(sides) and orangeL3.centerX>200):
        orangeL3.right=300
    
    #Movement of the block 3
    if(block3.right<=300 and block3.left>=100 and block3.bottom<=400 and block3.visible==True and not(block3.hitsShape(pile))):
        if(key == 'left'):
            block3.left -= block3.dx
        if(key == 'right'):
            block3.right += block3.dx
        if(key == 'up'):
            block3.rotateAngle+=90
    if(block3.hitsShape(sides) and block3.centerX<200):
        block3.left=100
    if(block3.hitsShape(sides) and block3.centerX>200):
        block3.right=300
    
    #Movement of the green S 3 block
    if(greenS3.right<=300 and greenS3.left>=100 and greenS3.bottom<=400 and greenS3.visible==True and not(greenS3.hitsShape(pile))):
        if(key == 'left'):
            greenS3.left -= greenS3.dx
        if(key == 'right'):
            greenS3.right += greenS3.dx
        if(key == 'up'):
            greenS3.rotateAngle+=90
    if(greenS3.hitsShape(sides) and greenS3.centerX<200):
        greenS3.left=100
    if(greenS3.hitsShape(sides) and greenS3.centerX>200):
        greenS3.right=300
    
    #Movement of the red S 3 block
    if(redS3.right<=300 and redS3.left>=100 and redS3.bottom<=400 and redS3.visible==True and not(redS3.hitsShape(pile))):
        if(key == 'left'):
            redS3.left -= redS3.dx
        if(key == 'right'):
            redS3.right += redS3.dx
        if(key == 'up'):
            redS3.rotateAngle+=90
    if(redS3.hitsShape(sides) and redS3.centerX<200):
        redS3.left=100
    if(redS3.hitsShape(sides) and redS3.centerX>200):
        redS3.right=300
    
    #Movement of the T 3 block
    if(t3.right<=300 and t3.left>=100 and t3.bottom<=400 and t3.visible==True and not(t3.hitsShape(pile))):
        if(key == 'left'):
            t3.left -= t3.dx
        if(key == 'right'):
            t3.right += t3.dx
        if(key == 'up'):
            t3.rotateAngle+=90
    if(t3.hitsShape(sides) and t3.centerX<200):
        t3.left=100
    if(t3.hitsShape(sides) and t3.centerX>200):
        t3.right=300
    
    
    #Fourth batch of blocks
    
    #Movement of the long blue 4 block
    if(longB4.right<=300 and longB4.left>=100 and longB4.bottom<=400 and longB4.visible==True and not(longB4.hitsShape(pile))):
        if(key == 'left'):
            longB4.left -= longB4.dx
        if(key == 'right'):
            longB4.right += longB4.dx
        if(key == 'up'):
            longB4.rotateAngle+=90
    if(longB4.hitsShape(sides) and longB4.centerX<200):
        longB4.left=100
    if(longB4.hitsShape(sides) and longB4.centerX>200):
        longB4.right=300
    
    #Movement of the blue L 4 block
    if(blueL4.right<=300 and blueL4.left>=100 and blueL4.bottom<=400 and blueL4.visible==True and not(blueL4.hitsShape(pile))):
        if(key == 'left'):
            blueL4.left -= blueL4.dx
        if(key == 'right'):
            blueL4.right += blueL4.dx
        if(key == 'up'):
            blueL4.rotateAngle+=90
    if(blueL4.hitsShape(sides) and blueL4.centerX<200):
        blueL4.left=100
    if(blueL4.hitsShape(sides) and blueL4.centerX>200):
        blueL4.right=300
    
    #Movement of the orange L 4 block
    if(orangeL4.right<=300 and orangeL4.left>=100 and orangeL4.bottom<=400 and orangeL4.visible==True and not(orangeL4.hitsShape(pile))):
        if(key == 'left'):
            orangeL4.left -= orangeL4.dx
        if(key == 'right'):
            orangeL4.right += orangeL4.dx
        if(key == 'up'):
            orangeL4.rotateAngle+=90
    if(orangeL4.hitsShape(sides) and orangeL4.centerX<200):
        orangeL4.left=100
    if(orangeL4.hitsShape(sides) and orangeL4.centerX>200):
        orangeL4.right=300
    
    #Movement of the block 4
    if(block4.right<=300 and block4.left>=100 and block4.bottom<=400 and block4.visible==True and not(block4.hitsShape(pile))):
        if(key == 'left'):
            block4.left -= block4.dx
        if(key == 'right'):
            block4.right += block4.dx
        if(key == 'up'):
            block4.rotateAngle+=90
    if(block4.hitsShape(sides) and block4.centerX<200):
        block4.left=100
    if(block4.hitsShape(sides) and block4.centerX>200):
        block4.right=300
    
    #Movement of the green S 4 block
    if(greenS4.right<=300 and greenS4.left>=100 and greenS4.bottom<=400 and greenS4.visible==True and not(greenS4.hitsShape(pile))):
        if(key == 'left'):
            greenS4.left -= greenS4.dx
        if(key == 'right'):
            greenS4.right += greenS4.dx
        if(key == 'up'):
            greenS4.rotateAngle+=90
    if(greenS4.hitsShape(sides) and greenS4.centerX<200):
        greenS4.left=100
    if(greenS4.hitsShape(sides) and greenS4.centerX>200):
        greenS4.right=300
    
    #Movement of the red S 4 block
    if(redS4.right<=300 and redS4.left>=100 and redS4.bottom<=400 and redS4.visible==True and not(redS4.hitsShape(pile))):
        if(key == 'left'):
            redS4.left -= redS4.dx
        if(key == 'right'):
            redS4.right += redS4.dx
        if(key == 'up'):
            redS4.rotateAngle+=90
    if(redS4.hitsShape(sides) and redS4.centerX<200):
        redS4.left=100
    if(redS4.hitsShape(sides) and redS4.centerX>200):
        redS4.right=300
    
    #Movement of the T 4 block
    if(t4.right<=300 and t4.left>=100 and t4.bottom<=400 and t4.visible==True and not(t4.hitsShape(pile))):
        if(key == 'left'):
            t4.left -= t4.dx
        if(key == 'right'):
            t4.right += t4.dx
        if(key == 'up'):
            t4.rotateAngle+=90
    if(t4.hitsShape(sides) and t4.centerX<200):
        t4.left=100
    if(t4.hitsShape(sides) and t4.centerX>200):
        t4.right=300
    
    
    
    
    
    #Toggles the pause-menu
    if(key=='tab' and tetrisPic.visible==False):
        menuScore.value=score.value
        togglePause()
        if(app.paused==True):
            pauseMenu.visible=True
            menuScore.visible=True
        else:
            pauseMenu.visible=False 
            menuScore.visible=False


#Things that have to be infront after everything else in the program
startblack.toFront()
tetrisPic.toFront()
start.toFront()
