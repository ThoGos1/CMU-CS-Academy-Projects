##### My program will mimic the Legend of Zelda from 1986
#You start on the start screen, which prompt you to press the mouse to start, when you
#press the mouse you see the world which is made up of a top menu with a ruby counter 
#and a minimap with a small green dot that representing the players movement on the canvas
#in addition a few UI elements are also added.
#You play as Link and you walk around using mouseDrag in passive mode, and if you press
#the mouse button on the pots in the left corner to enter hitting mode and either 
#get a ruby or dust.
#If you go into the water you die so you have to press the run-button to restart
#in addition to that if you run into the top menu you will get lost and therefore
#promted to restart.
#Bushes are also sprinkled around on the canvas which you can explore and find artifacts


#Links two stances, 'p' for passive and 'h' hitting
h = 'https://media.discordapp.net/attachments/554658343776682016/642906625950351370/LinkHitting80x80.png'
p = 'https://media.discordapp.net/attachments/554658343776682016/642909135020752900/LinkLOL50x50.png'

#The two pots in the lower left corner
pot = 'https://media.discordapp.net/attachments/554658343776682016/642906650168131614/ZeldaPot50x50.png'

pot1 = Image(pot,55,290,visible=False)
pot2 = Image(pot,1,290,visible=False)

#Artifacts from the bushes
artifactPhoto = 'https://media.discordapp.net/attachments/554658343776682016/643306464596721675/ZeldaArtifacts.png'
keyPhoto = 'https://media.discordapp.net/attachments/554658343776682016/643306503947681792/ZeldaKey.png'
ballPhoto = 'https://media.discordapp.net/attachments/554658343776682016/643306484297498634/ZeldaBall.png'

key = Image(keyPhoto,78,134,visible=False)
ball = Image(ballPhoto,375,291,visible=False)

#The app background/ground color
app.background='moccasin'

#Link in passive mode
linkp = Image(p,200,200)

#Link in hitting mode
linkh = Image(h,200,200,visible=False)

#Ruby for top menu and pot
rubyPhoto = 'https://media.discordapp.net/attachments/554658343776682016/642973038425407499/Rubypng.png'


###6 Helper functions
#The bushes that set the tone for the environment and that you find artifacts in
def drawBush(OvalX,OvalY):
    Oval(OvalX,OvalY,20,50,fill='green',border='black',borderWidth=1)

#The minimap in the top left corner
def drawMiniMap():
    Rect(2,15,100,70,fill='grey')

#The run button from cmu shown in the game over screen
def drawRun():
    Circle(200,300,15,fill='limeGreen')
    RegularPolygon(200,300,8,3,rotateAngle=90,fill='white')

#Hearts showing Links health points
def drawHeart():
    # Heart 1
    Oval(300,70,20,12,rotateAngle=-35,fill='red')
    Oval(294,70,20,12,rotateAngle=35,fill='red')
    
    # Heart 2
    Oval(330,70,20,12,rotateAngle=-35,fill='red')
    Oval(324,70,20,12,rotateAngle=35,fill='red')


#The artifacts in the top menu and the counter
def drawArtifacts():
    Image(rubyPhoto,110,14)
    Image(artifactPhoto,110,38)
    Label("X",137,24,fill='white',size=20)
    Label(0,150,23.6,fill='white',size=20)
    
    Label("X",137,52,fill='white',size=20)
    Label(0,150,51.6,fill='white',size=20)
    
    Label("X",137,75,fill='white',size=20)
    Label(0,150,74.6,fill='white',size=20)


#The sword used by Link and potraited in the top menu
def drawSword():
    Line(230,50,225,50,fill='lime')
    Line(230,50,235,50,fill='lime')
    Line(230,50,230,30,fill='brown',lineWidth=5)
    Rect(230,30,2,2,fill='brown',align='bottom')
    Line(230,50,230,60,fill='lime',lineWidth=5)
    Line(228,53,232,53,fill='orange')
    Line(228,57,232,57,fill='orange')
    


#The top black menu
def drawTopMenu():
    Rect(0,0,400,90)
    
    ###Helper functions being called inside another function
    drawHeart()
    drawArtifacts()
    drawSword()
    drawMiniMap()
    
    #Label over the amount of health points
    Label("-LIFE-",315,25,fill='red',size=30)
    
    #Makes the "Equipped" part of the top menu
    Rect(215,20,30,50,fill=None,border='blue')
    Rect(170,20,30,50,fill=None,border='blue')
    Rect(180,15,10,10)
    Rect(225,15,10,10)
    Label("B",185,20,fill='white',size=15)
    Label("A",230,20,fill='white',size=15)
    

