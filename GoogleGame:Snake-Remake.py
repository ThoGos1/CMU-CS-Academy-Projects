#####My program will mimic the Google Chrome Version of the classic game: Snake
#You Start on the Start Screen and you can move a mouse cursor around and hit play
#When you hit play you get into the game, there is a play space(the tiled part), 
#you a blue snake, a little guide on how to play, an apple on the play space and a top
#menu where you find the applecounter which shows you how many apples you've eaten, 
#a face that shows the mood of the snake, when he moves he's happy, when he is standing
#still he is sad, and a little x, you can hit if you don't want to play anymore
#when you press one of the arrow keys the "tutorial" goes away and you're playing snake
#When you eat/hitsShape an apple it dissapears, the counter goes up and you grow
#if you forget what buttons to press you can press any key on the keyboard 
#and the "tutorial" will show up again.
#If you try going outside of the play space you see the game over screen and it will
#show you how many apples you collected that round and the app stops so you'll have to
#press the run button to play again.



#The Blackground color
app.background='forestGreen'

###Custom App Property
app.appleCount=0

#Image links and the tiled playspace
playSpace = 'https://media.discordapp.net/attachments/554658343776682016/651646208783417354/yes.png?width=349&height=300'
appleImage = 'https://media.discordapp.net/attachments/554658343776682016/651620864605028353/Annotation_2019-12-03_190345.png'
startPicture = 'https://media.discordapp.net/attachments/554658343776682016/651621924278894608/snakeStart.png?width=400&height=400'
cursorPhoto = 'https://media.discordapp.net/attachments/554658343776682016/643525276516745256/actualcursorMini.png'
playButtonImage = 'https://media.discordapp.net/attachments/554658343776682016/651641440753025035/Annotation_2019-12-03_203014.png?width=80&height=30'
gameOver = 'https://media.discordapp.net/attachments/554658343776682016/651659912157593651/gamevoerlol.png'
applePNG = 'https://media.discordapp.net/attachments/554658343776682016/651944079512305686/applelol.png'
arrowKey = 'https://media.discordapp.net/attachments/554658343776682016/651954182533808128/Annotation_2019-12-04_171251.png?width=80&height=80'

#The tiled play space which is where you can move around
screen = Image(playSpace,26,85)

#The top menu 
def drawTopMenu():
    #The green menu background
    Rect(0,0,400,60,fill=rgb(78,115,46))
    
    #The apple in the top left corner
    Image(appleImage,5,10)
    
    

#The Game Over screen you get if you try to go outside of the play space
def drawGameOver():
    Rect(0,0,400,400,opacity=50)
    Image(gameOver,60,60)
    Label(app.appleCount,145,169,fill='white',size=28,bold=True)
    ###app.stop
    app.stop()

#Snake, body, eyes and notrils included
cursor = Group(Oval(110, 230, 45, 23, fill=rgb(81,118,250)),Circle(116,222,5,fill='white',border=rgb(81,118,250)),Circle(116,238,5,fill='white',border=rgb(81,118,250)),Oval(123,227,2,1),Oval(123,232,2,1),Circle(117,222,1), Circle(117,238,1))


###OnKeyPress
def onKeyPress(key):
    
    #Changes snakes location to the new one
    cursor.newX = cursor.centerX
    cursor.newY = cursor.centerY
    
    ###if-elif-else statement
    if (key == 'up'):
        cursor.newY -= 15
        cursor.rotateAngle=270
        keyPrompt.visible=False
        arrowPrompt.visible=False
    elif (key == 'down'):
        cursor.newY += 15
        cursor.rotateAngle=90
        keyPrompt.visible=False
        arrowPrompt.visible=False
    elif (key == 'left'):
        cursor.newX -= 15
        cursor.rotateAngle=180
        keyPrompt.visible=False
        arrowPrompt.visible=False
    elif (key == 'right'):
        cursor.newX += 15
        cursor.rotateAngle=360
        keyPrompt.visible=False
        arrowPrompt.visible=False
    else:
        keyPrompt.visible=True
        arrowPrompt.visible=True
        ###toFront() method
        keyPrompt.toFront()
        cursor.toFront()
        arrowPrompt.toFront()
        ###add.point() method
        keyPrompt.addPoint(260,200)
        keyPrompt.addPoint(238,220)
        keyPrompt.addPoint(167,220)
        keyPrompt.addPoint(145,200)
    
    ###Contains Method
    if (screen.contains(cursor.newX, cursor.newY) == True and startScreen.visible==False):
        cursor.centerX = cursor.newX
        cursor.centerY = cursor.newY
    elif(screen.contains(cursor.newX, cursor.newY) == False):
        drawGameOver()


    ###HitsShape Methods
    if(apple1.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple1.centerX=35234
        print(app.appleCount)
        cursor.width+=10
        apple2.centerX=68
    
    if(apple2.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple2.centerX=35234
        print(app.appleCount)
        cursor.width+=10
        apple3.centerX=89
    
    if(apple3.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple3.centerX=35234
        print(app.appleCount)
        cursor.height+=10
        apple4.centerX=230
    
    if(apple4.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple4.centerX=35234
        print(app.appleCount)
        cursor.width+=10
        apple5.centerX=120
    
    if(apple5.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple5.centerX=35234
        print(app.appleCount)
        cursor.width+=10
        apple6.centerX=160
    
    if(apple6.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple6.centerX=35234
        print(app.appleCount)
        cursor.height+=10
        apple7.centerX=330
    
    if(apple7.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple7.centerX=35234
        print(app.appleCount)
        cursor.height+=10
        apple8.centerX=270
    
    if(apple8.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple8.centerX=35234
        print(app.appleCount)
        cursor.height+=10
        apple9.centerX=253
    
    if(apple9.hitsShape(cursor)):
        app.appleCount+=1
        appleCount.value+=1
        apple9.centerX=35234
        print(app.appleCount)
        cursor.width+=10

    if(appleCount.value==9):
        drawGameOver()
    
    
    sad.visible=False
    happy.visible=True
    
    ###ToFront() Method
    startScreen.toFront()
    playButton.toFront()
    mouseCursor.toFront()

###onKeyRelease
def onKeyRelease(key):
    sad.visible=True
    happy.visible=False


def onMousePress(mouseX,mouseY):
    
    ###HitsShape Method
    if(mouseCursor.hitsShape(playButton)):
        startScreen.visible=False
        playButton.visible=False
        mouseCursor.visible=False
        keyPrompt.visible=True
        arrowPrompt.visible=True
        ###toFront() method
        keyPrompt.toFront()
        arrowPrompt.toFront()
        ###add.point() method
        keyPrompt.addPoint(260,200)
        keyPrompt.addPoint(238,220)
        keyPrompt.addPoint(167,220)
        keyPrompt.addPoint(145,200)
    
    ###Hits Method
    if(x.hits(mouseX,mouseY)):
        startScreen.visible=True
        mouseCursor.visible=True
        ###app.stop 
        app.stop()

def onMouseMove(mouseX,mouseY):
    mouseCursor.centerX=mouseX
    mouseCursor.centerY=mouseY


#Calling of helper function
drawTopMenu()


#Shapes that have to be ontop
x = Label('x',370,30,fill='white',size=25,visible=True)
keyPrompt = Polygon(145,128,167,106,238,106,260,128,opacity=60,visible=True)
arrowPrompt = Image(arrowKey,164,123,visible=True)
apple1 = Image(applePNG,295,210)
apple2 = Image(applePNG,22342,122)
apple3 = Image(applePNG,22342,308)
apple4 = Image(applePNG,22342,305)
apple5 = Image(applePNG,22342,200)
apple6 = Image(applePNG,22342,320)
apple7 = Image(applePNG,22342,150)
apple8 = Image(applePNG,22342,260)
apple9 = Image(applePNG,22342,330)
happy = Label(':)',200,35,fill='white',rotateAngle=90,visible=True,size=30)
sad = Label(':(',200,35,fill='white',rotateAngle=90,visible=False,size=30)
appleCount = Label(app.appleCount,55,30,fill='white',size=40)
startScreen = Image(startPicture,0,0,visible=True)
playButton = Image(playButtonImage,160,181,visible=False)
mouseCursor = Image(cursorPhoto,200,200)

###add.point() method
keyPrompt.addPoint(260,200)
keyPrompt.addPoint(238,220)
keyPrompt.addPoint(167,220)
keyPrompt.addPoint(145,200)