#The world itself
def drawWorld():
    
    #Artifacts hidden in the bushes
    key.visible=True
    ball.visible=True
    
    ###Helper Functions being called inside other function
    #Top left corner bushes
    drawBush(10,208)
    drawBush(30,198)
    drawBush(50,188)
    drawBush(70,178)
    drawBush(90,163)
    drawBush(110,158)
    drawBush(130,148)
    drawBush(150,138)
    drawBush(170,115)
    drawBush(10,160)
    drawBush(10,115)
    drawBush(30,160)
    drawBush(30,115)
    drawBush(50,153)
    drawBush(50,115)
    drawBush(70,148)
    drawBush(70,115)
    drawBush(90,115)
    drawBush(110,115)
    drawBush(130,115)
    drawBush(150,115)
    
    
    #Bottom right corner bushes
    drawBush(350,316)
    drawBush(370,316)
    drawBush(390,316)
    drawBush(350,266)
    drawBush(370,266)
    drawBush(390,266)
    
    #The water in the bottom of the canvas
    Rect(0,340,400,60,fill='blue')
    
    #The two pots in the bottom left corner
    pot1.visible=True
    pot2.visible=True
    
    

#How to make Link hit a pot
def onMousePress(mouseX,mouseY):
    
    #if Link hits the pot it breaks and he gets a ruby
    if(linkh.hitsShape(pot1)==True):
        pot1.visible=False
        linkh.visible=True
        linkp.visible=False
        Image(rubyPhoto,77,313)
        Rect(144,0,15,40)
        Label(1,150,23.6,fill='white',size=20)
    
    ###3 if-statements working together about getting either dust or artifacts
    if(linkh.hitsShape(pot2)==True):
        pot2.visible=False
        linkh.visible=True
        linkp.visible=False
        Label('You got dust',28,310,size=10)
        Rect(18,335,15,2,fill=rgb(118,85,76))
    
    if(linkp.hitsShape(key)==True):
        Rect(144,40,15,20)
        Label(1,150,52,fill='white',size=20)
    
    if(linkp.hitsShape(ball)==True):
        Rect(144,60,15,25)
        Label(1,150,75,fill='white',size=20)
    
    ###if else Statement
    #If you hit the start button the game starts by removing the start screen and 
    #reseting the rotateAngle of Link else a label shows up and prompts you to click it
    if(cursor.hitsShape(startButton)==True):
        startScreen.visible=False
        linkp.rotateAngle=0
        startButton.visible=False
        startLabel.visible=False
        cursor.visible=False
    else:
        Label('Yes this button',200,380,fill='blue')
        Line(200,370,200,343,fill='blue',arrowEnd=True)
    

#How to switch between the to stances
def onMouseRelease(mouseX,mouseY):
    linkh.visible=False
    linkp.visible=True


###onMouseDrag
#How to move Link around on the canvas
def onMouseDrag(mouseX,mouseY):
    
    ###3 if-Statements working together with the position of Link
    #Moves Link and the dot on the minimap around
    if(mouseY<340):
        linkp.centerX=mouseX
        linkp.centerY=mouseY
        linkh.centerX=mouseX
        linkh.centerY=mouseY
        l.centerX=mouseX/4
        l.centerY=mouseY/4
    
    #Makes it so if you go in the water you have to restart
    if(mouseY>340):
        Rect(0,0,400,400)
        Label("GAME OVER",200,200,size=50,fill='white')
        Label("Link cannot swin",200,133,size=10,fill='white')
        Label("Press the Run Button to Restart",200,270,size=20,fill='white')
        drawRun()

    #Makes it so if you go into the top menu you get lost and have to restart
    if(mouseY<65):
       Rect(0,0,400,400)
       Label('Oh no you lost Link to the',200,150,size=30,fill='white')
       Label('never ending VOID',200,200,size=30,fill='white')
       Label('of the top menu',200,250,size=30,fill='white')
       Label('Looks like you have to restart to continue',200,325,size=15,fill='white')
       drawRun()
    
###onMouseMove
#How to make Link look around
def onMouseMove(mouseX,mouseY):
    linkp.rotateAngle+=1.8
    cursor.centerX=mouseX
    cursor.centerY=mouseY


#The calling of functions
drawTopMenu()
drawWorld()


###Shapes that have to be ontop of the other shapes
#Green dot that follows Links position on the canvas
l = Rect(68,49,5,5,fill='lime',align='center')

#The startscreen
startScreenPhoto = 'https://media.discordapp.net/attachments/554658343776682016/642947238141624321/s.png'
startScreen = Image(startScreenPhoto,0,0)
startButton = RegularPolygon(200,300,8,3,rotateAngle=90,fill='white')
startLabel = Label('Start',200,317,fill='white')
cursorPhoto = 'https://media.discordapp.net/attachments/554658343776682016/643525276516745256/actualcursorMini.png'
cursor = Image(cursorPhoto,200,200)
